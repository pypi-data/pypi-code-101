from flask import Blueprint, jsonify, g

from pabui.api.utils import app_loaded_required


bp = Blueprint(
    "contracts",
    __name__,
    url_prefix="/contracts",
    template_folder="templates",
    static_folder="static",
)


@bp.route("/get", methods=("GET", ))
@app_loaded_required
def get():
	return jsonify(g.app.contracts.get_contracts_data())