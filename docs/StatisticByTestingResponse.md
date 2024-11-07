# StatisticByTestingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_testing** | **int** |  | 
**count_transactions** | **int** |  | 
**average_expense** | **float** |  | 
**average_expense_min** | **float** |  | 
**number_minutes** | **float** |  | 
**expense** | **float** |  | 
**predicted_expense** | **float** |  | 
**start_data** | **datetime** |  | 
**end_data** | **datetime** |  | 

## Example

```python
from wallet_client.models.statistic_by_testing_response import StatisticByTestingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticByTestingResponse from a JSON string
statistic_by_testing_response_instance = StatisticByTestingResponse.from_json(json)
# print the JSON string representation of the object
print(StatisticByTestingResponse.to_json())

# convert the object into a dict
statistic_by_testing_response_dict = statistic_by_testing_response_instance.to_dict()
# create an instance of StatisticByTestingResponse from a dict
statistic_by_testing_response_from_dict = StatisticByTestingResponse.from_dict(statistic_by_testing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


