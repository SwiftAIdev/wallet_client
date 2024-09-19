# InvoiceCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inn** | **str** |  | 
**email** | **str** |  | [optional] [default to 'user@mail.ru']
**phone_number** | **str** |  | [optional] [default to '+79999999999']

## Example

```python
from wallet_client.models.invoice_create_response import InvoiceCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceCreateResponse from a JSON string
invoice_create_response_instance = InvoiceCreateResponse.from_json(json)
# print the JSON string representation of the object
print(InvoiceCreateResponse.to_json())

# convert the object into a dict
invoice_create_response_dict = invoice_create_response_instance.to_dict()
# create an instance of InvoiceCreateResponse from a dict
invoice_create_response_from_dict = InvoiceCreateResponse.from_dict(invoice_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


