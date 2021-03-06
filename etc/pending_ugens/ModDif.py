import collections
from supriya.enums import CalculationRate
from supriya.synthdefs import UGen


class ModDif(UGen):
    """

    ::

        >>> mod_dif = supriya.ugens.ModDif.ar(
        ...     mod=1,
        ...     x=0,
        ...     y=0,
        ...     )
        >>> mod_dif
        ModDif.ar()

    """

    ### CLASS VARIABLES ###

    _ordered_input_names = collections.OrderedDict(
        'x',
        'y',
        'mod',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        mod=1,
        x=0,
        y=0,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            mod=mod,
            x=x,
            y=y,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        mod=1,
        x=0,
        y=0,
        ):
        """
        Constructs an audio-rate ModDif.

        ::

            >>> mod_dif = supriya.ugens.ModDif.ar(
            ...     mod=1,
            ...     x=0,
            ...     y=0,
            ...     )
            >>> mod_dif
            ModDif.ar()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            mod=mod,
            x=x,
            y=y,
            )
        return ugen

    @classmethod
    def ir(
        cls,
        mod=1,
        x=0,
        y=0,
        ):
        """
        Constructs a scale-rate ModDif.

        ::

            >>> mod_dif = supriya.ugens.ModDif.ir(
            ...     mod=1,
            ...     x=0,
            ...     y=0,
            ...     )
            >>> mod_dif
            ModDif.ir()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.CalculationRate.SCALAR
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            mod=mod,
            x=x,
            y=y,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        mod=1,
        x=0,
        y=0,
        ):
        """
        Constructs a control-rate ModDif.

        ::

            >>> mod_dif = supriya.ugens.ModDif.kr(
            ...     mod=1,
            ...     x=0,
            ...     y=0,
            ...     )
            >>> mod_dif
            ModDif.kr()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            mod=mod,
            x=x,
            y=y,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def mod(self):
        """
        Gets `mod` input of ModDif.

        ::

            >>> mod_dif = supriya.ugens.ModDif.ar(
            ...     mod=1,
            ...     x=0,
            ...     y=0,
            ...     )
            >>> mod_dif.mod
            1.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('mod')
        return self._inputs[index]

    @property
    def x(self):
        """
        Gets `x` input of ModDif.

        ::

            >>> mod_dif = supriya.ugens.ModDif.ar(
            ...     mod=1,
            ...     x=0,
            ...     y=0,
            ...     )
            >>> mod_dif.x
            0.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('x')
        return self._inputs[index]

    @property
    def y(self):
        """
        Gets `y` input of ModDif.

        ::

            >>> mod_dif = supriya.ugens.ModDif.ar(
            ...     mod=1,
            ...     x=0,
            ...     y=0,
            ...     )
            >>> mod_dif.y
            0.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('y')
        return self._inputs[index]
