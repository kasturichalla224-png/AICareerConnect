"""
Application Factory
-------------------
Creates and configures the Flask application using the factory pattern.
This is the SINGLE place where all extensions, blueprints, and error
handlers are wired together — making the app testable and modular.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS

from config import config_by_name

# ── Extension Instances (initialized without app) ────────────────────
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app(config_name="development"):
    """
    Application factory.

    Args:
        config_name: One of 'development', 'testing', 'production'.

    Returns:
        A fully configured Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # ── Initialize Extensions ────────────────────────────────────────
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    CORS(app)

    # ── Register Blueprints ──────────────────────────────────────────
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.career import career_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.speech import speech_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(career_bp, url_prefix="/career")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(speech_bp, url_prefix="/speech")

    # ── Create DB Tables ─────────────────────────────────────────────
    with app.app_context():
        from app import models  # noqa: F401 — import so SQLAlchemy sees the models
        db.create_all()

    # ── Register Error Handlers ──────────────────────────────────────
    from app.utils.error_handlers import register_error_handlers
    register_error_handlers(app)

    return app
