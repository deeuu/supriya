import collections
from supriya.enums import CalculationRate
from supriya.ugens.Index import Index


class IndexInBetween(Index):
    """

    ::

        >>> source = supriya.ugens.In.ar(bus=0)
        >>> index_in_between = supriya.ugens.IndexInBetween.ar(
        ...     buffer_id=buffer_id,
        ...     source=source,
        ...     )
        >>> index_in_between
        IndexInBetween.ar()

    """

    ### CLASS VARIABLES ###

    _ordered_input_names = collections.OrderedDict(
        'buffer_id',
        'source',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        buffer_id=None,
        source=None,
        ):
        Index.__init__(
            self,
            calculation_rate=calculation_rate,
            buffer_id=buffer_id,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        buffer_id=None,
        source=None,
        ):
        """
        Constructs an audio-rate IndexInBetween.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> index_in_between = supriya.ugens.IndexInBetween.ar(
            ...     buffer_id=buffer_id,
            ...     source=source,
            ...     )
            >>> index_in_between
            IndexInBetween.ar()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            buffer_id=buffer_id,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        buffer_id=None,
        source=None,
        ):
        """
        Constructs a control-rate IndexInBetween.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> index_in_between = supriya.ugens.IndexInBetween.kr(
            ...     buffer_id=buffer_id,
            ...     source=source,
            ...     )
            >>> index_in_between
            IndexInBetween.kr()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            buffer_id=buffer_id,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def buffer_id(self):
        """
        Gets `buffer_id` input of IndexInBetween.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> index_in_between = supriya.ugens.IndexInBetween.ar(
            ...     buffer_id=buffer_id,
            ...     source=source,
            ...     )
            >>> index_in_between.buffer_id

        Returns ugen input.
        """
        index = self._ordered_input_names.index('buffer_id')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of IndexInBetween.

        ::

            >>> source = supriya.ugens.In.ar(bus=0)
            >>> index_in_between = supriya.ugens.IndexInBetween.ar(
            ...     buffer_id=buffer_id,
            ...     source=source,
            ...     )
            >>> index_in_between.source
            OutputProxy(
                source=In(
                    bus=0.0,
                    calculation_rate=CalculationRate.AUDIO,
                    channel_count=1
                    ),
                output_index=0
                )

        Returns ugen input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
