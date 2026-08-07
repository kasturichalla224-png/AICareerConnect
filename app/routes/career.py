"""
Career Routes
-------------
Endpoints for AI-powered career guidance using the Mistral API.
"""

from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user

from app import db
from app.models import CareerSession
from app.services.mistral_service import get_career_advice

career_bp = Blueprint("career", __name__)


@career_bp.route("/", methods=["GET"])
@login_required
def career_home():
    """Render the career guidance chat interface."""
    return render_template("career/chat.html")


@career_bp.route("/ask", methods=["POST"])
@login_required
def ask_career():
    """
    Accept a career question, call Mistral, persist the exchange,
    and return the AI response as JSON.
    """
    data = request.get_json()
    query_text = data.get("query", "")

    if not query_text:
        return jsonify({"error": "Query cannot be empty."}), 400

    # Call the Mistral AI service
    result = get_career_advice(query_text)

    # Persist to DB
    session = CareerSession(
        user_id=current_user.id,
        query_text=query_text,
        ai_response=result["response"],
        career_field=result.get("career_field"),
        confidence_score=result.get("confidence_score"),
    )
    db.session.add(session)
    db.session.commit()

    return jsonify(result)


@career_bp.route("/history", methods=["GET"])
@login_required
def career_history():
    """Return the current user's past career sessions."""
    sessions = (
        CareerSession.query
        .filter_by(user_id=current_user.id)
        .order_by(CareerSession.created_at.desc())
        .limit(50)
        .all()
    )
    return render_template("career/history.html", sessions=sessions)
