from flask import Flask
from flask_migrate import Migrate
from homework_06.views.index import index_bp
from homework_06.models.database import db

app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI="postgresql+pg8000://postgres:password@localhost/homework_06_db",
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

db.init_app(app)

migrate = Migrate(app, db)
app.register_blueprint(index_bp)



