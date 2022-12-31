# schemas.py
# Schema for request body and response body
from typing import Type

from pydantic import BaseModel


class URLBase(BaseModel):
    target_url: Type[str] = str


class URL(URLBase):
    is_active: bool
    clicks: int

    class Config:
        orm_mode = True


class URLInfo(URL):
    url: str
    admin_url: str
