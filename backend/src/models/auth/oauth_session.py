"""
OAuth Session model.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from uuid import uuid4

    
@dataclass
class OAuthSession:
    """
    Represents an OAuth authentication session.
    """

    state: str

    code_verifier: str

    session_id: str

    created_at: datetime

    expires_at: datetime

    @classmethod
    def create(
        cls,
        state: str,
        code_verifier: str,
        expires_in_minutes: int = 10,
    ) -> "OAuthSession":

        now = datetime.utcnow()

        return cls(
            state=state,
            code_verifier=code_verifier,
            session_id=str(uuid4()),
            created_at=now,
            expires_at=now + timedelta(minutes=expires_in_minutes),
        )

    @property
    def expired(self) -> bool:
        return datetime.utcnow() > self.expires_at