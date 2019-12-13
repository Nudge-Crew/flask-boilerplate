import logging
import os

class Config(object):
    DEBUG = os.getenv("ENVIRONMENT") == "DEV"
    HOST = os.getenv("FLASK_RUN_HOST")
    PORT = int(os.getenv("FLASK_RUN_PORT", "3000"))

    POSTGRES = {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": os.getenv("DB_PORT", "5432"),
        "user": os.getenv("DB_USER", "db"),
        "password": os.getenv("DB_PASSWORD", ""),
        "db": os.getenv("DB_NAME", "postgres")
    }

    # SQLALCHEMY_DATABASE_URI = "postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(db)s" % POSTGRES
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

