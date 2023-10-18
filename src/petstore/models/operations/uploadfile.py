"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiresponse as shared_apiresponse
from typing import Optional


@dataclasses.dataclass
class UploadFileRequest:
    pet_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'petId', 'style': 'simple', 'explode': False }})
    r"""ID of pet to update"""
    additional_metadata: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'additionalMetadata', 'style': 'form', 'explode': True }})
    r"""Additional Metadata"""
    request_body: Optional[bytes] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/octet-stream' }})
    



@dataclasses.dataclass
class UploadFileResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_response: Optional[shared_apiresponse.APIResponse] = dataclasses.field(default=None)
    r"""successful operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
