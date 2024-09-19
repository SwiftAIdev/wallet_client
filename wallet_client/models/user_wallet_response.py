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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wallet_client.models.wallet_schema import WalletSchema
from typing import Optional, Set
from typing_extensions import Self

class UserWalletResponse(BaseModel):
    """
    UserWalletResponse
    """ # noqa: E501
    wallet: Optional[WalletSchema] = Field(default=None, description="Кошелек")
    name: Optional[StrictStr] = Field(default=None, description="name")
    email: Optional[StrictStr] = None
    id: Optional[StrictInt] = Field(default=None, description="email")
    third_party_id: Optional[StrictStr] = Field(default=None, description="third_party_id")
    __properties: ClassVar[List[str]] = ["wallet", "name", "email", "id", "third_party_id"]

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
        """Create an instance of UserWalletResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of wallet
        if self.wallet:
            _dict['wallet'] = self.wallet.to_dict()
        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserWalletResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "wallet": WalletSchema.from_dict(obj["wallet"]) if obj.get("wallet") is not None else None,
            "name": obj.get("name"),
            "email": obj.get("email"),
            "id": obj.get("id"),
            "third_party_id": obj.get("third_party_id")
        })
        return _obj


