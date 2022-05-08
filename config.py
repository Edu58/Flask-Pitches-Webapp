class Config:
    pass


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'default': DevConfig
}
