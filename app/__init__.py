from flask import Flask
from flask_login import LoginManager, login_manager
from flask_bootstrap import Bootstrap5
from config import config_options
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
login.login_view = "auth.login"
login.session_protection = "strong"
login.login_message_category = "warning"
db = SQLAlchemy()
bootstrap = Bootstrap5()


def create_app(configuration):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_options[configuration])
    app.config.from_pyfile('config.py')

    db.init_app(app)
    login_manager.init_app(app)

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
