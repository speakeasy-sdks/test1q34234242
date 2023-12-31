"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from petstore import utils
from typing import Optional

class Status(str, Enum):
    r"""Order Status"""
    PLACED = 'placed'
    APPROVED = 'approved'
    DELIVERED = 'delivered'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Order:
    complete: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('complete'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'complete' }})
    id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'id' }})
    pet_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('petId'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'petId' }})
    quantity: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'quantity' }})
    ship_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }, 'form': { 'field_name': 'shipDate' }})
    status: Optional[Status] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'status' }})
    r"""Order Status"""
    

