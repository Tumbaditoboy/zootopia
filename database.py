
import os
from urllib.parse import quote_plus
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

def init_db(app):
    """Configura y vincula la base de datos con Flask."""

    database_url = os.getenv("DATABASE_URL")

    if database_url:
        database_url = database_url.replace(
            "mysql://", "mysql+pymysql://", 1
        )
        app.config["SQLALCHEMY_DATABASE_URI"] = database_url

    else:
        db_user = os.getenv("MYSQL_USER", "zoo_user")
        db_password = os.getenv("MYSQL_PASSWORD", "zoo_password")
        db_host = os.getenv("MYSQL_HOST", "localhost")
        db_port = os.getenv(
            "MYSQL_PORT",
            "3306" if db_host == "db" else "3307"
        )
        db_name = os.getenv("MYSQL_DB", "zoologico_db")

        user = quote_plus(db_user)
        password = quote_plus(db_password)

        app.config["SQLALCHEMY_DATABASE_URI"] = (
            f"mysql+pymysql://{user}:{password}"
            f"@{db_host}:{db_port}/{db_name}"
        )

    engine_options = {
        "pool_pre_ping": True,
        "pool_recycle": 280
    }

    ssl_ca = os.getenv("MYSQL_SSL_CA")

    if ssl_ca:
        engine_options["connect_args"] = {
            "ssl": {"ca": ssl_ca}
        }

    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = engine_options

    db.init_app(app)
    return db
