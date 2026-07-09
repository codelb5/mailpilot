"""
OAuth Session Service.
"""

from src.models.auth import OAuthSession


class OAuthSessionStore:
    """
    Manages OAuth sessions.

    Current implementation:
        In-memory dictionary.

    Future:
        Redis
        MongoDB
    """

    _sessions: dict[str, OAuthSession] = {}

    def save(self, session: OAuthSession) -> None:

        self._sessions[session.state] = session

    def create(self, state: str, code_verifier: str) -> OAuthSession:

        session = OAuthSession.create(
            state=state,
            code_verifier=code_verifier,
        )

        self.save(session)

        return session

    def get(self, state: str) -> OAuthSession:

        session = self._sessions.get(state)

        if session is None:
            raise ValueError("OAuth session not found.")

        if session.expired:

            del self._sessions[state]

            raise ValueError("OAuth session expired.")

        return session

    def delete(self, state: str) -> None:

        self._sessions.pop(state, None)

    def clear_expired(self):

        expired = [
            state for state, session in self._sessions.items() if session.expired
        ]

        for state in expired:
            del self._sessions[state]
