"""
Mistral AI Service
------------------
Encapsulates all communication with the Mistral API so that routes
never deal with raw HTTP calls or prompt engineering directly.
"""

import os
import json
from mistralai import Mistral


def _get_client():
    """Create a Mistral client using the configured API key."""
    api_key = os.environ.get("MISTRAL_API_KEY", "")
    if not api_key:
        raise RuntimeError("MISTRAL_API_KEY is not set in the environment.")
    return Mistral(api_key=api_key)


def get_career_advice(user_query: str) -> dict:
    """
    Send a career-related question to Mistral and parse the response.

    Args:
        user_query: The user's career question in plain text.

    Returns:
        dict with keys: response, career_field, confidence_score
    """
    client = _get_client()
    model = os.environ.get("MISTRAL_MODEL", "mistral-large-latest")

    system_prompt = (
        "You are an expert AI career counselor. Analyze the user's question "
        "and provide detailed, actionable career guidance. Include:\n"
        "1. Recommended career paths\n"
        "2. Required skills and qualifications\n"
        "3. Industry trends and job market outlook\n"
        "4. Actionable next steps\n\n"
        "Also return a JSON block at the end of your response in this format:\n"
        '{"career_field": "<primary field>", "confidence_score": <0.0-1.0>}'
    )

    chat_response = client.chat.complete(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query},
        ],
    )

    ai_text = chat_response.choices[0].message.content

    # Try to extract structured metadata from the response
    career_field = None
    confidence_score = None
    try:
        # Look for the last JSON object in the response
        json_start = ai_text.rfind("{")
        json_end = ai_text.rfind("}") + 1
        if json_start != -1 and json_end > json_start:
            meta = json.loads(ai_text[json_start:json_end])
            career_field = meta.get("career_field")
            confidence_score = meta.get("confidence_score")
    except (json.JSONDecodeError, ValueError):
        pass  # Metadata extraction is best-effort

    return {
        "response": ai_text,
        "career_field": career_field,
        "confidence_score": confidence_score,
    }
