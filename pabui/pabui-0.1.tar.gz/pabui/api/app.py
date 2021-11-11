from flask import Blueprint, jsonify

from pathlib import Path

bp = Blueprint(
    "app",
    __name__,
    url_prefix="/app",
    template_folder="templates",
    static_folder="static",
)


@bp.route("/get", methods=("GET", ))
def get_directory():
    return jsonify(directory=str(Path.cwd()))