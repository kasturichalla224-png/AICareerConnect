"""
Speech Service
--------------
Handles Speech-to-Text (via SpeechRecognition / Google Web API) and
Text-to-Speech (via gTTS) so that routes stay thin.
"""

import os
import uuid
import tempfile

import speech_recognition as sr
from gtts import gTTS
from flask import current_app


def transcribe_audio(audio_file) -> str:
    """
    Transcribe an uploaded audio file to text.

    Args:
        audio_file: A file-like object (from request.files).

    Returns:
        The transcribed text string.
    """
    recognizer = sr.Recognizer()

    # Save upload to a temporary WAV file
    temp_dir = current_app.config.get("SPEECH_TEMP_DIR", tempfile.gettempdir())
    os.makedirs(temp_dir, exist_ok=True)
    temp_path = os.path.join(temp_dir, f"{uuid.uuid4()}.wav")

    try:
        audio_file.save(temp_path)

        with sr.AudioFile(temp_path) as source:
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data)
        return text

    except sr.UnknownValueError:
        return "[Could not understand the audio]"
    except sr.RequestError as exc:
        return f"[Speech recognition service error: {exc}]"
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)


def synthesize_speech(text: str) -> str:
    """
    Convert text to an MP3 audio file using Google Text-to-Speech.

    Args:
        text: The text to speak.

    Returns:
        Absolute path to the generated MP3 file.
    """
    temp_dir = current_app.config.get("SPEECH_TEMP_DIR", tempfile.gettempdir())
    os.makedirs(temp_dir, exist_ok=True)
    output_path = os.path.join(temp_dir, f"{uuid.uuid4()}.mp3")

    tts = gTTS(text=text, lang="en")
    tts.save(output_path)

    return output_path
