# UserWalletResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet** | [**WalletSchema**](WalletSchema.md) | Кошелек | [optional] 
**name** | **str** | name | [optional] 
**email** | **str** |  | [optional] 
**id** | **int** | email | [optional] 
**third_party_id** | **str** | third_party_id | [optional] 

## Example

```python
from wallet_client.models.user_wallet_response import UserWalletResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserWalletResponse from a JSON string
user_wallet_response_instance = UserWalletResponse.from_json(json)
# print the JSON string representation of the object
print(UserWalletResponse.to_json())

# convert the object into a dict
user_wallet_response_dict = user_wallet_response_instance.to_dict()
# create an instance of UserWalletResponse from a dict
user_wallet_response_from_dict = UserWalletResponse.from_dict(user_wallet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


