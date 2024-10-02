# wallet_client.InvoiceApi

All URIs are relative to */wallet_service/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invoice_users_user_id_invoices_post**](InvoiceApi.md#create_invoice_users_user_id_invoices_post) | **POST** /users/{user_id}/invoices | Create Invoice
[**get_invoice_users_user_id_invoices_invoice_id_get**](InvoiceApi.md#get_invoice_users_user_id_invoices_invoice_id_get) | **GET** /users/{user_id}/invoices/{invoice_id} | Get Invoice


# **create_invoice_users_user_id_invoices_post**
> InvoiceResponse create_invoice_users_user_id_invoices_post(user_id, invoice_create_response, x_request_id=x_request_id)

Create Invoice

### Example


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


# Enter a context with an instance of the API client
with wallet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet_client.InvoiceApi(api_client)
    user_id = 'user_id_example' # str | 
    invoice_create_response = wallet_client.InvoiceCreateResponse() # InvoiceCreateResponse | 
    x_request_id = '4a063058-9c8c-4e5a-b7f5-f719ab6f4d99' # str |  (optional) (default to '4a063058-9c8c-4e5a-b7f5-f719ab6f4d99')

    try:
        # Create Invoice
        api_response = api_instance.create_invoice_users_user_id_invoices_post(user_id, invoice_create_response, x_request_id=x_request_id)
        print("The response of InvoiceApi->create_invoice_users_user_id_invoices_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->create_invoice_users_user_id_invoices_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **invoice_create_response** | [**InvoiceCreateResponse**](InvoiceCreateResponse.md)|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;4a063058-9c8c-4e5a-b7f5-f719ab6f4d99&#39;]

### Return type

[**InvoiceResponse**](InvoiceResponse.md)

### Authorization

No authorization required

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_users_user_id_invoices_invoice_id_get**
> InvoiceResponse get_invoice_users_user_id_invoices_invoice_id_get(user_id, invoice_id, x_request_id=x_request_id)

Get Invoice

### Example


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


# Enter a context with an instance of the API client
with wallet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet_client.InvoiceApi(api_client)
    user_id = 'user_id_example' # str | 
    invoice_id = 56 # int | 
    x_request_id = '4a063058-9c8c-4e5a-b7f5-f719ab6f4d99' # str |  (optional) (default to '4a063058-9c8c-4e5a-b7f5-f719ab6f4d99')

    try:
        # Get Invoice
        api_response = api_instance.get_invoice_users_user_id_invoices_invoice_id_get(user_id, invoice_id, x_request_id=x_request_id)
        print("The response of InvoiceApi->get_invoice_users_user_id_invoices_invoice_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->get_invoice_users_user_id_invoices_invoice_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **invoice_id** | **int**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;4a063058-9c8c-4e5a-b7f5-f719ab6f4d99&#39;]

### Return type

[**InvoiceResponse**](InvoiceResponse.md)

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

