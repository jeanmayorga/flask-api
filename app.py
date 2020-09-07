"""Create an application instance."""
from flask.helpers import get_debug_flag

from project.app import create_app
from project.settings import DevConfig, ProdConfig

# CONFIG = DevConfig if get_debug_flag() else ProdConfig
CONFIG = DevConfig


app = create_app(CONFIG)
