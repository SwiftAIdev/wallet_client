# TransactionSchemaRefill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID транзакции | [optional] 
**amount** | **float** |  | [optional] [default to 0]
**var_date** | **datetime** |  | [optional] 
**category** | [**CategoryTransactionEnum**](CategoryTransactionEnum.md) |  | [optional] 
**wallet_id** | **int** |  | [optional] 
**status** | [**StatusTransactionEnum**](StatusTransactionEnum.md) |  | [optional] 
**data** | [**TransactionCreateRefill**](TransactionCreateRefill.md) |  | [optional] 
**acts** | [**List[ActSchema]**](ActSchema.md) |  | [optional] [default to []]

## Example

```python
from wallet_client.models.transaction_schema_refill import TransactionSchemaRefill

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSchemaRefill from a JSON string
transaction_schema_refill_instance = TransactionSchemaRefill.from_json(json)
# print the JSON string representation of the object
print(TransactionSchemaRefill.to_json())

# convert the object into a dict
transaction_schema_refill_dict = transaction_schema_refill_instance.to_dict()
# create an instance of TransactionSchemaRefill from a dict
transaction_schema_refill_from_dict = TransactionSchemaRefill.from_dict(transaction_schema_refill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


