# TransactionChangeStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**StatusTransactionEnum**](StatusTransactionEnum.md) |  | [optional] 

## Example

```python
from wallet_client.models.transaction_change_status_request import TransactionChangeStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionChangeStatusRequest from a JSON string
transaction_change_status_request_instance = TransactionChangeStatusRequest.from_json(json)
# print the JSON string representation of the object
print(TransactionChangeStatusRequest.to_json())

# convert the object into a dict
transaction_change_status_request_dict = transaction_change_status_request_instance.to_dict()
# create an instance of TransactionChangeStatusRequest from a dict
transaction_change_status_request_from_dict = TransactionChangeStatusRequest.from_dict(transaction_change_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


