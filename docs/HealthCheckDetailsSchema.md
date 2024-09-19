# HealthCheckDetailsSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | [**StatusDatabase**](StatusDatabase.md) |  | 
**redis** | [**StatusRedis**](StatusRedis.md) |  | 
**uptime** | **str** |  | 

## Example

```python
from wallet_client.models.health_check_details_schema import HealthCheckDetailsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of HealthCheckDetailsSchema from a JSON string
health_check_details_schema_instance = HealthCheckDetailsSchema.from_json(json)
# print the JSON string representation of the object
print(HealthCheckDetailsSchema.to_json())

# convert the object into a dict
health_check_details_schema_dict = health_check_details_schema_instance.to_dict()
# create an instance of HealthCheckDetailsSchema from a dict
health_check_details_schema_from_dict = HealthCheckDetailsSchema.from_dict(health_check_details_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


