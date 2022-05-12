import os


class Config:
    SECRET_KEY = "dskjyf5667UUGUvbaUGAUBUGYT8YGJB89Y8898989gbU8978t789G789T789"
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://ed:ed@localhost/pitches"
    UPLOADED_PHOTOS_DEST = 'app/static/photos'


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False
    # uri = os.getenv("DATABASE_URL")  # or other relevant config var
    # if uri.startswith("postgres://"):
    #     uri = uri.replace("postgres://", "postgresql://", 1)
    # # rest of connection code using the connection string `uri`
    # SQLALCHEMY_DATABASE_URI = uri


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'default': DevConfig
}
