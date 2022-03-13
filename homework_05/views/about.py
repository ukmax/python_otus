from flask import (
    Blueprint,
    render_template,
)

about_bp = Blueprint("about_bp", __name__)


@about_bp.route("/about/", endpoint="about")
def get_about_view():
    return render_template("about.html")
