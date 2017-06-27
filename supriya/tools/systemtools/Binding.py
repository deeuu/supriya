import inspect


class Binding:

    ### CLASS VARIABLES ###

    __slots__ = (
        'clip_maximum',
        'clip_minimum',
        'exponent',
        'source',
        'source_range',
        'symmetric',
        'target',
        'target_range',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        source,
        target,
        source_range=None,
        target_range=None,
        clip_minimum=None,
        clip_maximum=None,
        exponent=None,
        symmetric=None,
        ):
        from supriya.tools import synthdeftools
        self.source = self.patch(source)
        self.target = self.patch(target)
        if source_range is None:
            if hasattr(self.source.func.__self__, 'range_'):
                source_range = self.source.func.__self__.range_
            else:
                source_range = (0., 1.)
        self.source_range = synthdeftools.Range(source_range)
        if target_range is None:
            if (
                hasattr(self.target.func, '__self__') and
                hasattr(self.target.func.__self__, 'range_')
                ):
                target_range = self.target.func.__self__.range_
            else:
                target_range = (0., 1.)
        self.target_range = synthdeftools.Range(target_range)
        self.clip_maximum = bool(clip_maximum)
        self.clip_minimum = bool(clip_minimum)
        if exponent is None:
            exponent = 1.0
        self.exponent = float(exponent)
        self.symmetric = bool(symmetric)
        self.source.outgoing_bindings.add(self)
        self.target.incoming_bindings.add(self)

    ### PUBLIC METHODS ###

    def is_class_instance(self, object_):
        return (
            hasattr(object_, '__class__') and
            ('__dict__' in dir(object_) or hasattr(object_, '__slots__'))
            )

    def patch(self, object_):
        from supriya.tools import systemtools
        if self.is_class_instance(object_) and hasattr(object_, '__call__'):
            instance = object_
            class_ = type(object_)
            method_name = '__call__'
        elif inspect.ismethod(object_):
            instance = object_.__self__
            class_ = type(instance)
            method_name = object_.__name__
        else:
            raise TypeError
        function = getattr(instance, method_name)
        if isinstance(function, systemtools.Bindable):
            return function
        function = getattr(class_, method_name)
        bindable = systemtools.Bindable(function)
        setattr(class_, method_name, bindable)
        bindable = getattr(instance, method_name)
        return bindable

    @staticmethod
    def perform_mapping(
        value,
        input_range,
        output_range,
        exponent=1,
        symmetric=False,
        ):
        value = (value - input_range.minimum) / input_range.width
        if exponent != 1:
            if symmetric and value >= 0.5:
                value = (pow((value - 0.5) * 2, exponent) / 2) + 0.5
            elif symmetric and value < 0.5:
                value = (1 - pow(1 - (value * 2), exponent)) / 2
            else:
                value = pow(value, exponent)
        return (value * output_range.width) + output_range.minimum

    def perform_outgoing(self, value):
        if self.target.forbid_reentrancy:
            return
        value = self.perform_mapping(
            value,
            self.source_range,
            self.target_range,
            exponent=self.exponent,
            symmetric=self.symmetric,
            )
        self.target(value)

    def perform_incoming(self, value):
        # TODO: handle exponent and symmetric in reverse
        if self.source.forbid_reentrancy:
            return
        value = self.perform_mapping(
            value,
            self.target_range,
            self.source_range,
            )
        self.source(value)

    def unbind(self):
        self.source.outgoing_bindings.remove(self)
        self.target.incoming_bindings.remove(self)
