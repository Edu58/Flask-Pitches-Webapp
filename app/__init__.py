from flask import Flask
# from flask_login import LoginManager
from flask_bootstrap import Bootstrap5
from config import config_options

# login = LoginManager()
# login.login_view = "auth.login"
# login.session_protection = "strong"
# login.login_message_category = "warning"
bootstrap = Bootstrap5()


def create_app(configuration):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_options[configuration])
    app.config.from_pyfile('config.py')

    # login.init_app(app)

    bootstrap.init_app(app)

    from app.main import main
    app.register_blueprint(main)

    from app.auth import auth
    app.register_blueprint(auth, url_prefix="auth/")

    return app
