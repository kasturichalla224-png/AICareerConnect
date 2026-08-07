"""
Helper Utilities
----------------
Small reusable functions shared across the application.
"""

from datetime import datetime


def format_datetime(dt: datetime, fmt: str = "%Y-%m-%d %H:%M") -> str:
    """Format a datetime object into a human-readable string."""
    if dt is None:
        return ""
    return dt.strftime(fmt)


def truncate_text(text: str, max_length: int = 200) -> str:
    """Truncate text to *max_length* characters, appending '…' if cut."""
    if len(text) <= max_length:
        return text
    return text[: max_length - 1] + "…"
