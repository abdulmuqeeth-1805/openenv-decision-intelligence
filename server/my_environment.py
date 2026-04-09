from openenv.core.env_server.interfaces import Environment
from openenv.core.env_server.types import State
from ..models import MyAction, MyObservation

class MyEnvironment(Environment):
    def __init__(self):
        self._state = State(episode_id="", step_count=0)

    def reset(self):
        return MyObservation(result="Ready", success=True)

    def step(self, action: MyAction):
        return MyObservation(result="Done", success=True)