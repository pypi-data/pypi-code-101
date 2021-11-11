from pathlib import Path

from flask import Blueprint, current_app, g

from pabui.api.app import bp as app_bp
from pabui.api.config import bp as config_bp
from pabui.api.tasks import bp as tasks_bp
from pabui.api.strategies import bp as strategies_bp
from pabui.api.contracts import bp as contracts_bp

from pabui.lib.app import PAB


@current_app.before_request
def load_app():
    g.app = PAB(Path.cwd())


apis = Blueprint(
    "api",
    __name__,
    url_prefix="/api",
    template_folder="templates",
    static_folder="static",
)


apis.register_blueprint(app_bp)
apis.register_blueprint(config_bp)
apis.register_blueprint(tasks_bp)
apis.register_blueprint(strategies_bp)
apis.register_blueprint(contracts_bp)
