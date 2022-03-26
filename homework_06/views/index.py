from flask import (Blueprint, render_template, request, redirect, url_for)

index_bp = Blueprint("index_bp", __name__)

WORD_PAIRS = {
    "potato": "картофель",
    "cucumber": "огурец",
    "apple": "яблоко",
}


@index_bp.route("/", methods=["GET", "POST"], endpoint="index")
def get_index_view():
    if request.method == "GET":
        return render_template("index.html", products=list(WORD_PAIRS.items()))

    if request.method == "POST":
        english_word = request.form.get("english-word")
        russian_word = request.form.get("russian-word")

        WORD_PAIRS[english_word] = russian_word

        index_url = url_for("index_bp.index")
        return redirect(index_url)
