import os

from typing import Optional

from flask import Flask

from pabui.config import CONFIG


def create_app(test_config: Optional[dict] = None):
    app = Flask(__name__, instance_relative_config=True)

    with app.app_context():
        register_app(app, test_config)
        register_extensions(app)
        register_blueprints(app)
        register_commands(app)
    return app


def register_app(app, dconfig: Optional[dict]):
    app.config.from_object(CONFIG)
    if dconfig is not None:
        app.config.from_mapping(dconfig)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


def register_extensions(app):
    ...


def register_blueprints(app):
    from . import api
    from . import views
    
    app.register_blueprint(api.apis)
    app.register_blueprint(views.bp)


def register_commands(app):
    from . import commands


def run():
    import argparse
    parser = argparse.ArgumentParser("pabui")
    parser.add_argument("-p", "--port", default=5000, type=int)
    args = parser.parse_args()
    create_app().run(host="0.0.0.0", port=args.port)

if __name__ == "__main__":
    create_app().run(host="0.0.0.0")
