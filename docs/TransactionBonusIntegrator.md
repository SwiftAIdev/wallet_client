# TransactionBonusIntegrator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_user** | **str** |  | [optional] [default to '']
**amount** | **float** |  | [optional] [default to 0]

## Example

```python
from wallet_client.models.transaction_bonus_integrator import TransactionBonusIntegrator

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionBonusIntegrator from a JSON string
transaction_bonus_integrator_instance = TransactionBonusIntegrator.from_json(json)
# print the JSON string representation of the object
print(TransactionBonusIntegrator.to_json())

# convert the object into a dict
transaction_bonus_integrator_dict = transaction_bonus_integrator_instance.to_dict()
# create an instance of TransactionBonusIntegrator from a dict
transaction_bonus_integrator_from_dict = TransactionBonusIntegrator.from_dict(transaction_bonus_integrator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


