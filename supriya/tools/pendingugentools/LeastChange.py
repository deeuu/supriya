# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.MostChange import MostChange


class LeastChange(MostChange):
    r'''

    ::

        >>> least_change = ugentools.LeastChange.(
        ...     a=0,
        ...     b=0,
        ...     )
        >>> least_change

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = (
        'a',
        'b',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        a=0,
        b=0,
        ):
        MostChange.__init__(
            self,
            calculation_rate=calculation_rate,
            a=a,
            b=b,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        a=0,
        b=0,
        ):
        r'''Constructs an audio-rate LeastChange.

        ::

            >>> least_change = ugentools.LeastChange.ar(
            ...     a=0,
            ...     b=0,
            ...     )
            >>> least_change

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            a=a,
            b=b,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        a=0,
        b=0,
        ):
        r'''Constructs a control-rate LeastChange.

        ::

            >>> least_change = ugentools.LeastChange.kr(
            ...     a=0,
            ...     b=0,
            ...     )
            >>> least_change

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            a=a,
            b=b,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def a(self):
        r'''Gets `a` input of LeastChange.

        ::

            >>> least_change = ugentools.LeastChange.ar(
            ...     a=0,
            ...     b=0,
            ...     )
            >>> least_change.a

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('a')
        return self._inputs[index]

    @property
    def b(self):
        r'''Gets `b` input of LeastChange.

        ::

            >>> least_change = ugentools.LeastChange.ar(
            ...     a=0,
            ...     b=0,
            ...     )
            >>> least_change.b

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('b')
        return self._inputs[index]