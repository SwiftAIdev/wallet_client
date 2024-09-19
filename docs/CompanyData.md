# CompanyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inn** | **str** |  | 
**short_name** | **str** |  | [optional] [default to '']
**full_name** | **str** |  | [optional] [default to '']
**kpp** | **str** |  | [optional] [default to '']
**address** | **str** |  | [optional] [default to '']

## Example

```python
from wallet_client.models.company_data import CompanyData

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyData from a JSON string
company_data_instance = CompanyData.from_json(json)
# print the JSON string representation of the object
print(CompanyData.to_json())

# convert the object into a dict
company_data_dict = company_data_instance.to_dict()
# create an instance of CompanyData from a dict
company_data_from_dict = CompanyData.from_dict(company_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


