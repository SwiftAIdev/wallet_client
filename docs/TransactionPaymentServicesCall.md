# TransactionPaymentServicesCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_transaction_integrator** | **str** |  | [optional] [default to '']
**duration** | **int** |  | [optional] [default to 0]
**price_second** | **float** |  | [optional] [default to 0]
**text_call** | **str** |  | [optional] [default to '']

## Example

```python
from wallet_client.models.transaction_payment_services_call import TransactionPaymentServicesCall

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPaymentServicesCall from a JSON string
transaction_payment_services_call_instance = TransactionPaymentServicesCall.from_json(json)
# print the JSON string representation of the object
print(TransactionPaymentServicesCall.to_json())

# convert the object into a dict
transaction_payment_services_call_dict = transaction_payment_services_call_instance.to_dict()
# create an instance of TransactionPaymentServicesCall from a dict
transaction_payment_services_call_from_dict = TransactionPaymentServicesCall.from_dict(transaction_payment_services_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


