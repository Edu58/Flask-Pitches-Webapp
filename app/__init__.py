from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

login = LoginManager()
login.login_view = "auth.login"
login.session_protection = "strong"
login.login_message_category = "warning"
bootstrap = Bootstrap()


def create_app():
    app = Flask(__name__)

    login.init_app(app)

    bootstrap.init_app(app)

    from app.main import main
    app.register_blueprint(main)

    from app.auth import auth
    app.register_blueprint(auth, url_prefix="auth/")

    return app
