# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.Filter import Filter


class Slew(Filter):
    r'''

    ::

        >>> slew = ugentools.Slew.(
        ...     dn=1,
        ...     source=None,
        ...     up=1,
        ...     )
        >>> slew

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'up',
        'dn',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        dn=1,
        source=None,
        up=1,
        ):
        Filter.__init__(
            self,
            calculation_rate=calculation_rate,
            dn=dn,
            source=source,
            up=up,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        dn=1,
        source=None,
        up=1,
        ):
        r'''Constructs an audio-rate Slew.

        ::

            >>> slew = ugentools.Slew.ar(
            ...     dn=1,
            ...     source=None,
            ...     up=1,
            ...     )
            >>> slew

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            dn=dn,
            source=source,
            up=up,
            )
        return ugen

    # def coeffs(): ...

    @classmethod
    def kr(
        cls,
        dn=1,
        source=None,
        up=1,
        ):
        r'''Constructs a control-rate Slew.

        ::

            >>> slew = ugentools.Slew.kr(
            ...     dn=1,
            ...     source=None,
            ...     up=1,
            ...     )
            >>> slew

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            dn=dn,
            source=source,
            up=up,
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
        r'''Gets `source` input of Slew.

        ::

            >>> slew = ugentools.Slew.ar(
            ...     dn=1,
            ...     source=None,
            ...     up=1,
            ...     )
            >>> slew.source

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('source')
        return self._inputs[index]

    @property
    def up(self):
        r'''Gets `up` input of Slew.

        ::

            >>> slew = ugentools.Slew.ar(
            ...     dn=1,
            ...     source=None,
            ...     up=1,
            ...     )
            >>> slew.up

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('up')
        return self._inputs[index]

    @property
    def dn(self):
        r'''Gets `dn` input of Slew.

        ::

            >>> slew = ugentools.Slew.ar(
            ...     dn=1,
            ...     source=None,
            ...     up=1,
            ...     )
            >>> slew.dn

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('dn')
        return self._inputs[index]