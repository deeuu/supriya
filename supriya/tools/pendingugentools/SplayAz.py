# -*- encoding: utf-8 -*-
from supriya.tools.synthdeftools.UGen import UGen


class SplayAz(UGen):
    r'''

    ::

        >>> splay_az = ugentools.SplayAz.(
        ...     center=0,
        ...     channel_count=4,
        ...     in_array=None,
        ...     level=1,
        ...     level_comp=True,
        ...     orientation=0.5,
        ...     spread=1,
        ...     width=2,
        ...     )
        >>> splay_az

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = (
        'channel_count',
        'in_array',
        'spread',
        'level',
        'width',
        'center',
        'orientation',
        'level_comp',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        center=0,
        channel_count=4,
        in_array=None,
        level=1,
        level_comp=True,
        orientation=0.5,
        spread=1,
        width=2,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            center=center,
            channel_count=channel_count,
            in_array=in_array,
            level=level,
            level_comp=level_comp,
            orientation=orientation,
            spread=spread,
            width=width,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        center=0,
        channel_count=4,
        in_array=None,
        level=1,
        level_comp=True,
        orientation=0.5,
        spread=1,
        width=2,
        ):
        r'''Constructs an audio-rate SplayAz.

        ::

            >>> splay_az = ugentools.SplayAz.ar(
            ...     center=0,
            ...     channel_count=4,
            ...     in_array=None,
            ...     level=1,
            ...     level_comp=True,
            ...     orientation=0.5,
            ...     spread=1,
            ...     width=2,
            ...     )
            >>> splay_az

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            center=center,
            channel_count=channel_count,
            in_array=in_array,
            level=level,
            level_comp=level_comp,
            orientation=orientation,
            spread=spread,
            width=width,
            )
        return ugen

    # def arFill(): ...

    @classmethod
    def kr(
        cls,
        center=0,
        channel_count=4,
        in_array=None,
        level=1,
        level_comp=True,
        orientation=0.5,
        spread=1,
        width=2,
        ):
        r'''Constructs a control-rate SplayAz.

        ::

            >>> splay_az = ugentools.SplayAz.kr(
            ...     center=0,
            ...     channel_count=4,
            ...     in_array=None,
            ...     level=1,
            ...     level_comp=True,
            ...     orientation=0.5,
            ...     spread=1,
            ...     width=2,
            ...     )
            >>> splay_az

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            center=center,
            channel_count=channel_count,
            in_array=in_array,
            level=level,
            level_comp=level_comp,
            orientation=orientation,
            spread=spread,
            width=width,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def channel_count(self):
        r'''Gets `channel_count` input of SplayAz.

        ::

            >>> splay_az = ugentools.SplayAz.ar(
            ...     center=0,
            ...     channel_count=4,
            ...     in_array=None,
            ...     level=1,
            ...     level_comp=True,
            ...     orientation=0.5,
            ...     spread=1,
            ...     width=2,
            ...     )
            >>> splay_az.channel_count

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('channel_count')
        return self._inputs[index]

    @property
    def in_array(self):
        r'''Gets `in_array` input of SplayAz.

        ::

            >>> splay_az = ugentools.SplayAz.ar(
            ...     center=0,
            ...     channel_count=4,
            ...     in_array=None,
            ...     level=1,
            ...     level_comp=True,
            ...     orientation=0.5,
            ...     spread=1,
            ...     width=2,
            ...     )
            >>> splay_az.in_array

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('in_array')
        return self._inputs[index]

    @property
    def spread(self):
        r'''Gets `spread` input of SplayAz.

        ::

            >>> splay_az = ugentools.SplayAz.ar(
            ...     center=0,
            ...     channel_count=4,
            ...     in_array=None,
            ...     level=1,
            ...     level_comp=True,
            ...     orientation=0.5,
            ...     spread=1,
            ...     width=2,
            ...     )
            >>> splay_az.spread

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('spread')
        return self._inputs[index]

    @property
    def level(self):
        r'''Gets `level` input of SplayAz.

        ::

            >>> splay_az = ugentools.SplayAz.ar(
            ...     center=0,
            ...     channel_count=4,
            ...     in_array=None,
            ...     level=1,
            ...     level_comp=True,
            ...     orientation=0.5,
            ...     spread=1,
            ...     width=2,
            ...     )
            >>> splay_az.level

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('level')
        return self._inputs[index]

    @property
    def width(self):
        r'''Gets `width` input of SplayAz.

        ::

            >>> splay_az = ugentools.SplayAz.ar(
            ...     center=0,
            ...     channel_count=4,
            ...     in_array=None,
            ...     level=1,
            ...     level_comp=True,
            ...     orientation=0.5,
            ...     spread=1,
            ...     width=2,
            ...     )
            >>> splay_az.width

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('width')
        return self._inputs[index]

    @property
    def center(self):
        r'''Gets `center` input of SplayAz.

        ::

            >>> splay_az = ugentools.SplayAz.ar(
            ...     center=0,
            ...     channel_count=4,
            ...     in_array=None,
            ...     level=1,
            ...     level_comp=True,
            ...     orientation=0.5,
            ...     spread=1,
            ...     width=2,
            ...     )
            >>> splay_az.center

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('center')
        return self._inputs[index]

    @property
    def orientation(self):
        r'''Gets `orientation` input of SplayAz.

        ::

            >>> splay_az = ugentools.SplayAz.ar(
            ...     center=0,
            ...     channel_count=4,
            ...     in_array=None,
            ...     level=1,
            ...     level_comp=True,
            ...     orientation=0.5,
            ...     spread=1,
            ...     width=2,
            ...     )
            >>> splay_az.orientation

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('orientation')
        return self._inputs[index]

    @property
    def level_comp(self):
        r'''Gets `level_comp` input of SplayAz.

        ::

            >>> splay_az = ugentools.SplayAz.ar(
            ...     center=0,
            ...     channel_count=4,
            ...     in_array=None,
            ...     level=1,
            ...     level_comp=True,
            ...     orientation=0.5,
            ...     spread=1,
            ...     width=2,
            ...     )
            >>> splay_az.level_comp

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('level_comp')
        return self._inputs[index]