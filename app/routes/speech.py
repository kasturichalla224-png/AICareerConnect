"""
Speech Routes
-------------
REST endpoints for Speech-to-Text and Text-to-Speech operations.
"""

from flask import Blueprint, request, jsonify, send_file
from flask_login import login_required, current_user

from app import db
from app.models import SpeechLog
from app.services.speech_service import transcribe_audio, synthesize_speech

speech_bp = Blueprint("speech", __name__)


@speech_bp.route("/to-text", methods=["POST"])
@login_required
def speech_to_text():
    """
    Accept an audio file upload, transcribe it, log the result,
    and return the transcription as JSON.
    """
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided."}), 400

    audio_file = request.files["audio"]
    transcription = transcribe_audio(audio_file)

    # Log
    log = SpeechLog(
        user_id=current_user.id,
        input_type="speech_to_text",
        output_text=transcription,
    )
    db.session.add(log)
    db.session.commit()

    return jsonify({"transcription": transcription})


@speech_bp.route("/to-speech", methods=["POST"])
@login_required
def text_to_speech():
    """
    Accept text in JSON body, convert to speech audio file,
    log it, and return the audio file for playback.
    """
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "Text cannot be empty."}), 400

    audio_path = synthesize_speech(text)

    # Log
    log = SpeechLog(
        user_id=current_user.id,
        input_type="text_to_speech",
        input_text=text,
    )
    db.session.add(log)
    db.session.commit()

    return send_file(audio_path, mimetype="audio/mpeg")
