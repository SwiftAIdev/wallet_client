# coding: utf-8

"""
    Wallet Service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wallet_client.models.category_transaction_enum import CategoryTransactionEnum
from wallet_client.models.get_api_v1_invoice_invoice_id_info_response200_status import GetApiV1InvoiceInvoiceIdInfoResponse200Status
from wallet_client.models.status_transaction_enum import StatusTransactionEnum
from typing import Optional, Set
from typing_extensions import Self

class StatusRefillTransaction(BaseModel):
    """
    StatusRefillTransaction
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="ID транзакции")
    category: Optional[CategoryTransactionEnum] = None
    status: Optional[StatusTransactionEnum] = None
    status_tinkoff: Optional[GetApiV1InvoiceInvoiceIdInfoResponse200Status] = None
    __properties: ClassVar[List[str]] = ["id", "category", "status", "status_tinkoff"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of StatusRefillTransaction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StatusRefillTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "category": obj.get("category"),
            "status": obj.get("status"),
            "status_tinkoff": obj.get("status_tinkoff")
        })
        return _obj


