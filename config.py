import os


class Config:
    UPLOADED_PHOTOS_DEST = 'app/static/photos'


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'default': DevConfig
}
