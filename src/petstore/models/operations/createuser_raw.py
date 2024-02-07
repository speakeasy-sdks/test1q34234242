"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import user as shared_user
from typing import Optional


@dataclasses.dataclass
class CreateUserRawResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    body: Optional[bytes] = dataclasses.field(default=None)
    user: Optional[shared_user.User] = dataclasses.field(default=None)
    r"""successful operation"""
    

