# ServiceErrorPydantic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**type** | [**TypeErrorEnum**](TypeErrorEnum.md) |  | 
**translate_path** | **str** |  | 
**details** | **str** |  | 

## Example

```python
from wallet_client.models.service_error_pydantic import ServiceErrorPydantic

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceErrorPydantic from a JSON string
service_error_pydantic_instance = ServiceErrorPydantic.from_json(json)
# print the JSON string representation of the object
print(ServiceErrorPydantic.to_json())

# convert the object into a dict
service_error_pydantic_dict = service_error_pydantic_instance.to_dict()
# create an instance of ServiceErrorPydantic from a dict
service_error_pydantic_from_dict = ServiceErrorPydantic.from_dict(service_error_pydantic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


