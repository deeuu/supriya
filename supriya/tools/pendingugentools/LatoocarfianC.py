# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.LatoocarfianN import LatoocarfianN


class LatoocarfianC(LatoocarfianN):
    r'''

    ::

        >>> latoocarfian_c = ugentools.LatoocarfianC.(
        ...     a=1,
        ...     b=3,
        ...     c=0.5,
        ...     d=0.5,
        ...     frequency=22050,
        ...     xi=0.5,
        ...     yi=0.5,
        ...     )
        >>> latoocarfian_c

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = (
        'frequency',
        'a',
        'b',
        'c',
        'd',
        'xi',
        'yi',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        a=1,
        b=3,
        c=0.5,
        d=0.5,
        frequency=22050,
        xi=0.5,
        yi=0.5,
        ):
        LatoocarfianN.__init__(
            self,
            calculation_rate=calculation_rate,
            a=a,
            b=b,
            c=c,
            d=d,
            frequency=frequency,
            xi=xi,
            yi=yi,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        a=1,
        b=3,
        c=0.5,
        d=0.5,
        frequency=22050,
        xi=0.5,
        yi=0.5,
        ):
        r'''Constructs an audio-rate LatoocarfianC.

        ::

            >>> latoocarfian_c = ugentools.LatoocarfianC.ar(
            ...     a=1,
            ...     b=3,
            ...     c=0.5,
            ...     d=0.5,
            ...     frequency=22050,
            ...     xi=0.5,
            ...     yi=0.5,
            ...     )
            >>> latoocarfian_c

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            a=a,
            b=b,
            c=c,
            d=d,
            frequency=frequency,
            xi=xi,
            yi=yi,
            )
        return ugen

    # def equation(): ...

    ### PUBLIC PROPERTIES ###

    @property
    def frequency(self):
        r'''Gets `frequency` input of LatoocarfianC.

        ::

            >>> latoocarfian_c = ugentools.LatoocarfianC.ar(
            ...     a=1,
            ...     b=3,
            ...     c=0.5,
            ...     d=0.5,
            ...     frequency=22050,
            ...     xi=0.5,
            ...     yi=0.5,
            ...     )
            >>> latoocarfian_c.frequency

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('frequency')
        return self._inputs[index]

    @property
    def a(self):
        r'''Gets `a` input of LatoocarfianC.

        ::

            >>> latoocarfian_c = ugentools.LatoocarfianC.ar(
            ...     a=1,
            ...     b=3,
            ...     c=0.5,
            ...     d=0.5,
            ...     frequency=22050,
            ...     xi=0.5,
            ...     yi=0.5,
            ...     )
            >>> latoocarfian_c.a

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('a')
        return self._inputs[index]

    @property
    def b(self):
        r'''Gets `b` input of LatoocarfianC.

        ::

            >>> latoocarfian_c = ugentools.LatoocarfianC.ar(
            ...     a=1,
            ...     b=3,
            ...     c=0.5,
            ...     d=0.5,
            ...     frequency=22050,
            ...     xi=0.5,
            ...     yi=0.5,
            ...     )
            >>> latoocarfian_c.b

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('b')
        return self._inputs[index]

    @property
    def c(self):
        r'''Gets `c` input of LatoocarfianC.

        ::

            >>> latoocarfian_c = ugentools.LatoocarfianC.ar(
            ...     a=1,
            ...     b=3,
            ...     c=0.5,
            ...     d=0.5,
            ...     frequency=22050,
            ...     xi=0.5,
            ...     yi=0.5,
            ...     )
            >>> latoocarfian_c.c

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('c')
        return self._inputs[index]

    @property
    def d(self):
        r'''Gets `d` input of LatoocarfianC.

        ::

            >>> latoocarfian_c = ugentools.LatoocarfianC.ar(
            ...     a=1,
            ...     b=3,
            ...     c=0.5,
            ...     d=0.5,
            ...     frequency=22050,
            ...     xi=0.5,
            ...     yi=0.5,
            ...     )
            >>> latoocarfian_c.d

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('d')
        return self._inputs[index]

    @property
    def xi(self):
        r'''Gets `xi` input of LatoocarfianC.

        ::

            >>> latoocarfian_c = ugentools.LatoocarfianC.ar(
            ...     a=1,
            ...     b=3,
            ...     c=0.5,
            ...     d=0.5,
            ...     frequency=22050,
            ...     xi=0.5,
            ...     yi=0.5,
            ...     )
            >>> latoocarfian_c.xi

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('xi')
        return self._inputs[index]

    @property
    def yi(self):
        r'''Gets `yi` input of LatoocarfianC.

        ::

            >>> latoocarfian_c = ugentools.LatoocarfianC.ar(
            ...     a=1,
            ...     b=3,
            ...     c=0.5,
            ...     d=0.5,
            ...     frequency=22050,
            ...     xi=0.5,
            ...     yi=0.5,
            ...     )
            >>> latoocarfian_c.yi

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('yi')
        return self._inputs[index]