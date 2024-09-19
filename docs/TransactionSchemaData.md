# TransactionSchemaData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_transaction_integrator** | **str** |  | [optional] [default to '']
**duration** | **int** |  | [optional] [default to 0]
**price_second** | **float** |  | [optional] [default to 0]
**text_call** | **str** |  | [optional] [default to '']
**id_user** | **str** |  | [optional] [default to '']
**amount** | **float** |  | [optional] [default to 0]
**invoice_id** | **str** |  | 
**invoice_number** | **str** |  | [optional] [default to '']
**inn** | **str** |  | [optional] [default to '']
**phone** | **str** |  | [optional] [default to '']
**invoice_url** | **str** |  | 
**remains** | **float** |  | 
**act_url** | **str** |  | [optional] [default to '']

## Example

```python
from wallet_client.models.transaction_schema_data import TransactionSchemaData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSchemaData from a JSON string
transaction_schema_data_instance = TransactionSchemaData.from_json(json)
# print the JSON string representation of the object
print(TransactionSchemaData.to_json())

# convert the object into a dict
transaction_schema_data_dict = transaction_schema_data_instance.to_dict()
# create an instance of TransactionSchemaData from a dict
transaction_schema_data_from_dict = TransactionSchemaData.from_dict(transaction_schema_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


