from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    mention: str
    uuid_mention: str
    role: str
    uuid_role: str
    token_type: str


class TokenPayload(BaseModel):
    uuid: Optional[str] = None
