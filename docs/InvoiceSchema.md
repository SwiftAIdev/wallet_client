# InvoiceSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID счета | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** | Дата последнего обновления | [optional] 
**is_delete** | **bool** |  | [optional] [default to False]
**inn** | **str** |  | 
**email** | **str** |  | [optional] [default to '0']
**phone_number** | **str** |  | [optional] [default to 'RUB']

## Example

```python
from wallet_client.models.invoice_schema import InvoiceSchema

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceSchema from a JSON string
invoice_schema_instance = InvoiceSchema.from_json(json)
# print the JSON string representation of the object
print(InvoiceSchema.to_json())

# convert the object into a dict
invoice_schema_dict = invoice_schema_instance.to_dict()
# create an instance of InvoiceSchema from a dict
invoice_schema_from_dict = InvoiceSchema.from_dict(invoice_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


