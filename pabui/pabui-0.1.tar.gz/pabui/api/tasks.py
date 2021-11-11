from flask import Blueprint, jsonify, g, request

from pabui.api.utils import app_loaded_required

bp = Blueprint(
    "tasks",
    __name__,
    url_prefix="/tasks",
    template_folder="templates",
    static_folder="static",
)


@bp.route("/get", methods=("GET", ))
@app_loaded_required
def get():
	return jsonify(g.app.tasks.read())


@bp.route("/save", methods=("POST", ))
@app_loaded_required
def save():
    data = request.json
    if data:
        g.app.tasks.save(data)
        return jsonify(saved=True)
    return jsonify(saved=False)

