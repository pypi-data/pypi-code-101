import json
from flask import Blueprint, jsonify, g, request

from pab.config import DEFAULTS_CONFIG_FILE
from pabui.api.utils import app_loaded_required

bp = Blueprint(
    "config",
    __name__,
    url_prefix="/config",
    template_folder="templates",
    static_folder="static",
)


@bp.route("/current", methods=("GET", ))
@app_loaded_required
def get():
	return jsonify(g.app.config.read())


@bp.route("/save", methods=("POST", ))
@app_loaded_required
def save():
    data = request.json
    if data:
        g.app.config.save(data)
        return jsonify(saved=True)
    return jsonify(saved=False)


@bp.route("/defaults", methods=("GET", ))
def defaults():
    if DEFAULTS_CONFIG_FILE.is_file():
        with DEFAULTS_CONFIG_FILE.open("r") as fp:
            return jsonify(json.load(fp))
    return jsonify({"error": "Unable to load defaults"})

