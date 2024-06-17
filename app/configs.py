class DefaultConfig:
    DEBUG = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///vulnerablepython.db"


class DevelopmentConfig(DefaultConfig):
    DEBUG = True


class TestingConfig(DefaultConfig):
    DEBUG = True


class ProductionConfig(DefaultConfig):
    pass


config_dict = {
    "dev": DevelopmentConfig,
    "test": TestingConfig,
    "prod": ProductionConfig,
}
