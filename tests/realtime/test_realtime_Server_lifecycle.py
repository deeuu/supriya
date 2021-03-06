import time

import pytest
from uqbar.strings import normalize

import supriya
from supriya import exceptions, scsynth
from supriya.osc import OscMessage
from supriya.realtime import Server
from supriya.realtime.protocols import SyncProcessProtocol

pytestmark = pytest.mark.timeout(60)


def test_boot_and_quit():
    server = Server()
    assert not server.is_running
    assert not server.is_owner
    server.boot()
    assert server.is_running
    assert server.is_owner
    server.quit()
    assert not server.is_running
    assert not server.is_owner


def test_boot_and_boot():
    server = Server()
    assert not server.is_running
    assert not server.is_owner
    server.boot()
    assert server.is_running
    assert server.is_owner
    with pytest.raises(exceptions.ServerOnline):
        server.boot()
    assert server.is_running
    assert server.is_owner


def test_boot_and_quit_and_quit():
    server = Server()
    assert not server.is_running
    assert not server.is_owner
    server.boot()
    assert server.is_running
    assert server.is_owner
    server.quit()
    assert not server.is_running
    assert not server.is_owner
    server.quit()
    assert not server.is_running
    assert not server.is_owner


def test_boot_and_connect():
    server = Server()
    assert not server.is_running
    assert not server.is_owner
    server.boot()
    assert server.is_running
    assert server.is_owner
    with pytest.raises(exceptions.ServerOnline):
        server.connect()
    assert server.is_running
    assert server.is_owner


def test_boot_a_and_connect_b():
    server_a, server_b = Server(), Server()
    assert not server_a.is_running and not server_a.is_owner
    assert not server_b.is_running and not server_b.is_owner
    server_a.boot(maximum_logins=4)
    assert server_a.is_running and server_a.is_owner
    assert not server_b.is_running and not server_b.is_owner
    server_b.connect()
    assert server_a.is_running and server_a.is_owner
    assert server_b.is_running and not server_b.is_owner
    assert server_a.query_remote_nodes() == server_b.query_remote_nodes()
    assert server_a.client_id == 0 and server_b.client_id == 1
    assert server_a.default_group.node_id == 1 and server_b.default_group.node_id == 2
    group = supriya.Group()
    group.allocate(target_node=server_a)
    assert server_a.root_node[0][0] is group
    server_b.sync()
    assert server_b.root_node[0][0] is not group
    assert server_a.query_remote_nodes() == server_b.query_remote_nodes()


def test_boot_a_and_boot_b_cannot_boot():
    server_a, server_b = Server(), Server()
    assert not server_a.is_running and not server_a.is_owner
    assert not server_b.is_running and not server_b.is_owner
    server_a.boot(maximum_logins=4)
    assert server_a.is_running and server_a.is_owner
    assert not server_b.is_running and not server_b.is_owner
    with pytest.raises(exceptions.ServerCannotBoot):
        server_b.boot(maximum_logins=4)
    assert server_a.is_running and server_a.is_owner
    assert not server_b.is_running and not server_b.is_owner


def test_boot_a_and_connect_b_too_many_clients():
    server_a, server_b = Server(), Server()
    assert not server_a.is_running and not server_a.is_owner
    assert not server_b.is_running and not server_b.is_owner
    server_a.boot(maximum_logins=1)
    assert server_a.is_running and server_a.is_owner
    assert not server_b.is_running and not server_b.is_owner
    with pytest.raises(exceptions.TooManyClients):
        server_b.connect()
    assert server_a.is_running and server_a.is_owner
    assert not server_b.is_running and not server_b.is_owner


def test_boot_a_and_connect_b_and_quit_a():
    server_a, server_b = Server(), Server()
    assert not server_a.is_running and not server_a.is_owner
    assert not server_b.is_running and not server_b.is_owner
    server_a.boot(maximum_logins=2)
    server_b.connect()
    assert server_a.is_running and server_a.is_owner
    assert server_b.is_running and not server_b.is_owner
    server_a.quit()
    assert not server_a.is_running and not server_a.is_owner
    for _ in range(45):
        time.sleep(1)
        if not server_b.is_running:
            break
    assert not server_b.is_running and not server_b.is_owner


def test_boot_a_and_connect_b_and_disconnect_b():
    server_a, server_b = Server(), Server()
    assert not server_a.is_running and not server_a.is_owner
    assert not server_b.is_running and not server_b.is_owner
    server_a.boot(maximum_logins=2)
    server_b.connect()
    assert server_a.is_running and server_a.is_owner
    assert server_b.is_running and not server_b.is_owner
    server_b.disconnect()
    assert server_a.is_running and server_a.is_owner
    assert not server_b.is_running and not server_b.is_owner


def test_boot_a_and_connect_b_and_disconnect_a():
    server_a, server_b = Server(), Server()
    assert not server_a.is_running and not server_a.is_owner
    assert not server_b.is_running and not server_b.is_owner
    server_a.boot(maximum_logins=2)
    server_b.connect()
    assert server_a.is_running and server_a.is_owner
    assert server_b.is_running and not server_b.is_owner
    with pytest.raises(exceptions.OwnedServerShutdown):
        server_a.disconnect()
    assert server_a.is_running and server_a.is_owner
    assert server_b.is_running and not server_b.is_owner


def test_boot_a_and_connect_b_and_quit_b():
    server_a, server_b = Server(), Server()
    assert not server_a.is_running and not server_a.is_owner
    assert not server_b.is_running and not server_b.is_owner
    server_a.boot(maximum_logins=2)
    server_b.connect()
    assert server_a.is_running and server_a.is_owner
    assert server_b.is_running and not server_b.is_owner
    with pytest.raises(exceptions.UnownedServerShutdown):
        server_b.quit()
    assert server_a.is_running and server_a.is_owner
    assert server_b.is_running and not server_b.is_owner


def test_boot_a_and_connect_b_and_force_quit_b():
    server_a, server_b = Server(), Server()
    assert not server_a.is_running and not server_a.is_owner
    assert not server_b.is_running and not server_b.is_owner
    server_a.boot(maximum_logins=2)
    server_b.connect()
    assert server_a.is_running and server_a.is_owner
    assert server_b.is_running and not server_b.is_owner
    server_b.quit(force=True)
    assert not server_b.is_running and not server_b.is_owner
    for _ in range(45):
        time.sleep(1)
        if not server_a.is_running:
            break
    assert not server_a.is_running and not server_a.is_owner


def test_shared_resources():
    server_a, server_b = Server(), Server()
    server_a.boot(maximum_logins=2)
    server_b.connect()
    with supriya.SynthDefBuilder(frequency=440) as builder:
        _ = supriya.ugens.Out.ar(
            bus=0, source=supriya.ugens.SinOsc.ar(frequency=builder["frequency"])
        )
    synthdef = builder.build(name="foo")
    synth = supriya.Synth(synthdef=synthdef)
    transcript_a = server_a.osc_protocol.capture()
    transcript_b = server_b.osc_protocol.capture()
    with transcript_a, transcript_b:
        synth.allocate(target_node=server_b)
        time.sleep(0.1)  # Wait for all clients to receive /n_go
    assert synth not in server_a
    assert synth in server_b
    assert [
        (label, osc_message)
        for _, label, osc_message in transcript_a
        if osc_message.address not in ["/status", "/status.reply"]
    ] == [("R", OscMessage("/n_go", 67109864, 2, -1, -1, 0))]
    assert [
        (label, osc_message)
        for _, label, osc_message in transcript_b
        if osc_message.address not in ["/status", "/status.reply"]
    ] == [
        (
            "S",
            OscMessage(
                "/d_recv",
                synthdef.compile(),
                OscMessage("/s_new", "foo", 67109864, 0, 2),
            ),
        ),
        ("R", OscMessage("/n_go", 67109864, 2, -1, -1, 0)),
        ("R", OscMessage("/done", "/d_recv")),
    ]
    # TODO: Server A doesn't actually know what this SynthDef should be.
    assert str(server_a.query_local_nodes(True)) == normalize(
        """
        NODE TREE 0 group
            1 group
            2 group
                67109864 default
                    amplitude: 0.1, frequency: 440.0, gate: 1.0, out: 0.0, pan: 0.5
    """
    )
    assert str(server_b.query_local_nodes(True)) == normalize(
        """
        NODE TREE 0 group
            1 group
            2 group
                67109864 foo
                    frequency: 440.0
    """
    )


def test_connect_and_reconnect():
    try:
        options = scsynth.Options(maximum_logins=4)
        protocol = SyncProcessProtocol()
        protocol.boot(options, scsynth.find(), 57110)
        server = Server()
        server.connect(port=57110)
        assert server.is_running and not server.is_owner
        assert server.client_id == 0
        assert str(server.query_local_nodes(True)) == normalize(
            """
            NODE TREE 0 group
                1 group
                2 group
                3 group
                4 group
        """
        )
        server.disconnect()
        server.connect(port=57110)
        assert server.is_running and not server.is_owner
        assert server.client_id == 1
        assert str(server.query_local_nodes(True)) == normalize(
            """
            NODE TREE 0 group
                1 group
                2 group
                3 group
                4 group
        """
        )
    finally:
        protocol.quit()
