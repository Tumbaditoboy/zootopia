import os
from flask_sqlalchemy import SQLAlchemy

# Aquí se inicializa la extensión de mysql sin conectarse todavía
db = SQLAlchemy()

def init_db(app):
    """Configura y vincula la base de datos con la aplicación Flask"""
    db_user = os.getenv('MYSQL_USER', 'zoo_user')
    db_password = os.getenv('MYSQL_PASSWORD', 'zoo_password')
    db_host = os.getenv('MYSQL_HOST', 'localhost')
    db_name = os.getenv('MYSQL_DB', 'zoologico_db')

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    return db