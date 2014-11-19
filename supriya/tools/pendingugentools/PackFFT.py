# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.PV_ChainUGen import PV_ChainUGen


class PackFFT(PV_ChainUGen):
    r'''

    ::

        >>> pack_fft = ugentools.PackFFT.(
        ...     bufsize=None,
        ...     chain=None,
        ...     frombin=0,
        ...     magsphases=None,
        ...     tobin=None,
        ...     zeroothers=0,
        ...     )
        >>> pack_fft

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = (
        'chain',
        'bufsize',
        'magsphases',
        'frombin',
        'tobin',
        'zeroothers',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        bufsize=None,
        chain=None,
        frombin=0,
        magsphases=None,
        tobin=None,
        zeroothers=0,
        ):
        PV_ChainUGen.__init__(
            self,
            calculation_rate=calculation_rate,
            bufsize=bufsize,
            chain=chain,
            frombin=frombin,
            magsphases=magsphases,
            tobin=tobin,
            zeroothers=zeroothers,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def new(
        cls,
        bufsize=None,
        chain=None,
        frombin=0,
        magsphases=None,
        tobin=None,
        zeroothers=0,
        ):
        r'''Constructs a PackFFT.

        ::

            >>> pack_fft = ugentools.PackFFT.new(
            ...     bufsize=None,
            ...     chain=None,
            ...     frombin=0,
            ...     magsphases=None,
            ...     tobin=None,
            ...     zeroothers=0,
            ...     )
            >>> pack_fft

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = None
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            bufsize=bufsize,
            chain=chain,
            frombin=frombin,
            magsphases=magsphases,
            tobin=tobin,
            zeroothers=zeroothers,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def bufsize(self):
        r'''Gets `bufsize` input of PackFFT.

        ::

            >>> pack_fft = ugentools.PackFFT.ar(
            ...     bufsize=None,
            ...     chain=None,
            ...     frombin=0,
            ...     magsphases=None,
            ...     tobin=None,
            ...     zeroothers=0,
            ...     )
            >>> pack_fft.bufsize

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('bufsize')
        return self._inputs[index]

    @property
    def chain(self):
        r'''Gets `chain` input of PackFFT.

        ::

            >>> pack_fft = ugentools.PackFFT.ar(
            ...     bufsize=None,
            ...     chain=None,
            ...     frombin=0,
            ...     magsphases=None,
            ...     tobin=None,
            ...     zeroothers=0,
            ...     )
            >>> pack_fft.chain

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('chain')
        return self._inputs[index]

    @property
    def frombin(self):
        r'''Gets `frombin` input of PackFFT.

        ::

            >>> pack_fft = ugentools.PackFFT.ar(
            ...     bufsize=None,
            ...     chain=None,
            ...     frombin=0,
            ...     magsphases=None,
            ...     tobin=None,
            ...     zeroothers=0,
            ...     )
            >>> pack_fft.frombin

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('frombin')
        return self._inputs[index]

    @property
    def magsphases(self):
        r'''Gets `magsphases` input of PackFFT.

        ::

            >>> pack_fft = ugentools.PackFFT.ar(
            ...     bufsize=None,
            ...     chain=None,
            ...     frombin=0,
            ...     magsphases=None,
            ...     tobin=None,
            ...     zeroothers=0,
            ...     )
            >>> pack_fft.magsphases

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('magsphases')
        return self._inputs[index]

    @property
    def tobin(self):
        r'''Gets `tobin` input of PackFFT.

        ::

            >>> pack_fft = ugentools.PackFFT.ar(
            ...     bufsize=None,
            ...     chain=None,
            ...     frombin=0,
            ...     magsphases=None,
            ...     tobin=None,
            ...     zeroothers=0,
            ...     )
            >>> pack_fft.tobin

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('tobin')
        return self._inputs[index]

    @property
    def zeroothers(self):
        r'''Gets `zeroothers` input of PackFFT.

        ::

            >>> pack_fft = ugentools.PackFFT.ar(
            ...     bufsize=None,
            ...     chain=None,
            ...     frombin=0,
            ...     magsphases=None,
            ...     tobin=None,
            ...     zeroothers=0,
            ...     )
            >>> pack_fft.zeroothers

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('zeroothers')
        return self._inputs[index]