import collections

import supriya.osc
from supriya.enums import RequestId

from .BufferAllocateReadRequest import BufferAllocateReadRequest


class BufferAllocateReadChannelRequest(BufferAllocateReadRequest):
    """
    A /b_allocRead request.

    ::

        >>> import supriya.commands
        >>> request = supriya.commands.BufferAllocateReadChannelRequest(
        ...     buffer_id=23,
        ...     channel_indices=(3, 4),
        ...     file_path='pulse_44100sr_16bit_octo.wav',
        ...     )
        >>> print(request)
        BufferAllocateReadChannelRequest(
            buffer_id=23,
            channel_indices=(3, 4),
            file_path='pulse_44100sr_16bit_octo.wav',
            )

    ::

        >>> request.to_osc()
        OscMessage('/b_allocReadChannel', 23, '...pulse_44100sr_16bit_octo.wav', 0, -1, 3, 4)

    """

    ### CLASS VARIABLES ###

    request_id = RequestId.BUFFER_ALLOCATE_READ_CHANNEL

    ### INITIALIZER ###

    def __init__(
        self,
        buffer_id=None,
        channel_indices=None,
        callback=None,
        file_path=None,
        frame_count=None,
        starting_frame=None,
    ):
        BufferAllocateReadRequest.__init__(
            self,
            buffer_id=buffer_id,
            callback=callback,
            file_path=file_path,
            frame_count=frame_count,
            starting_frame=starting_frame,
        )
        if channel_indices is None:
            channel_indices = -1
        if not isinstance(channel_indices, collections.Sequence):
            channel_indices = (channel_indices,)
        channel_indices = tuple(int(_) for _ in channel_indices)
        if channel_indices != (-1,):
            assert all(0 <= _ for _ in channel_indices)
        self._channel_indices = channel_indices

    ### PUBLIC METHODS ###

    def to_osc(self, *, with_placeholders=False):
        contents = self._get_osc_message_contents()
        contents.extend(self.channel_indices)
        if self.callback:
            contents.append(self.callback.to_osc())
        message = supriya.osc.OscMessage(*contents)
        return message

    ### PUBLIC PROPERTIES ###

    @property
    def channel_indices(self):
        return self._channel_indices

    @property
    def response_patterns(self):
        return ["/done", "/b_allocReadChannel", self.buffer_id], None
