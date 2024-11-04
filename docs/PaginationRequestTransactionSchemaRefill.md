# PaginationRequestTransactionSchemaRefill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**size** | **int** |  | 
**total** | **int** |  | 
**data** | [**List[TransactionSchemaRefill]**](TransactionSchemaRefill.md) |  | 

## Example

```python
from wallet_client.models.pagination_request_transaction_schema_refill import PaginationRequestTransactionSchemaRefill

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationRequestTransactionSchemaRefill from a JSON string
pagination_request_transaction_schema_refill_instance = PaginationRequestTransactionSchemaRefill.from_json(json)
# print the JSON string representation of the object
print(PaginationRequestTransactionSchemaRefill.to_json())

# convert the object into a dict
pagination_request_transaction_schema_refill_dict = pagination_request_transaction_schema_refill_instance.to_dict()
# create an instance of PaginationRequestTransactionSchemaRefill from a dict
pagination_request_transaction_schema_refill_from_dict = PaginationRequestTransactionSchemaRefill.from_dict(pagination_request_transaction_schema_refill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


