from flask import Blueprint, request, send_from_directory

bp = Blueprint(
    "views",
    __name__,
    url_prefix="",
    template_folder="templates",
    static_folder="static",
)



@bp.route("/", defaults={"path": ""})
@bp.route("/<path:path>")
def index(path):
    """Route for index page."""
    return send_from_directory("templates", "index.html")


@bp.route("/staticd/<path:subpath>", strict_slashes=False)
def static_files(subpath):
    """ Route for static resources."""
    return send_from_directory("static", subpath)
