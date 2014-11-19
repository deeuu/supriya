# -*- encoding: utf-8 -*-
from supriya.tools.synthdeftools.UGen import UGen


class Unpack1FFT(UGen):
    r'''

    ::

        >>> unpack_1_fft = ugentools.Unpack1FFT.(
        ...     binindex=None,
        ...     bufsize=None,
        ...     chain=None,
        ...     whichmeasure=0,
        ...     )
        >>> unpack_1_fft

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = (
        'chain',
        'bufsize',
        'binindex',
        'whichmeasure',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        binindex=None,
        bufsize=None,
        chain=None,
        whichmeasure=0,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            binindex=binindex,
            bufsize=bufsize,
            chain=chain,
            whichmeasure=whichmeasure,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def new(
        cls,
        binindex=None,
        bufsize=None,
        chain=None,
        whichmeasure=0,
        ):
        r'''Constructs a Unpack1FFT.

        ::

            >>> unpack_1_fft = ugentools.Unpack1FFT.new(
            ...     binindex=None,
            ...     bufsize=None,
            ...     chain=None,
            ...     whichmeasure=0,
            ...     )
            >>> unpack_1_fft

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = None
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            binindex=binindex,
            bufsize=bufsize,
            chain=chain,
            whichmeasure=whichmeasure,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def binindex(self):
        r'''Gets `binindex` input of Unpack1FFT.

        ::

            >>> unpack_1_fft = ugentools.Unpack1FFT.ar(
            ...     binindex=None,
            ...     bufsize=None,
            ...     chain=None,
            ...     whichmeasure=0,
            ...     )
            >>> unpack_1_fft.binindex

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('binindex')
        return self._inputs[index]

    @property
    def bufsize(self):
        r'''Gets `bufsize` input of Unpack1FFT.

        ::

            >>> unpack_1_fft = ugentools.Unpack1FFT.ar(
            ...     binindex=None,
            ...     bufsize=None,
            ...     chain=None,
            ...     whichmeasure=0,
            ...     )
            >>> unpack_1_fft.bufsize

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('bufsize')
        return self._inputs[index]

    @property
    def chain(self):
        r'''Gets `chain` input of Unpack1FFT.

        ::

            >>> unpack_1_fft = ugentools.Unpack1FFT.ar(
            ...     binindex=None,
            ...     bufsize=None,
            ...     chain=None,
            ...     whichmeasure=0,
            ...     )
            >>> unpack_1_fft.chain

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('chain')
        return self._inputs[index]

    @property
    def whichmeasure(self):
        r'''Gets `whichmeasure` input of Unpack1FFT.

        ::

            >>> unpack_1_fft = ugentools.Unpack1FFT.ar(
            ...     binindex=None,
            ...     bufsize=None,
            ...     chain=None,
            ...     whichmeasure=0,
            ...     )
            >>> unpack_1_fft.whichmeasure

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('whichmeasure')
        return self._inputs[index]