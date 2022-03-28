from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def register_extensions(app):
    db.init_app(app)


def configure_database(app):
    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    from app.views import views
    app.register_blueprint(views)
    configure_database(app)
    return app
