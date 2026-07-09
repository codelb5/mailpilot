from pydantic import BaseModel


class ErrorResponse(BaseModel):

    success: bool = False

    error: str

    error_code: str | None = None
