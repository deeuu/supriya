from supriya.commands.MoveRequest import MoveRequest
from supriya.enums import RequestId


class NodeAfterRequest(MoveRequest):
    """
    An /n_after request.

    ::

        >>> import supriya
        >>> server = supriya.Server.default().boot()
        >>> group_a = supriya.Group([supriya.Group(), supriya.Group()])
        >>> group_b = supriya.Group([supriya.Group(), supriya.Group()])
        >>> synth_a = supriya.Synth()
        >>> synth_b = supriya.Synth()
        >>> server.default_group.extend([synth_a, synth_b, group_a, group_b])

    ::

        >>> print(server.query_remote_nodes())
        NODE TREE 0 group
            1 group
                1000 default
                1001 default
                1002 group
                    1003 group
                    1004 group
                1005 group
                    1006 group
                    1007 group

    ::

        >>> request = supriya.commands.NodeAfterRequest([
        ...     [synth_a, group_a[-1]],
        ...     [synth_b, group_b],
        ...     ])
        >>> request.to_osc()
        OscMessage('/n_after', 1000, 1004, 1001, 1005)

    ::

        >>> with server.osc_protocol.capture() as transcript:
        ...     request.communicate(server=server)
        ...     _ = server.sync()
        ...
        >>> for entry in transcript:
        ...     (entry.label, entry.message)
        ...
        ('S', OscMessage('/n_after', 1000, 1004, 1001, 1005))
        ('S', OscMessage('/sync', 0))
        ('R', OscMessage('/n_move', 1000, 1002, 1004, -1, 0))
        ('R', OscMessage('/n_move', 1001, 1, 1005, -1, 0))
        ('R', OscMessage('/synced', 0))

    ::

        >>> print(server.query_remote_nodes())
        NODE TREE 0 group
            1 group
                1002 group
                    1003 group
                    1004 group
                    1000 default
                1005 group
                    1006 group
                    1007 group
                1001 default

    ::

        >>> print(server.query_local_nodes())
        NODE TREE 0 group
            1 group
                1002 group
                    1003 group
                    1004 group
                    1000 default
                1005 group
                    1006 group
                    1007 group
                1001 default

    """

    ### CLASS VARIABLES ###

    _target_first = False

    request_id = RequestId.NODE_AFTER
