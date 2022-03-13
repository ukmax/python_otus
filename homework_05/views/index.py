from flask import (
    Blueprint,
    render_template,
)

index_bp = Blueprint("index_bp", __name__)


@index_bp.route("/", endpoint="index")
def get_about_view():
    return render_template("index.html")
