from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Підключення маршрутів
    from app.routes import users, categories, records, currencies
    app.register_blueprint(users.bp)
    app.register_blueprint(categories.bp)
    app.register_blueprint(records.bp)
    app.register_blueprint(currencies.bp)

    return app