# PaginationRequestInvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**size** | **int** |  | 
**total** | **int** |  | 
**data** | [**List[InvoiceResponse]**](InvoiceResponse.md) |  | 

## Example

```python
from wallet_client.models.pagination_request_invoice_response import PaginationRequestInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationRequestInvoiceResponse from a JSON string
pagination_request_invoice_response_instance = PaginationRequestInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(PaginationRequestInvoiceResponse.to_json())

# convert the object into a dict
pagination_request_invoice_response_dict = pagination_request_invoice_response_instance.to_dict()
# create an instance of PaginationRequestInvoiceResponse from a dict
pagination_request_invoice_response_from_dict = PaginationRequestInvoiceResponse.from_dict(pagination_request_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


