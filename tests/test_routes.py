"""
Smoke tests — verify that core pages load and app initializes correctly.
"""


def test_index_loads(client):
    """Landing page should return 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_login_page_loads(client):
    """Login page should return 200."""
    response = client.get("/auth/login")
    assert response.status_code == 200


def test_register_page_loads(client):
    """Register page should return 200."""
    response = client.get("/auth/register")
    assert response.status_code == 200
