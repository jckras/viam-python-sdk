import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ...... import proto
from ...... import proto

class ObjectManipulationServiceBase(abc.ABC):

    @abc.abstractmethod
    async def DoGrab(self, stream: 'grpclib.server.Stream[proto.api.service.objectmanipulation.v1.object_manipulation_pb2.DoGrabRequest, proto.api.service.objectmanipulation.v1.object_manipulation_pb2.DoGrabResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.service.objectmanipulation.v1.ObjectManipulationService/DoGrab': grpclib.const.Handler(self.DoGrab, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.objectmanipulation.v1.object_manipulation_pb2.DoGrabRequest, proto.api.service.objectmanipulation.v1.object_manipulation_pb2.DoGrabResponse)}

class ObjectManipulationServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.DoGrab = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.objectmanipulation.v1.ObjectManipulationService/DoGrab', proto.api.service.objectmanipulation.v1.object_manipulation_pb2.DoGrabRequest, proto.api.service.objectmanipulation.v1.object_manipulation_pb2.DoGrabResponse)