from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, init, upgrade, migrate

from routes import login_and_registration as lar
from routes import home_page as hp


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(hp.create_home_page_blueprint())
    app.register_blueprint(lar.create_login_and_registration_blueprint())

    return app


def create_db(app):
    sql_db = SQLAlchemy(app)

    return sql_db


def create_models(app, db):
    with app.app_context():
        db.create_all()
        db.session.commit()


def create_migrate(app, db):
    migration = Migrate(app, db)
    return migration


def initialize_migration(app):
    with app.app_context():
        init()


def db_migrate(app):
    with app.app_context():
        migrate()


def db_migrate_upgrade(app):
    with app.app_context():
        upgrade()




