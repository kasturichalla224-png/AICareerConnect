"""
Error Handlers
--------------
Centralised HTTP error handlers registered once on the app.
"""

from flask import render_template, jsonify, request


def register_error_handlers(app):
    """Attach error handlers to the Flask app."""

    @app.errorhandler(404)
    def not_found(error):
        if request.accept_mimetypes.best == "application/json":
            return jsonify({"error": "Resource not found."}), 404
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def internal_error(error):
        if request.accept_mimetypes.best == "application/json":
            return jsonify({"error": "Internal server error."}), 500
        return render_template("errors/500.html"), 500
