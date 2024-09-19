# TransactionSchemaCreateIncome


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | 
**invoice_id** | **int** |  | 

## Example

```python
from wallet_client.models.transaction_schema_create_income import TransactionSchemaCreateIncome

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSchemaCreateIncome from a JSON string
transaction_schema_create_income_instance = TransactionSchemaCreateIncome.from_json(json)
# print the JSON string representation of the object
print(TransactionSchemaCreateIncome.to_json())

# convert the object into a dict
transaction_schema_create_income_dict = transaction_schema_create_income_instance.to_dict()
# create an instance of TransactionSchemaCreateIncome from a dict
transaction_schema_create_income_from_dict = TransactionSchemaCreateIncome.from_dict(transaction_schema_create_income_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


