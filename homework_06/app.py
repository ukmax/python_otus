from flask import Flask
from homework_06.views.index import index_bp

app = Flask(__name__)
app.register_blueprint(index_bp)



