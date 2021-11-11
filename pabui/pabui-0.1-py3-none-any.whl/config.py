import os

env = os.environ


class Config:
    # You can override any configuration in the file: /etc/data_integrations_info/config.toml
    ENV = env.get("FLASK_ENV", "production")
    DEBUG = ENV == "development"
    SECRET_KEY = "ChangeYourKeyInThe_Config.toml_File"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:pass@host/database"  # Modify this in the config.toml file
    SQLALCHEMY_TRACK_MODIFICATIONS = False


CONFIG = Config
