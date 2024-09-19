# WalletSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID настроек | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** | Дата последнего обновления | [optional] 
**is_delete** | **bool** |  | [optional] [default to False]
**user_id** | **str** |  | 
**wallet_id** | **str** |  | 
**invoices** | [**List[InvoiceSchema]**](InvoiceSchema.md) |  | [optional] [default to []]
**is_testing** | **bool** |  | 
**testing_end** | **datetime** |  | [optional] 
**currency_code** | **str** |  | [optional] [default to 'RUB']
**balance** | **float** |  | [optional] [default to 0]
**expenses** | **float** |  | [optional] [default to 0]
**opening_balance** | **float** |  | [optional] [default to 0]

## Example

```python
from wallet_client.models.wallet_schema import WalletSchema

# TODO update the JSON string below
json = "{}"
# create an instance of WalletSchema from a JSON string
wallet_schema_instance = WalletSchema.from_json(json)
# print the JSON string representation of the object
print(WalletSchema.to_json())

# convert the object into a dict
wallet_schema_dict = wallet_schema_instance.to_dict()
# create an instance of WalletSchema from a dict
wallet_schema_from_dict = WalletSchema.from_dict(wallet_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


