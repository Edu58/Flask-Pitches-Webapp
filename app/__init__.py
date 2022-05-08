from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5
from config import config_options
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bootstrap = Bootstrap5()


def create_app(configuration):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_options[configuration])
    app.config.from_pyfile('config.py')

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.session_protection = "strong"
    login_manager.login_message_category = "warning"

    bootstrap.init_app(app)

    from app.main import main
    app.register_blueprint(main)

    from app.auth import auth
    app.register_blueprint(auth, url_prefix="/auth/")

    from .models import Users

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    return app
