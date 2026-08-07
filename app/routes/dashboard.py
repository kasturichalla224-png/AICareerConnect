"""
Dashboard Routes
----------------
Dynamic dashboard with real-time analytics served as JSON for Chart.js.
"""

from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from sqlalchemy import func

from app import db
from app.models import CareerSession, SpeechLog, DashboardMetric

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
@login_required
def overview():
    """Render the main dashboard page."""
    return render_template("dashboard/overview.html")


@dashboard_bp.route("/api/stats", methods=["GET"])
@login_required
def stats():
    """
    Return aggregated statistics for the current user.
    Consumed by Chart.js on the frontend.
    """
    total_sessions = CareerSession.query.filter_by(user_id=current_user.id).count()
    total_speech = SpeechLog.query.filter_by(user_id=current_user.id).count()

    # Career-field distribution
    field_data = (
        db.session.query(CareerSession.career_field, func.count(CareerSession.id))
        .filter_by(user_id=current_user.id)
        .group_by(CareerSession.career_field)
        .all()
    )

    return jsonify({
        "total_sessions": total_sessions,
        "total_speech_interactions": total_speech,
        "career_fields": {
            field: count for field, count in field_data if field
        },
    })


@dashboard_bp.route("/api/metrics", methods=["GET"])
@login_required
def metrics():
    """Return cached / pre-computed platform-wide metrics."""
    records = DashboardMetric.query.order_by(DashboardMetric.recorded_at.desc()).limit(20).all()
    return jsonify([
        {
            "name": m.metric_name,
            "value": m.metric_value,
            "category": m.category,
            "recorded_at": m.recorded_at.isoformat(),
        }
        for m in records
    ])
