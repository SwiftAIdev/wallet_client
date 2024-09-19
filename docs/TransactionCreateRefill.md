# TransactionCreateRefill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** |  | 
**invoice_number** | **str** |  | [optional] [default to '']
**inn** | **str** |  | [optional] [default to '']
**phone** | **str** |  | [optional] [default to '']
**invoice_url** | **str** |  | 
**remains** | **float** |  | 
**act_url** | **str** |  | [optional] [default to '']

## Example

```python
from wallet_client.models.transaction_create_refill import TransactionCreateRefill

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCreateRefill from a JSON string
transaction_create_refill_instance = TransactionCreateRefill.from_json(json)
# print the JSON string representation of the object
print(TransactionCreateRefill.to_json())

# convert the object into a dict
transaction_create_refill_dict = transaction_create_refill_instance.to_dict()
# create an instance of TransactionCreateRefill from a dict
transaction_create_refill_from_dict = TransactionCreateRefill.from_dict(transaction_create_refill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


