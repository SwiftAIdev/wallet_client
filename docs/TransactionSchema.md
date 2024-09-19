# TransactionSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID транзакции | [optional] 
**amount** | **float** |  | [optional] [default to 0]
**var_date** | **datetime** |  | [optional] 
**category** | [**CategoryTransactionEnum**](CategoryTransactionEnum.md) |  | [optional] 
**wallet_id** | **int** |  | [optional] 
**status** | [**StatusTransactionEnum**](StatusTransactionEnum.md) |  | [optional] 
**data** | [**TransactionSchemaData**](TransactionSchemaData.md) |  | [optional] 

## Example

```python
from wallet_client.models.transaction_schema import TransactionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSchema from a JSON string
transaction_schema_instance = TransactionSchema.from_json(json)
# print the JSON string representation of the object
print(TransactionSchema.to_json())

# convert the object into a dict
transaction_schema_dict = transaction_schema_instance.to_dict()
# create an instance of TransactionSchema from a dict
transaction_schema_from_dict = TransactionSchema.from_dict(transaction_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


