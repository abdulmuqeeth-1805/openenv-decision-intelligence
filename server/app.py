from openenv.core.env_server import create_app
from ..models import MyAction, MyObservation
from .my_environment import MyEnvironment

app = create_app(MyEnvironment, MyAction, MyObservation, env_name="decision-intelligence-env")