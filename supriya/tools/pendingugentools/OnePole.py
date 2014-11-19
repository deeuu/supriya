# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.Filter import Filter


class OnePole(Filter):
    r'''

    ::

        >>> one_pole = ugentools.OnePole.(
        ...     coefficient=0.5,
        ...     source=None,
        ...     )
        >>> one_pole

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'coefficient',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        coefficient=0.5,
        source=None,
        ):
        Filter.__init__(
            self,
            calculation_rate=calculation_rate,
            coefficient=coefficient,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        coefficient=0.5,
        source=None,
        ):
        r'''Constructs an audio-rate OnePole.

        ::

            >>> one_pole = ugentools.OnePole.ar(
            ...     coefficient=0.5,
            ...     source=None,
            ...     )
            >>> one_pole

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            coefficient=coefficient,
            source=source,
            )
        return ugen

    # def coeffs(): ...

    @classmethod
    def kr(
        cls,
        coefficient=0.5,
        source=None,
        ):
        r'''Constructs a control-rate OnePole.

        ::

            >>> one_pole = ugentools.OnePole.kr(
            ...     coefficient=0.5,
            ...     source=None,
            ...     )
            >>> one_pole

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            coefficient=coefficient,
            source=source,
            )
        return ugen

    # def magResponse(): ...

    # def magResponse2(): ...

    # def magResponse5(): ...

    # def magResponseN(): ...

    # def scopeResponse(): ...

    ### PUBLIC PROPERTIES ###

    @property
    def source(self):
        r'''Gets `source` input of OnePole.

        ::

            >>> one_pole = ugentools.OnePole.ar(
            ...     coefficient=0.5,
            ...     source=None,
            ...     )
            >>> one_pole.source

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('source')
        return self._inputs[index]

    @property
    def coefficient(self):
        r'''Gets `coefficient` input of OnePole.

        ::

            >>> one_pole = ugentools.OnePole.ar(
            ...     coefficient=0.5,
            ...     source=None,
            ...     )
            >>> one_pole.coefficient

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('coefficient')
        return self._inputs[index]