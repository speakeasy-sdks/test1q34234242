"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import order as shared_order
from typing import Optional


@dataclasses.dataclass
class GetOrderByIDRequest:
    order_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'orderId', 'style': 'simple', 'explode': False }})
    r"""ID of order that needs to be fetched"""
    



@dataclasses.dataclass
class GetOrderByIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    body: Optional[bytes] = dataclasses.field(default=None)
    order: Optional[shared_order.Order] = dataclasses.field(default=None)
    r"""successful operation"""
    

