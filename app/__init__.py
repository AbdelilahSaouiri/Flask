from flask import Flask
from .config import Config
from .extensions import db, migrate
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialiser les extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Enregistrer les routes
    register_routes(app)

    return app
