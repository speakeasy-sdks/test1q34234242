"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import user as shared_user
from typing import Optional


@dataclasses.dataclass
class UpdateUserJSONRequest:
    username: str = dataclasses.field(metadata={'path_param': { 'field_name': 'username', 'style': 'simple', 'explode': False }})
    r"""name that needs to be updated"""
    user: Optional[shared_user.User] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Update an existent user in the store"""
    



@dataclasses.dataclass
class UpdateUserJSONResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

