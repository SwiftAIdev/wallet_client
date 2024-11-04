# PaginationRequestWalletSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**size** | **int** |  | 
**total** | **int** |  | 
**data** | [**List[WalletSchema]**](WalletSchema.md) |  | 

## Example

```python
from wallet_client.models.pagination_request_wallet_schema import PaginationRequestWalletSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationRequestWalletSchema from a JSON string
pagination_request_wallet_schema_instance = PaginationRequestWalletSchema.from_json(json)
# print the JSON string representation of the object
print(PaginationRequestWalletSchema.to_json())

# convert the object into a dict
pagination_request_wallet_schema_dict = pagination_request_wallet_schema_instance.to_dict()
# create an instance of PaginationRequestWalletSchema from a dict
pagination_request_wallet_schema_from_dict = PaginationRequestWalletSchema.from_dict(pagination_request_wallet_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


