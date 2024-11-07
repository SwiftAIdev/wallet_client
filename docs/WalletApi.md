# wallet_client.WalletApi

All URIs are relative to */wallet_service/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_create_wallet**](WalletApi.md#v1_create_wallet) | **POST** /v1/users/{user_id}/wallet | Users:Create Wallet
[**v1_end_wallet_testing**](WalletApi.md#v1_end_wallet_testing) | **POST** /v1/users/{user_id}/wallet/testing/end | Users:End Wallet Testing
[**v1_get_wallet**](WalletApi.md#v1_get_wallet) | **GET** /v1/users/{user_id}/wallet | Users:Get Wallet
[**v1_get_wallets**](WalletApi.md#v1_get_wallets) | **GET** /v1/users/wallets | Users:Get Wallets
[**v1_get_wallets_invited**](WalletApi.md#v1_get_wallets_invited) | **GET** /v1/users/{user_id}/invited/all | Users:Get Wallets Invited
[**v1_resume_wallet_testing**](WalletApi.md#v1_resume_wallet_testing) | **POST** /v1/users/{user_id}/wallet/testing/resume | Users:Resume Wallet Testing
[**v1_start_wallet_testing**](WalletApi.md#v1_start_wallet_testing) | **POST** /v1/users/{user_id}/wallet/testing/start | Users:Start Wallet Testing
[**v1_stop_wallet_testing**](WalletApi.md#v1_stop_wallet_testing) | **POST** /v1/users/{user_id}/wallet/testing/stop | Users:Stop Wallet Testing


# **v1_create_wallet**
> WalletSchema v1_create_wallet(user_id, x_request_id=x_request_id)

Users:Create Wallet

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.wallet_schema import WalletSchema
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
    api_instance = wallet_client.WalletApi(api_client)
    user_id = 'user_id_example' # str | 
    x_request_id = '7aec7dfc-f84a-4595-8d0d-8cf694721112' # str |  (optional) (default to '7aec7dfc-f84a-4595-8d0d-8cf694721112')

    try:
        # Users:Create Wallet
        api_response = api_instance.v1_create_wallet(user_id, x_request_id=x_request_id)
        print("The response of WalletApi->v1_create_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->v1_create_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;7aec7dfc-f84a-4595-8d0d-8cf694721112&#39;]

### Return type

[**WalletSchema**](WalletSchema.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **v1_end_wallet_testing**
> WalletSchema v1_end_wallet_testing(user_id, x_request_id=x_request_id)

Users:End Wallet Testing

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.wallet_schema import WalletSchema
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
    api_instance = wallet_client.WalletApi(api_client)
    user_id = 'user_id_example' # str | 
    x_request_id = '7aec7dfc-f84a-4595-8d0d-8cf694721112' # str |  (optional) (default to '7aec7dfc-f84a-4595-8d0d-8cf694721112')

    try:
        # Users:End Wallet Testing
        api_response = api_instance.v1_end_wallet_testing(user_id, x_request_id=x_request_id)
        print("The response of WalletApi->v1_end_wallet_testing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->v1_end_wallet_testing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;7aec7dfc-f84a-4595-8d0d-8cf694721112&#39;]

### Return type

[**WalletSchema**](WalletSchema.md)

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

# **v1_get_wallet**
> WalletSchema v1_get_wallet(user_id, x_request_id=x_request_id)

Users:Get Wallet

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.wallet_schema import WalletSchema
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
    api_instance = wallet_client.WalletApi(api_client)
    user_id = 'user_id_example' # str | 
    x_request_id = '7aec7dfc-f84a-4595-8d0d-8cf694721112' # str |  (optional) (default to '7aec7dfc-f84a-4595-8d0d-8cf694721112')

    try:
        # Users:Get Wallet
        api_response = api_instance.v1_get_wallet(user_id, x_request_id=x_request_id)
        print("The response of WalletApi->v1_get_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->v1_get_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;7aec7dfc-f84a-4595-8d0d-8cf694721112&#39;]

### Return type

[**WalletSchema**](WalletSchema.md)

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

# **v1_get_wallets**
> PaginationRequestWalletSchema v1_get_wallets(page=page, size=size, user_id=user_id, user_id__in=user_id__in, wallet_id__in=wallet_id__in, wallet_id=wallet_id, id=id, id__neq=id__neq, testing_end__gt=testing_end__gt, testing_end__lt=testing_end__lt, testing_end__isnull=testing_end__isnull, is_testing=is_testing, x_request_id=x_request_id)

Users:Get Wallets

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.pagination_request_wallet_schema import PaginationRequestWalletSchema
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
    api_instance = wallet_client.WalletApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    size = 25 # int |  (optional) (default to 25)
    user_id = 'user_id_example' # str |  (optional)
    user_id__in = 'user_id__in_example' # str |  (optional)
    wallet_id__in = 'wallet_id__in_example' # str |  (optional)
    wallet_id = 'wallet_id_example' # str |  (optional)
    id = 56 # int |  (optional)
    id__neq = 56 # int |  (optional)
    testing_end__gt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    testing_end__lt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    testing_end__isnull = True # bool |  (optional)
    is_testing = True # bool |  (optional)
    x_request_id = '7aec7dfc-f84a-4595-8d0d-8cf694721112' # str |  (optional) (default to '7aec7dfc-f84a-4595-8d0d-8cf694721112')

    try:
        # Users:Get Wallets
        api_response = api_instance.v1_get_wallets(page=page, size=size, user_id=user_id, user_id__in=user_id__in, wallet_id__in=wallet_id__in, wallet_id=wallet_id, id=id, id__neq=id__neq, testing_end__gt=testing_end__gt, testing_end__lt=testing_end__lt, testing_end__isnull=testing_end__isnull, is_testing=is_testing, x_request_id=x_request_id)
        print("The response of WalletApi->v1_get_wallets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->v1_get_wallets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **size** | **int**|  | [optional] [default to 25]
 **user_id** | **str**|  | [optional] 
 **user_id__in** | **str**|  | [optional] 
 **wallet_id__in** | **str**|  | [optional] 
 **wallet_id** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **id__neq** | **int**|  | [optional] 
 **testing_end__gt** | **datetime**|  | [optional] 
 **testing_end__lt** | **datetime**|  | [optional] 
 **testing_end__isnull** | **bool**|  | [optional] 
 **is_testing** | **bool**|  | [optional] 
 **x_request_id** | **str**|  | [optional] [default to &#39;7aec7dfc-f84a-4595-8d0d-8cf694721112&#39;]

### Return type

[**PaginationRequestWalletSchema**](PaginationRequestWalletSchema.md)

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

# **v1_get_wallets_invited**
> List[UserWalletResponse] v1_get_wallets_invited(user_id, x_request_id=x_request_id)

Users:Get Wallets Invited

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.user_wallet_response import UserWalletResponse
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
    api_instance = wallet_client.WalletApi(api_client)
    user_id = 'user_id_example' # str | 
    x_request_id = '7aec7dfc-f84a-4595-8d0d-8cf694721112' # str |  (optional) (default to '7aec7dfc-f84a-4595-8d0d-8cf694721112')

    try:
        # Users:Get Wallets Invited
        api_response = api_instance.v1_get_wallets_invited(user_id, x_request_id=x_request_id)
        print("The response of WalletApi->v1_get_wallets_invited:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->v1_get_wallets_invited: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;7aec7dfc-f84a-4595-8d0d-8cf694721112&#39;]

### Return type

[**List[UserWalletResponse]**](UserWalletResponse.md)

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

# **v1_resume_wallet_testing**
> WalletSchema v1_resume_wallet_testing(user_id, testing_schema, x_request_id=x_request_id)

Users:Resume Wallet Testing

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.testing_schema import TestingSchema
from wallet_client.models.wallet_schema import WalletSchema
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
    api_instance = wallet_client.WalletApi(api_client)
    user_id = 'user_id_example' # str | 
    testing_schema = wallet_client.TestingSchema() # TestingSchema | 
    x_request_id = '7aec7dfc-f84a-4595-8d0d-8cf694721112' # str |  (optional) (default to '7aec7dfc-f84a-4595-8d0d-8cf694721112')

    try:
        # Users:Resume Wallet Testing
        api_response = api_instance.v1_resume_wallet_testing(user_id, testing_schema, x_request_id=x_request_id)
        print("The response of WalletApi->v1_resume_wallet_testing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->v1_resume_wallet_testing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **testing_schema** | [**TestingSchema**](TestingSchema.md)|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;7aec7dfc-f84a-4595-8d0d-8cf694721112&#39;]

### Return type

[**WalletSchema**](WalletSchema.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **v1_start_wallet_testing**
> WalletSchema v1_start_wallet_testing(user_id, testing_schema, x_request_id=x_request_id)

Users:Start Wallet Testing

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.testing_schema import TestingSchema
from wallet_client.models.wallet_schema import WalletSchema
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
    api_instance = wallet_client.WalletApi(api_client)
    user_id = 'user_id_example' # str | 
    testing_schema = wallet_client.TestingSchema() # TestingSchema | 
    x_request_id = '7aec7dfc-f84a-4595-8d0d-8cf694721112' # str |  (optional) (default to '7aec7dfc-f84a-4595-8d0d-8cf694721112')

    try:
        # Users:Start Wallet Testing
        api_response = api_instance.v1_start_wallet_testing(user_id, testing_schema, x_request_id=x_request_id)
        print("The response of WalletApi->v1_start_wallet_testing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->v1_start_wallet_testing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **testing_schema** | [**TestingSchema**](TestingSchema.md)|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;7aec7dfc-f84a-4595-8d0d-8cf694721112&#39;]

### Return type

[**WalletSchema**](WalletSchema.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **v1_stop_wallet_testing**
> WalletSchema v1_stop_wallet_testing(user_id, x_request_id=x_request_id)

Users:Stop Wallet Testing

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.wallet_schema import WalletSchema
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
    api_instance = wallet_client.WalletApi(api_client)
    user_id = 'user_id_example' # str | 
    x_request_id = '7aec7dfc-f84a-4595-8d0d-8cf694721112' # str |  (optional) (default to '7aec7dfc-f84a-4595-8d0d-8cf694721112')

    try:
        # Users:Stop Wallet Testing
        api_response = api_instance.v1_stop_wallet_testing(user_id, x_request_id=x_request_id)
        print("The response of WalletApi->v1_stop_wallet_testing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->v1_stop_wallet_testing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;7aec7dfc-f84a-4595-8d0d-8cf694721112&#39;]

### Return type

[**WalletSchema**](WalletSchema.md)

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

