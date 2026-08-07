"""
Database Models
---------------
All SQLAlchemy models live here. Each model maps to a SQLite table.
Keeping models in one file simplifies imports for a project of this scale.
"""

from datetime import datetime
from flask_login import UserMixin
from app import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    """Registered user of the platform."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    career_sessions = db.relationship("CareerSession", backref="user", lazy="dynamic")
    speech_logs = db.relationship("SpeechLog", backref="user", lazy="dynamic")

    def __repr__(self):
        return f"<User {self.username}>"


class CareerSession(db.Model):
    """A single career-guidance conversation with the AI."""

    __tablename__ = "career_sessions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    query_text = db.Column(db.Text, nullable=False)
    ai_response = db.Column(db.Text, nullable=False)
    career_field = db.Column(db.String(100))
    confidence_score = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<CareerSession {self.id}>"


class SpeechLog(db.Model):
    """Tracks speech-to-text / text-to-speech interactions for analytics."""

    __tablename__ = "speech_logs"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    input_type = db.Column(db.String(20))   # 'speech_to_text' | 'text_to_speech'
    input_text = db.Column(db.Text)
    output_text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<SpeechLog {self.id}>"


class DashboardMetric(db.Model):
    """Pre-computed or cached metrics shown on the dashboard."""

    __tablename__ = "dashboard_metrics"

    id = db.Column(db.Integer, primary_key=True)
    metric_name = db.Column(db.String(100), nullable=False)
    metric_value = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50))
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<DashboardMetric {self.metric_name}: {self.metric_value}>"
