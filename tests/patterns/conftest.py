import re
import types

import pytest

from supriya.patterns import RealtimeEventPlayer
from supriya.realtime import BlockAllocator, NodeIdAllocator


@pytest.fixture
def pseudo_server():
    return types.SimpleNamespace(
        audio_bus_allocator=BlockAllocator(),
        control_bus_allocator=BlockAllocator(),
        node_id_allocator=NodeIdAllocator(),
    )


@pytest.helpers.register
def setup_pattern_send(pattern, iterations):
    events, iterator = [], iter(pattern)
    for i in range(iterations):
        event = next(iterator)
        events.append(event)
    try:
        event = iterator.send(True)
        events.append(event)
        events.extend(iterator)
    except StopIteration:
        pass
    return events


@pytest.helpers.register
def manual_incommunicado(pattern, timestamp=10):
    server = types.SimpleNamespace(
        audio_bus_allocator=BlockAllocator(),
        control_bus_allocator=BlockAllocator(),
        node_id_allocator=NodeIdAllocator(),
    )
    player = RealtimeEventPlayer(pattern, server=server)
    lists, deltas, delta = [], [], True
    while delta is not None:
        bundle, delta = player(timestamp, timestamp, communicate=False)
        if delta is not None:
            timestamp += delta
        lists.append(bundle.to_list())
        deltas.append(delta)
    return lists, deltas


@pytest.helpers.register
def get_objects_as_string(objects, replace_uuids=False):
    pattern = re.compile(r"\bUUID\('(.*)'\)")
    string = "\n".join(format(x) for x in objects)
    if replace_uuids:
        matches = []
        for match in pattern.findall(string):
            if match not in matches:
                matches.append(match)
        for i, match in enumerate(matches, 65):
            string = string.replace(match, chr(i))
    return string
