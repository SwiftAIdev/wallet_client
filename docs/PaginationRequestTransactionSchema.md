# PaginationRequestTransactionSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**size** | **int** |  | 
**total** | **int** |  | 
**data** | [**List[TransactionSchema]**](TransactionSchema.md) |  | 

## Example

```python
from wallet_client.models.pagination_request_transaction_schema import PaginationRequestTransactionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationRequestTransactionSchema from a JSON string
pagination_request_transaction_schema_instance = PaginationRequestTransactionSchema.from_json(json)
# print the JSON string representation of the object
print(PaginationRequestTransactionSchema.to_json())

# convert the object into a dict
pagination_request_transaction_schema_dict = pagination_request_transaction_schema_instance.to_dict()
# create an instance of PaginationRequestTransactionSchema from a dict
pagination_request_transaction_schema_from_dict = PaginationRequestTransactionSchema.from_dict(pagination_request_transaction_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


