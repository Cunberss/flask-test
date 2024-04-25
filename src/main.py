from flask import Flask
from src.routes.api import api_bp
from src.routes.app import app_bp


def build_app():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(api_bp)
    flask_app.register_blueprint(app_bp)
    return flask_app


flask_app = build_app()


if __name__ == '__main__':
    flask_app.run()