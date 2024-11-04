# wallet_client.InvoiceApi

All URIs are relative to */wallet_service/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_create_invoice**](InvoiceApi.md#v1_create_invoice) | **POST** /v1/users/{user_id}/invoices | Users:Create Invoice
[**v1_get_invoice_by_id**](InvoiceApi.md#v1_get_invoice_by_id) | **GET** /v1/users/{user_id}/invoices/{invoice_id} | Users:Get Invoice By Id
[**v1_get_invoices**](InvoiceApi.md#v1_get_invoices) | **GET** /v1/users/{user_id}/invoices | Users:Get Invoices


# **v1_create_invoice**
> InvoiceResponse v1_create_invoice(user_id, invoice_create_response, x_request_id=x_request_id)

Users:Create Invoice

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.invoice_create_response import InvoiceCreateResponse
from wallet_client.models.invoice_response import InvoiceResponse
from wallet_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /wallet_service/api
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet_client.Configuration(
    host = "/wallet_service/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = wallet_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with wallet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet_client.InvoiceApi(api_client)
    user_id = 'user_id_example' # str | 
    invoice_create_response = wallet_client.InvoiceCreateResponse() # InvoiceCreateResponse | 
    x_request_id = '4bb1364c-a33a-49d9-aa65-5b982ec0f864' # str |  (optional) (default to '4bb1364c-a33a-49d9-aa65-5b982ec0f864')

    try:
        # Users:Create Invoice
        api_response = api_instance.v1_create_invoice(user_id, invoice_create_response, x_request_id=x_request_id)
        print("The response of InvoiceApi->v1_create_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->v1_create_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **invoice_create_response** | [**InvoiceCreateResponse**](InvoiceCreateResponse.md)|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;4bb1364c-a33a-49d9-aa65-5b982ec0f864&#39;]

### Return type

[**InvoiceResponse**](InvoiceResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**204** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_invoice_by_id**
> InvoiceResponse v1_get_invoice_by_id(user_id, invoice_id, x_request_id=x_request_id)

Users:Get Invoice By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.invoice_response import InvoiceResponse
from wallet_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /wallet_service/api
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet_client.Configuration(
    host = "/wallet_service/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = wallet_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with wallet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet_client.InvoiceApi(api_client)
    user_id = 'user_id_example' # str | 
    invoice_id = 56 # int | 
    x_request_id = '4bb1364c-a33a-49d9-aa65-5b982ec0f864' # str |  (optional) (default to '4bb1364c-a33a-49d9-aa65-5b982ec0f864')

    try:
        # Users:Get Invoice By Id
        api_response = api_instance.v1_get_invoice_by_id(user_id, invoice_id, x_request_id=x_request_id)
        print("The response of InvoiceApi->v1_get_invoice_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->v1_get_invoice_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **invoice_id** | **int**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;4bb1364c-a33a-49d9-aa65-5b982ec0f864&#39;]

### Return type

[**InvoiceResponse**](InvoiceResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

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
**204** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_invoices**
> PaginationRequestInvoiceResponse v1_get_invoices(user_id, page=page, size=size, x_request_id=x_request_id)

Users:Get Invoices

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.pagination_request_invoice_response import PaginationRequestInvoiceResponse
from wallet_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /wallet_service/api
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet_client.Configuration(
    host = "/wallet_service/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = wallet_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with wallet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet_client.InvoiceApi(api_client)
    user_id = 'user_id_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    size = 25 # int |  (optional) (default to 25)
    x_request_id = '4bb1364c-a33a-49d9-aa65-5b982ec0f864' # str |  (optional) (default to '4bb1364c-a33a-49d9-aa65-5b982ec0f864')

    try:
        # Users:Get Invoices
        api_response = api_instance.v1_get_invoices(user_id, page=page, size=size, x_request_id=x_request_id)
        print("The response of InvoiceApi->v1_get_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->v1_get_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **size** | **int**|  | [optional] [default to 25]
 **x_request_id** | **str**|  | [optional] [default to &#39;4bb1364c-a33a-49d9-aa65-5b982ec0f864&#39;]

### Return type

[**PaginationRequestInvoiceResponse**](PaginationRequestInvoiceResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

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
**204** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

