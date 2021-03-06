# flake8: noqa
"""
Tools for object-modeling OSC responses received from ``scsynth``.
"""
from .BufferAllocateReadChannelRequest import BufferAllocateReadChannelRequest
from .BufferAllocateReadRequest import BufferAllocateReadRequest
from .BufferAllocateRequest import BufferAllocateRequest
from .BufferCloseRequest import BufferCloseRequest
from .BufferCopyRequest import BufferCopyRequest
from .BufferFillRequest import BufferFillRequest
from .BufferFreeRequest import BufferFreeRequest
from .BufferGenerateRequest import BufferGenerateRequest
from .BufferGetContiguousRequest import BufferGetContiguousRequest
from .BufferGetRequest import BufferGetRequest
from .BufferInfoResponse import BufferInfoResponse
from .BufferNormalizeRequest import BufferNormalizeRequest
from .BufferQueryRequest import BufferQueryRequest
from .BufferReadChannelRequest import BufferReadChannelRequest
from .BufferReadRequest import BufferReadRequest
from .BufferSetContiguousRequest import BufferSetContiguousRequest
from .BufferSetContiguousResponse import BufferSetContiguousResponse
from .BufferSetRequest import BufferSetRequest
from .BufferSetResponse import BufferSetResponse
from .BufferWriteRequest import BufferWriteRequest
from .BufferZeroRequest import BufferZeroRequest
from .ClearScheduleRequest import ClearScheduleRequest
from .CommandRequest import CommandRequest
from .ControlBusFillRequest import ControlBusFillRequest
from .ControlBusGetContiguousRequest import ControlBusGetContiguousRequest
from .ControlBusGetRequest import ControlBusGetRequest
from .ControlBusSetContiguousRequest import ControlBusSetContiguousRequest
from .ControlBusSetContiguousResponse import ControlBusSetContiguousResponse
from .ControlBusSetRequest import ControlBusSetRequest
from .ControlBusSetResponse import ControlBusSetResponse
from .DoneResponse import DoneResponse
from .DumpOscRequest import DumpOscRequest
from .ErrorRequest import ErrorRequest
from .FailResponse import FailResponse
from .GroupDeepFreeRequest import GroupDeepFreeRequest
from .GroupDumpTreeRequest import GroupDumpTreeRequest
from .GroupFreeAllRequest import GroupFreeAllRequest
from .GroupHeadRequest import GroupHeadRequest
from .GroupNewRequest import GroupNewRequest
from .GroupQueryTreeRequest import GroupQueryTreeRequest
from .GroupTailRequest import GroupTailRequest
from .MoveRequest import MoveRequest
from .NodeAfterRequest import NodeAfterRequest
from .NodeBeforeRequest import NodeBeforeRequest
from .NodeCommandRequest import NodeCommandRequest
from .NodeFillRequest import NodeFillRequest
from .NodeFreeRequest import NodeFreeRequest
from .NodeInfoResponse import NodeInfoResponse
from .NodeMapToAudioBusContiguousRequest import NodeMapToAudioBusContiguousRequest
from .NodeMapToAudioBusRequest import NodeMapToAudioBusRequest
from .NodeMapToControlBusContiguousRequest import NodeMapToControlBusContiguousRequest
from .NodeMapToControlBusRequest import NodeMapToControlBusRequest
from .NodeOrderRequest import NodeOrderRequest
from .NodeQueryRequest import NodeQueryRequest
from .NodeRunRequest import NodeRunRequest
from .NodeSetContiguousRequest import NodeSetContiguousRequest
from .NodeSetContiguousResponse import NodeSetContiguousResponse
from .NodeSetRequest import NodeSetRequest
from .NodeSetResponse import NodeSetResponse
from .NodeTraceRequest import NodeTraceRequest
from .NothingRequest import NothingRequest
from .NotifyRequest import NotifyRequest
from .ParallelGroupNewRequest import ParallelGroupNewRequest
from .QueryTreeResponse import QueryTreeResponse
from .QuitRequest import QuitRequest
from .Request import Request
from .RequestBundle import RequestBundle
from .Requestable import Requestable
from .Response import Response
from .StatusRequest import StatusRequest
from .StatusResponse import StatusResponse
from .SyncRequest import SyncRequest
from .SyncedResponse import SyncedResponse
from .SynthDefFreeAllRequest import SynthDefFreeAllRequest
from .SynthDefFreeRequest import SynthDefFreeRequest
from .SynthDefLoadDirectoryRequest import SynthDefLoadDirectoryRequest
from .SynthDefLoadRequest import SynthDefLoadRequest
from .SynthDefReceiveRequest import SynthDefReceiveRequest
from .SynthDefRemovedResponse import SynthDefRemovedResponse
from .SynthGetContiguousRequest import SynthGetContiguousRequest
from .SynthGetRequest import SynthGetRequest
from .SynthNewRequest import SynthNewRequest
from .SynthNewargsRequest import SynthNewargsRequest
from .SynthNoidRequest import SynthNoidRequest
from .TriggerResponse import TriggerResponse
from .UgenCommandRequest import UgenCommandRequest

__all__ = [
    "BufferAllocateReadChannelRequest",
    "BufferAllocateReadRequest",
    "BufferAllocateRequest",
    "BufferCloseRequest",
    "BufferCopyRequest",
    "BufferFillRequest",
    "BufferFreeRequest",
    "BufferGenerateRequest",
    "BufferGetContiguousRequest",
    "BufferGetRequest",
    "BufferInfoResponse",
    "BufferNormalizeRequest",
    "BufferQueryRequest",
    "BufferReadChannelRequest",
    "BufferReadRequest",
    "BufferSetContiguousRequest",
    "BufferSetContiguousResponse",
    "BufferSetRequest",
    "BufferSetResponse",
    "BufferWriteRequest",
    "BufferZeroRequest",
    "ClearScheduleRequest",
    "CommandRequest",
    "ControlBusFillRequest",
    "ControlBusGetContiguousRequest",
    "ControlBusGetRequest",
    "ControlBusSetContiguousRequest",
    "ControlBusSetContiguousResponse",
    "ControlBusSetRequest",
    "ControlBusSetResponse",
    "DoneResponse",
    "DumpOscRequest",
    "ErrorRequest",
    "FailResponse",
    "GroupDeepFreeRequest",
    "GroupDumpTreeRequest",
    "GroupFreeAllRequest",
    "GroupHeadRequest",
    "GroupNewRequest",
    "GroupQueryTreeRequest",
    "GroupTailRequest",
    "MoveRequest",
    "NodeAfterRequest",
    "NodeBeforeRequest",
    "NodeCommandRequest",
    "NodeFillRequest",
    "NodeFreeRequest",
    "NodeInfoResponse",
    "NodeMapToAudioBusContiguousRequest",
    "NodeMapToAudioBusRequest",
    "NodeMapToControlBusContiguousRequest",
    "NodeMapToControlBusRequest",
    "NodeOrderRequest",
    "NodeQueryRequest",
    "NodeRunRequest",
    "NodeSetContiguousRequest",
    "NodeSetContiguousResponse",
    "NodeSetRequest",
    "NodeSetResponse",
    "NodeTraceRequest",
    "NothingRequest",
    "NotifyRequest",
    "ParallelGroupNewRequest",
    "QueryTreeResponse",
    "QuitRequest",
    "Request",
    "RequestBundle",
    "Requestable",
    "Response",
    "StatusRequest",
    "StatusResponse",
    "SyncRequest",
    "SyncedResponse",
    "SynthDefFreeAllRequest",
    "SynthDefFreeRequest",
    "SynthDefLoadDirectoryRequest",
    "SynthDefLoadRequest",
    "SynthDefReceiveRequest",
    "SynthDefRemovedResponse",
    "SynthGetContiguousRequest",
    "SynthGetRequest",
    "SynthNewRequest",
    "SynthNewargsRequest",
    "SynthNoidRequest",
    "TriggerResponse",
    "UgenCommandRequest",
]
