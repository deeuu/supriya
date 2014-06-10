# -*- encoding: utf-8 -*-
from supriya.tools.responsetools.Response import Response


class CSetnResponse(Response):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_items',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        items=None,
        ):
        self._items = items

    ### PUBLIC PROPERTIES ###

    @property
    def items(self):
        return self._items