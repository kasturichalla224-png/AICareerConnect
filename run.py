"""
Application Entry Point
-----------------------
Bootstraps the Flask app using the application factory and starts the dev server.
"""

from app import create_app

app = create_app("development")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
