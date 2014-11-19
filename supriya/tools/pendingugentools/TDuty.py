# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.Duty import Duty


class TDuty(Duty):
    r'''

    ::

        >>> tduty = ugentools.TDuty.(
        ...     done_action=0,
        ...     duration=1,
        ...     gap_first=0,
        ...     level=1,
        ...     reset=0,
        ...     )
        >>> tduty

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = (
        'duration',
        'reset',
        'level',
        'done_action',
        'gap_first',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        done_action=0,
        duration=1,
        gap_first=0,
        level=1,
        reset=0,
        ):
        Duty.__init__(
            self,
            calculation_rate=calculation_rate,
            done_action=done_action,
            duration=duration,
            gap_first=gap_first,
            level=level,
            reset=reset,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        done_action=0,
        duration=1,
        gap_first=0,
        level=1,
        reset=0,
        ):
        r'''Constructs an audio-rate TDuty.

        ::

            >>> tduty = ugentools.TDuty.ar(
            ...     done_action=0,
            ...     duration=1,
            ...     gap_first=0,
            ...     level=1,
            ...     reset=0,
            ...     )
            >>> tduty

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            done_action=done_action,
            duration=duration,
            gap_first=gap_first,
            level=level,
            reset=reset,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        done_action=0,
        duration=1,
        gap_first=0,
        level=1,
        reset=0,
        ):
        r'''Constructs a control-rate TDuty.

        ::

            >>> tduty = ugentools.TDuty.kr(
            ...     done_action=0,
            ...     duration=1,
            ...     gap_first=0,
            ...     level=1,
            ...     reset=0,
            ...     )
            >>> tduty

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            done_action=done_action,
            duration=duration,
            gap_first=gap_first,
            level=level,
            reset=reset,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def duration(self):
        r'''Gets `duration` input of TDuty.

        ::

            >>> tduty = ugentools.TDuty.ar(
            ...     done_action=0,
            ...     duration=1,
            ...     gap_first=0,
            ...     level=1,
            ...     reset=0,
            ...     )
            >>> tduty.duration

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('duration')
        return self._inputs[index]

    @property
    def reset(self):
        r'''Gets `reset` input of TDuty.

        ::

            >>> tduty = ugentools.TDuty.ar(
            ...     done_action=0,
            ...     duration=1,
            ...     gap_first=0,
            ...     level=1,
            ...     reset=0,
            ...     )
            >>> tduty.reset

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('reset')
        return self._inputs[index]

    @property
    def level(self):
        r'''Gets `level` input of TDuty.

        ::

            >>> tduty = ugentools.TDuty.ar(
            ...     done_action=0,
            ...     duration=1,
            ...     gap_first=0,
            ...     level=1,
            ...     reset=0,
            ...     )
            >>> tduty.level

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('level')
        return self._inputs[index]

    @property
    def done_action(self):
        r'''Gets `done_action` input of TDuty.

        ::

            >>> tduty = ugentools.TDuty.ar(
            ...     done_action=0,
            ...     duration=1,
            ...     gap_first=0,
            ...     level=1,
            ...     reset=0,
            ...     )
            >>> tduty.done_action

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('done_action')
        return self._inputs[index]

    @property
    def gap_first(self):
        r'''Gets `gap_first` input of TDuty.

        ::

            >>> tduty = ugentools.TDuty.ar(
            ...     done_action=0,
            ...     duration=1,
            ...     gap_first=0,
            ...     level=1,
            ...     reset=0,
            ...     )
            >>> tduty.gap_first

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('gap_first')
        return self._inputs[index]