from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_uploads import IMAGES, UploadSet, configure_uploads

db = SQLAlchemy()
bootstrap = Bootstrap5()
login_manager = LoginManager()
moment = Moment()
photos = UploadSet('photos', IMAGES)


def create_app(configuration):
    app = Flask(__name__)
    app.config.from_object(config_options[configuration])

    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.session_protection = "strong"
    login_manager.login_message_category = "warning"

    bootstrap.init_app(app)

    moment.init_app(app)

    configure_uploads(app, photos)

    from app.main import main
    app.register_blueprint(main)

    from app.auth import auth
    app.register_blueprint(auth, url_prefix="/auth/")

    return app
