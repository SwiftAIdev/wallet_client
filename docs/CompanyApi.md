# wallet_client.CompanyApi

All URIs are relative to */wallet_service/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_company_data_company_inn_info_get**](CompanyApi.md#get_company_data_company_inn_info_get) | **GET** /company/{inn}/info | Get Company Data


# **get_company_data_company_inn_info_get**
> CompanyData get_company_data_company_inn_info_get(inn, x_request_id=x_request_id)

Get Company Data

### Example


```python
import wallet_client
from wallet_client.models.company_data import CompanyData
from wallet_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /wallet_service/api
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet_client.Configuration(
    host = "/wallet_service/api"
)


# Enter a context with an instance of the API client
with wallet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet_client.CompanyApi(api_client)
    inn = 'inn_example' # str | 
    x_request_id = '4a063058-9c8c-4e5a-b7f5-f719ab6f4d99' # str |  (optional) (default to '4a063058-9c8c-4e5a-b7f5-f719ab6f4d99')

    try:
        # Get Company Data
        api_response = api_instance.get_company_data_company_inn_info_get(inn, x_request_id=x_request_id)
        print("The response of CompanyApi->get_company_data_company_inn_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->get_company_data_company_inn_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inn** | **str**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;4a063058-9c8c-4e5a-b7f5-f719ab6f4d99&#39;]

### Return type

[**CompanyData**](CompanyData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

