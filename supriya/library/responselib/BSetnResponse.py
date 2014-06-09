# -*- encoding: utf-8 -*-
from supriya.library.responselib.ServerResponse import ServerResponse


class BSetnResponse(ServerResponse):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_buffer_number',
        '_items',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        items=None,
        buffer_number=None
        ):
        self._buffer_number = buffer_number
        self._items = items

    ### PUBLIC PROPERTIES ###

    @property
    def buffer_number(self):
        return self._buffer_number

    @property
    def items(self):
        return self._items