# ExpenseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**amount** | **float** |  | 

## Example

```python
from wallet_client.models.expense_response import ExpenseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseResponse from a JSON string
expense_response_instance = ExpenseResponse.from_json(json)
# print the JSON string representation of the object
print(ExpenseResponse.to_json())

# convert the object into a dict
expense_response_dict = expense_response_instance.to_dict()
# create an instance of ExpenseResponse from a dict
expense_response_from_dict = ExpenseResponse.from_dict(expense_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


