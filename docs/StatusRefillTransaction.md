# StatusRefillTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID транзакции | [optional] 
**category** | [**CategoryTransactionEnum**](CategoryTransactionEnum.md) |  | [optional] 
**status** | [**StatusTransactionEnum**](StatusTransactionEnum.md) |  | [optional] 
**status_tinkoff** | [**GetApiV1InvoiceInvoiceIdInfoResponse200Status**](GetApiV1InvoiceInvoiceIdInfoResponse200Status.md) |  | [optional] 

## Example

```python
from wallet_client.models.status_refill_transaction import StatusRefillTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of StatusRefillTransaction from a JSON string
status_refill_transaction_instance = StatusRefillTransaction.from_json(json)
# print the JSON string representation of the object
print(StatusRefillTransaction.to_json())

# convert the object into a dict
status_refill_transaction_dict = status_refill_transaction_instance.to_dict()
# create an instance of StatusRefillTransaction from a dict
status_refill_transaction_from_dict = StatusRefillTransaction.from_dict(status_refill_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


