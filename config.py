import os


class Config:
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    uri = os.getenv("DATABASE_URL")  # or other relevant config var
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    # rest of connection code using the connection string `uri`


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
