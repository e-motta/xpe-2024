from flask import Blueprint, send_from_directory


frontend_route_blueprint = Blueprint("frontend", __name__, url_prefix="/frontend")


@frontend_route_blueprint.route("/", methods=["GET"])
def index():
    return send_from_directory("app/frontend/static", "index.html")
