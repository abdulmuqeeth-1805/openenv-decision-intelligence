from pydantic import Field
from openenv.core.env_server.types import Action, Observation

class MyAction(Action):
    command: str = Field(..., description="Command to execute")
    parameters: dict = Field(default_factory=dict)

class MyObservation(Observation):
    result: str = Field(..., description="Result")
    success: bool = Field(..., description="Success status")