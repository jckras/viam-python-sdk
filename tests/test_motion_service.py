import pytest
from grpclib.testing import ChannelFor
from viam.components import ComponentType
from viam.proto.api.common import Pose, PoseInFrame
from viam.services.motion import MotionClient

from .mocks.services import MockMotionService

MOVE_RESPONSES = {
    'arm': True,
    'gantry': False
}
GET_POSE_RESPONSES = {
    'arm': PoseInFrame(
        reference_frame='arm',
        pose=Pose(
            x=1,
            y=2,
            z=3,
            o_x=2,
            o_y=3,
            o_z=4,
            theta=20
        )
    ),
    'gantry': PoseInFrame(
        reference_frame='gantry',
        pose=Pose(
            x=2,
            y=3,
            z=4,
            o_x=3,
            o_y=4,
            o_z=5,
            theta=21
        )
    )
}


@pytest.fixture(scope='function')
def service() -> MockMotionService:
    return MockMotionService(
        move_responses=MOVE_RESPONSES,
        get_pose_responses=GET_POSE_RESPONSES
    )


class TestClient:
    @pytest.mark.asyncio
    async def test_move(self, service: MockMotionService):
        async with ChannelFor([service]) as channel:
            client = MotionClient(channel)
            success = await client.move(
                ComponentType.ARM, 'arm', PoseInFrame(), [])
            assert success == MOVE_RESPONSES['arm']
            success = await client.move(ComponentType.GANTRY,
                                        'gantry', PoseInFrame(), [])
            assert success == MOVE_RESPONSES['gantry']

    @pytest.mark.asyncio
    async def test_get_pose(self, service: MockMotionService):
        async with ChannelFor([service]) as channel:
            client = MotionClient(channel)
            pose = await client.get_pose(ComponentType.ARM, 'arm', 'x')
            assert pose == GET_POSE_RESPONSES['arm']
            pose = await client.get_pose(ComponentType.GANTRY, 'gantry', 'y')
            assert pose == GET_POSE_RESPONSES['gantry']