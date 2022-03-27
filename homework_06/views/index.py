from flask import (Blueprint, render_template, request, redirect, url_for)
from homework_06.models.words import Words
from homework_06.models.database import db
from sqlalchemy.exc import DatabaseError
from werkzeug.exceptions import InternalServerError

index_bp = Blueprint("index_bp", __name__)


@index_bp.route("/", methods=["GET", "POST"], endpoint="index")
def get_index_view():
    if request.method == "GET":
        words = Words.query.all()
        return render_template("index.html", words=words)

    if request.method == "POST":
        english_word = request.form.get("english-word")
        russian_word = request.form.get("russian-word")

        word = Words(eng_word=english_word, rus_word=russian_word)
        db.session.add(word)
        try:
            db.session.commit()
        except DatabaseError:
            db.session.rollback()
            raise InternalServerError(f"Не удалось сохранить запись, произошла неизвестная ошибка")

        index_url = url_for("index_bp.index")
        return redirect(index_url)
