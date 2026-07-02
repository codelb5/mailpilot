from dataclasses import dataclass


@dataclass
class AuthorizationRequest:
    url: str
    state: str
    code_verifier: str
