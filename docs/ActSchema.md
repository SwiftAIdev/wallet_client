# ActSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID настроек | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** | Дата последнего обновления | [optional] 
**status** | [**StatusTransactionEnum**](StatusTransactionEnum.md) |  | [optional] 
**amount** | **float** |  | [optional] [default to 0]

## Example

```python
from wallet_client.models.act_schema import ActSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ActSchema from a JSON string
act_schema_instance = ActSchema.from_json(json)
# print the JSON string representation of the object
print(ActSchema.to_json())

# convert the object into a dict
act_schema_dict = act_schema_instance.to_dict()
# create an instance of ActSchema from a dict
act_schema_from_dict = ActSchema.from_dict(act_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


