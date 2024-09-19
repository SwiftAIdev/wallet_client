# InvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID счета | [optional] 
**inn** | **str** |  | 
**kpp** | **str** |  | 
**email** | **str** |  | [optional] [default to '0']
**phone_number** | **str** |  | [optional] [default to 'RUB']
**name** | **str** |  | [optional] [default to '']

## Example

```python
from wallet_client.models.invoice_response import InvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceResponse from a JSON string
invoice_response_instance = InvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(InvoiceResponse.to_json())

# convert the object into a dict
invoice_response_dict = invoice_response_instance.to_dict()
# create an instance of InvoiceResponse from a dict
invoice_response_from_dict = InvoiceResponse.from_dict(invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


