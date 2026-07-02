"""
Application dependencies.
"""

from src.auth.google_oauth import GoogleOAuth


def get_google_oauth() -> GoogleOAuth:
    """
    Return a Google OAuth service instance.
    """
    return GoogleOAuth()
