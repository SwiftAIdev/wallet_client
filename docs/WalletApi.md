# wallet_client.WalletApi

All URIs are relative to */wallet_service/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_wallet_users_user_id_wallet_post**](WalletApi.md#create_wallet_users_user_id_wallet_post) | **POST** /users/{user_id}/wallet | Create Wallet
[**get_wallet_users_user_id_wallet_get**](WalletApi.md#get_wallet_users_user_id_wallet_get) | **GET** /users/{user_id}/wallet | Get Wallet
[**get_wallets_integrator_user_id_invited_all_get**](WalletApi.md#get_wallets_integrator_user_id_invited_all_get) | **GET** /integrator/{user_id}/invited/all | Get Wallets


# **create_wallet_users_user_id_wallet_post**
> WalletSchema create_wallet_users_user_id_wallet_post(user_id, x_request_id=x_request_id)

Create Wallet

### Example


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


# Enter a context with an instance of the API client
with wallet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet_client.WalletApi(api_client)
    user_id = 'user_id_example' # str | 
    x_request_id = 'f5f2132b-ef09-4106-8a5e-aaaaa403448f' # str |  (optional) (default to 'f5f2132b-ef09-4106-8a5e-aaaaa403448f')

    try:
        # Create Wallet
        api_response = api_instance.create_wallet_users_user_id_wallet_post(user_id, x_request_id=x_request_id)
        print("The response of WalletApi->create_wallet_users_user_id_wallet_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->create_wallet_users_user_id_wallet_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;f5f2132b-ef09-4106-8a5e-aaaaa403448f&#39;]

### Return type

[**WalletSchema**](WalletSchema.md)

### Authorization

No authorization required

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallet_users_user_id_wallet_get**
> WalletSchema get_wallet_users_user_id_wallet_get(user_id, x_request_id=x_request_id)

Get Wallet

### Example


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


# Enter a context with an instance of the API client
with wallet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet_client.WalletApi(api_client)
    user_id = 'user_id_example' # str | 
    x_request_id = 'f5f2132b-ef09-4106-8a5e-aaaaa403448f' # str |  (optional) (default to 'f5f2132b-ef09-4106-8a5e-aaaaa403448f')

    try:
        # Get Wallet
        api_response = api_instance.get_wallet_users_user_id_wallet_get(user_id, x_request_id=x_request_id)
        print("The response of WalletApi->get_wallet_users_user_id_wallet_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_wallet_users_user_id_wallet_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;f5f2132b-ef09-4106-8a5e-aaaaa403448f&#39;]

### Return type

[**WalletSchema**](WalletSchema.md)

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

# **get_wallets_integrator_user_id_invited_all_get**
> List[UserWalletResponse] get_wallets_integrator_user_id_invited_all_get(user_id, x_request_id=x_request_id)

Get Wallets

### Example


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


# Enter a context with an instance of the API client
with wallet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet_client.WalletApi(api_client)
    user_id = 'user_id_example' # str | 
    x_request_id = 'f5f2132b-ef09-4106-8a5e-aaaaa403448f' # str |  (optional) (default to 'f5f2132b-ef09-4106-8a5e-aaaaa403448f')

    try:
        # Get Wallets
        api_response = api_instance.get_wallets_integrator_user_id_invited_all_get(user_id, x_request_id=x_request_id)
        print("The response of WalletApi->get_wallets_integrator_user_id_invited_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_wallets_integrator_user_id_invited_all_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;f5f2132b-ef09-4106-8a5e-aaaaa403448f&#39;]

### Return type

[**List[UserWalletResponse]**](UserWalletResponse.md)

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

