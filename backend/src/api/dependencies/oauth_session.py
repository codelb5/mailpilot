from src.auth.oauth_session_store import OAuthSessionStore


def get_oauth_session_store() -> OAuthSessionStore:
    return OAuthSessionStore()
