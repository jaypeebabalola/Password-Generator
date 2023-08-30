from flask import Flask
from app.routes import views

def create_app():
    app = Flask(__name__)
    app.register_blueprint(views)
    return app

from app import routes
    