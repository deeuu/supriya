# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.LagUD import LagUD


class Lag2UD(LagUD):
    r'''

    ::

        >>> lag_2_ud = ugentools.Lag2UD.(
        ...     lag_time_d=0.1,
        ...     lag_time_u=0.1,
        ...     source=None,
        ...     )
        >>> lag_2_ud

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'lag_time_u',
        'lag_time_d',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        lag_time_d=0.1,
        lag_time_u=0.1,
        source=None,
        ):
        LagUD.__init__(
            self,
            calculation_rate=calculation_rate,
            lag_time_d=lag_time_d,
            lag_time_u=lag_time_u,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        lag_time_d=0.1,
        lag_time_u=0.1,
        source=None,
        ):
        r'''Constructs an audio-rate Lag2UD.

        ::

            >>> lag_2_ud = ugentools.Lag2UD.ar(
            ...     lag_time_d=0.1,
            ...     lag_time_u=0.1,
            ...     source=None,
            ...     )
            >>> lag_2_ud

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            lag_time_d=lag_time_d,
            lag_time_u=lag_time_u,
            source=source,
            )
        return ugen

    # def coeffs(): ...

    @classmethod
    def kr(
        cls,
        lag_time_d=0.1,
        lag_time_u=0.1,
        source=None,
        ):
        r'''Constructs a control-rate Lag2UD.

        ::

            >>> lag_2_ud = ugentools.Lag2UD.kr(
            ...     lag_time_d=0.1,
            ...     lag_time_u=0.1,
            ...     source=None,
            ...     )
            >>> lag_2_ud

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            lag_time_d=lag_time_d,
            lag_time_u=lag_time_u,
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
        r'''Gets `source` input of Lag2UD.

        ::

            >>> lag_2_ud = ugentools.Lag2UD.ar(
            ...     lag_time_d=0.1,
            ...     lag_time_u=0.1,
            ...     source=None,
            ...     )
            >>> lag_2_ud.source

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('source')
        return self._inputs[index]

    @property
    def lag_time_u(self):
        r'''Gets `lag_time_u` input of Lag2UD.

        ::

            >>> lag_2_ud = ugentools.Lag2UD.ar(
            ...     lag_time_d=0.1,
            ...     lag_time_u=0.1,
            ...     source=None,
            ...     )
            >>> lag_2_ud.lag_time_u

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('lag_time_u')
        return self._inputs[index]

    @property
    def lag_time_d(self):
        r'''Gets `lag_time_d` input of Lag2UD.

        ::

            >>> lag_2_ud = ugentools.Lag2UD.ar(
            ...     lag_time_d=0.1,
            ...     lag_time_u=0.1,
            ...     source=None,
            ...     )
            >>> lag_2_ud.lag_time_d

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('lag_time_d')
        return self._inputs[index]