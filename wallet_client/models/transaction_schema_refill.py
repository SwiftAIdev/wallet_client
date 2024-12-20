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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from wallet_client.models.act_schema import ActSchema
from wallet_client.models.category_transaction_enum import CategoryTransactionEnum
from wallet_client.models.status_transaction_enum import StatusTransactionEnum
from wallet_client.models.transaction_create_refill import TransactionCreateRefill
from typing import Optional, Set
from typing_extensions import Self

class TransactionSchemaRefill(BaseModel):
    """
    TransactionSchemaRefill
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="ID транзакции")
    amount: Optional[Union[StrictFloat, StrictInt]] = 0
    var_date: Optional[datetime] = Field(default=None, alias="date")
    category: Optional[CategoryTransactionEnum] = None
    wallet_id: Optional[StrictInt] = None
    status: Optional[StatusTransactionEnum] = None
    data: Optional[TransactionCreateRefill] = None
    acts: Optional[List[ActSchema]] = None
    __properties: ClassVar[List[str]] = ["id", "amount", "date", "category", "wallet_id", "status", "data", "acts"]

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
        """Create an instance of TransactionSchemaRefill from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in acts (list)
        _items = []
        if self.acts:
            for _item_acts in self.acts:
                if _item_acts:
                    _items.append(_item_acts.to_dict())
            _dict['acts'] = _items
        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionSchemaRefill from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "amount": obj.get("amount") if obj.get("amount") is not None else 0,
            "date": obj.get("date"),
            "category": obj.get("category"),
            "wallet_id": obj.get("wallet_id"),
            "status": obj.get("status"),
            "data": TransactionCreateRefill.from_dict(obj["data"]) if obj.get("data") is not None else None,
            "acts": [ActSchema.from_dict(_item) for _item in obj["acts"]] if obj.get("acts") is not None else None
        })
        return _obj


