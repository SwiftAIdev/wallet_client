# wallet_client.TransactionApi

All URIs are relative to */wallet_service/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_change_status_transaction**](TransactionApi.md#v1_change_status_transaction) | **PUT** /v1/users/{user_id}/transactions/{transaction_id} | Users:Change Status Transaction
[**v1_close_acts**](TransactionApi.md#v1_close_acts) | **POST** /v1/users/close_acts | Users:Close Acts
[**v1_confirming_invoices**](TransactionApi.md#v1_confirming_invoices) | **GET** /v1/users/confirming_invoices | Users:Confirming Invoices
[**v1_end_old_transactions**](TransactionApi.md#v1_end_old_transactions) | **POST** /v1/users/end_old_transactions | Users:End Old Transactions
[**v1_get_expenses**](TransactionApi.md#v1_get_expenses) | **GET** /v1/users/{user_id}/expenses | Users:Get Expenses
[**v1_get_file_act_by_id**](TransactionApi.md#v1_get_file_act_by_id) | **GET** /v1/users/{user_id}/acts/{act_id}/file | Users:Get Act By Id:File
[**v1_get_file_invoice_by_id**](TransactionApi.md#v1_get_file_invoice_by_id) | **GET** /v1/users/{user_id}/invoice/{invoice_id}/file | Users:Get Invoice By Id:File
[**v1_get_refills**](TransactionApi.md#v1_get_refills) | **GET** /v1/users/{user_id}/refills | Users:Get Refills
[**v1_get_statistic_by_testing**](TransactionApi.md#v1_get_statistic_by_testing) | **GET** /v1/users/{user_id}/statistic/testing | Users:Get Statistic By Testing
[**v1_get_status_refill_transaction**](TransactionApi.md#v1_get_status_refill_transaction) | **GET** /v1/users/{user_id}/refills/{transaction_id}/status | Users:Get Status Refill Transaction
[**v1_get_transaction_by_id**](TransactionApi.md#v1_get_transaction_by_id) | **GET** /v1/users/{user_id}/transactions/{transaction_id} | Users:Get Transaction By Id
[**v1_get_transactions**](TransactionApi.md#v1_get_transactions) | **GET** /v1/users/{user_id}/transactions | Users:Get Transactions
[**v1_payment_transaction**](TransactionApi.md#v1_payment_transaction) | **POST** /v1/users/{user_id}/payment_transaction | Users:Payment Transaction
[**v1_refill_transaction**](TransactionApi.md#v1_refill_transaction) | **POST** /v1/users/{user_id}/refill_transaction | Users:Refill Transaction


# **v1_change_status_transaction**
> TransactionSchema v1_change_status_transaction(user_id, transaction_id, transaction_change_status_request, x_request_id=x_request_id)

Users:Change Status Transaction

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.transaction_change_status_request import TransactionChangeStatusRequest
from wallet_client.models.transaction_schema import TransactionSchema
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
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    transaction_id = 'transaction_id_example' # str | 
    transaction_change_status_request = wallet_client.TransactionChangeStatusRequest() # TransactionChangeStatusRequest | 
    x_request_id = '85f5bd03-8af0-4a0f-8fab-b596be01f315' # str |  (optional) (default to '85f5bd03-8af0-4a0f-8fab-b596be01f315')

    try:
        # Users:Change Status Transaction
        api_response = api_instance.v1_change_status_transaction(user_id, transaction_id, transaction_change_status_request, x_request_id=x_request_id)
        print("The response of TransactionApi->v1_change_status_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->v1_change_status_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **transaction_id** | **str**|  | 
 **transaction_change_status_request** | [**TransactionChangeStatusRequest**](TransactionChangeStatusRequest.md)|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;85f5bd03-8af0-4a0f-8fab-b596be01f315&#39;]

### Return type

[**TransactionSchema**](TransactionSchema.md)

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

# **v1_close_acts**
> bool v1_close_acts(x_request_id=x_request_id)

Users:Close Acts

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
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
    api_instance = wallet_client.TransactionApi(api_client)
    x_request_id = '85f5bd03-8af0-4a0f-8fab-b596be01f315' # str |  (optional) (default to '85f5bd03-8af0-4a0f-8fab-b596be01f315')

    try:
        # Users:Close Acts
        api_response = api_instance.v1_close_acts(x_request_id=x_request_id)
        print("The response of TransactionApi->v1_close_acts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->v1_close_acts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**|  | [optional] [default to &#39;85f5bd03-8af0-4a0f-8fab-b596be01f315&#39;]

### Return type

**bool**

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

# **v1_confirming_invoices**
> List[str] v1_confirming_invoices(x_request_id=x_request_id)

Users:Confirming Invoices

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
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
    api_instance = wallet_client.TransactionApi(api_client)
    x_request_id = '85f5bd03-8af0-4a0f-8fab-b596be01f315' # str |  (optional) (default to '85f5bd03-8af0-4a0f-8fab-b596be01f315')

    try:
        # Users:Confirming Invoices
        api_response = api_instance.v1_confirming_invoices(x_request_id=x_request_id)
        print("The response of TransactionApi->v1_confirming_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->v1_confirming_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**|  | [optional] [default to &#39;85f5bd03-8af0-4a0f-8fab-b596be01f315&#39;]

### Return type

**List[str]**

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

# **v1_end_old_transactions**
> PaginationRequestTransactionSchema v1_end_old_transactions(x_request_id=x_request_id)

Users:End Old Transactions

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.pagination_request_transaction_schema import PaginationRequestTransactionSchema
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
    api_instance = wallet_client.TransactionApi(api_client)
    x_request_id = '85f5bd03-8af0-4a0f-8fab-b596be01f315' # str |  (optional) (default to '85f5bd03-8af0-4a0f-8fab-b596be01f315')

    try:
        # Users:End Old Transactions
        api_response = api_instance.v1_end_old_transactions(x_request_id=x_request_id)
        print("The response of TransactionApi->v1_end_old_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->v1_end_old_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**|  | [optional] [default to &#39;85f5bd03-8af0-4a0f-8fab-b596be01f315&#39;]

### Return type

[**PaginationRequestTransactionSchema**](PaginationRequestTransactionSchema.md)

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

# **v1_get_expenses**
> ExpenseResponse v1_get_expenses(user_id, days=days, x_request_id=x_request_id)

Users:Get Expenses

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.expense_response import ExpenseResponse
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
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    days = 30 # int |  (optional) (default to 30)
    x_request_id = '85f5bd03-8af0-4a0f-8fab-b596be01f315' # str |  (optional) (default to '85f5bd03-8af0-4a0f-8fab-b596be01f315')

    try:
        # Users:Get Expenses
        api_response = api_instance.v1_get_expenses(user_id, days=days, x_request_id=x_request_id)
        print("The response of TransactionApi->v1_get_expenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->v1_get_expenses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **days** | **int**|  | [optional] [default to 30]
 **x_request_id** | **str**|  | [optional] [default to &#39;85f5bd03-8af0-4a0f-8fab-b596be01f315&#39;]

### Return type

[**ExpenseResponse**](ExpenseResponse.md)

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

# **v1_get_file_act_by_id**
> v1_get_file_act_by_id(user_id, act_id, x_request_id=x_request_id)

Users:Get Act By Id:File

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
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
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    act_id = 56 # int | 
    x_request_id = '85f5bd03-8af0-4a0f-8fab-b596be01f315' # str |  (optional) (default to '85f5bd03-8af0-4a0f-8fab-b596be01f315')

    try:
        # Users:Get Act By Id:File
        api_instance.v1_get_file_act_by_id(user_id, act_id, x_request_id=x_request_id)
    except Exception as e:
        print("Exception when calling TransactionApi->v1_get_file_act_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **act_id** | **int**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;85f5bd03-8af0-4a0f-8fab-b596be01f315&#39;]

### Return type

void (empty response body)

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

# **v1_get_file_invoice_by_id**
> v1_get_file_invoice_by_id(user_id, invoice_id, x_request_id=x_request_id)

Users:Get Invoice By Id:File

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
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
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    invoice_id = 56 # int | 
    x_request_id = '85f5bd03-8af0-4a0f-8fab-b596be01f315' # str |  (optional) (default to '85f5bd03-8af0-4a0f-8fab-b596be01f315')

    try:
        # Users:Get Invoice By Id:File
        api_instance.v1_get_file_invoice_by_id(user_id, invoice_id, x_request_id=x_request_id)
    except Exception as e:
        print("Exception when calling TransactionApi->v1_get_file_invoice_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **invoice_id** | **int**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;85f5bd03-8af0-4a0f-8fab-b596be01f315&#39;]

### Return type

void (empty response body)

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

# **v1_get_refills**
> PaginationRequestTransactionSchemaRefill v1_get_refills(user_id, page=page, size=size, x_request_id=x_request_id)

Users:Get Refills

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.pagination_request_transaction_schema_refill import PaginationRequestTransactionSchemaRefill
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
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    size = 25 # int |  (optional) (default to 25)
    x_request_id = '85f5bd03-8af0-4a0f-8fab-b596be01f315' # str |  (optional) (default to '85f5bd03-8af0-4a0f-8fab-b596be01f315')

    try:
        # Users:Get Refills
        api_response = api_instance.v1_get_refills(user_id, page=page, size=size, x_request_id=x_request_id)
        print("The response of TransactionApi->v1_get_refills:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->v1_get_refills: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **size** | **int**|  | [optional] [default to 25]
 **x_request_id** | **str**|  | [optional] [default to &#39;85f5bd03-8af0-4a0f-8fab-b596be01f315&#39;]

### Return type

[**PaginationRequestTransactionSchemaRefill**](PaginationRequestTransactionSchemaRefill.md)

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

# **v1_get_statistic_by_testing**
> StatisticByTestingResponse v1_get_statistic_by_testing(user_id, x_request_id=x_request_id)

Users:Get Statistic By Testing

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.statistic_by_testing_response import StatisticByTestingResponse
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
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    x_request_id = '85f5bd03-8af0-4a0f-8fab-b596be01f315' # str |  (optional) (default to '85f5bd03-8af0-4a0f-8fab-b596be01f315')

    try:
        # Users:Get Statistic By Testing
        api_response = api_instance.v1_get_statistic_by_testing(user_id, x_request_id=x_request_id)
        print("The response of TransactionApi->v1_get_statistic_by_testing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->v1_get_statistic_by_testing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;85f5bd03-8af0-4a0f-8fab-b596be01f315&#39;]

### Return type

[**StatisticByTestingResponse**](StatisticByTestingResponse.md)

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

# **v1_get_status_refill_transaction**
> StatusRefillTransaction v1_get_status_refill_transaction(user_id, transaction_id, x_request_id=x_request_id)

Users:Get Status Refill Transaction

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.status_refill_transaction import StatusRefillTransaction
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
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    transaction_id = 'transaction_id_example' # str | 
    x_request_id = '85f5bd03-8af0-4a0f-8fab-b596be01f315' # str |  (optional) (default to '85f5bd03-8af0-4a0f-8fab-b596be01f315')

    try:
        # Users:Get Status Refill Transaction
        api_response = api_instance.v1_get_status_refill_transaction(user_id, transaction_id, x_request_id=x_request_id)
        print("The response of TransactionApi->v1_get_status_refill_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->v1_get_status_refill_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **transaction_id** | **str**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;85f5bd03-8af0-4a0f-8fab-b596be01f315&#39;]

### Return type

[**StatusRefillTransaction**](StatusRefillTransaction.md)

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

# **v1_get_transaction_by_id**
> TransactionSchema v1_get_transaction_by_id(user_id, transaction_id, x_request_id=x_request_id)

Users:Get Transaction By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.transaction_schema import TransactionSchema
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
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    transaction_id = 'transaction_id_example' # str | 
    x_request_id = '85f5bd03-8af0-4a0f-8fab-b596be01f315' # str |  (optional) (default to '85f5bd03-8af0-4a0f-8fab-b596be01f315')

    try:
        # Users:Get Transaction By Id
        api_response = api_instance.v1_get_transaction_by_id(user_id, transaction_id, x_request_id=x_request_id)
        print("The response of TransactionApi->v1_get_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->v1_get_transaction_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **transaction_id** | **str**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;85f5bd03-8af0-4a0f-8fab-b596be01f315&#39;]

### Return type

[**TransactionSchema**](TransactionSchema.md)

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

# **v1_get_transactions**
> PaginationRequestTransactionSchema v1_get_transactions(user_id, page=page, size=size, x_request_id=x_request_id)

Users:Get Transactions

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.pagination_request_transaction_schema import PaginationRequestTransactionSchema
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
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    size = 25 # int |  (optional) (default to 25)
    x_request_id = '85f5bd03-8af0-4a0f-8fab-b596be01f315' # str |  (optional) (default to '85f5bd03-8af0-4a0f-8fab-b596be01f315')

    try:
        # Users:Get Transactions
        api_response = api_instance.v1_get_transactions(user_id, page=page, size=size, x_request_id=x_request_id)
        print("The response of TransactionApi->v1_get_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->v1_get_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **size** | **int**|  | [optional] [default to 25]
 **x_request_id** | **str**|  | [optional] [default to &#39;85f5bd03-8af0-4a0f-8fab-b596be01f315&#39;]

### Return type

[**PaginationRequestTransactionSchema**](PaginationRequestTransactionSchema.md)

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

# **v1_payment_transaction**
> TransactionSchema v1_payment_transaction(user_id, transaction_schema_create_payment_services, x_request_id=x_request_id)

Users:Payment Transaction

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.transaction_schema import TransactionSchema
from wallet_client.models.transaction_schema_create_payment_services import TransactionSchemaCreatePaymentServices
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
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    transaction_schema_create_payment_services = wallet_client.TransactionSchemaCreatePaymentServices() # TransactionSchemaCreatePaymentServices | 
    x_request_id = '85f5bd03-8af0-4a0f-8fab-b596be01f315' # str |  (optional) (default to '85f5bd03-8af0-4a0f-8fab-b596be01f315')

    try:
        # Users:Payment Transaction
        api_response = api_instance.v1_payment_transaction(user_id, transaction_schema_create_payment_services, x_request_id=x_request_id)
        print("The response of TransactionApi->v1_payment_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->v1_payment_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **transaction_schema_create_payment_services** | [**TransactionSchemaCreatePaymentServices**](TransactionSchemaCreatePaymentServices.md)|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;85f5bd03-8af0-4a0f-8fab-b596be01f315&#39;]

### Return type

[**TransactionSchema**](TransactionSchema.md)

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

# **v1_refill_transaction**
> TransactionSchema v1_refill_transaction(user_id, transaction_schema_create_income, x_request_id=x_request_id)

Users:Refill Transaction

### Example

* Bearer Authentication (HTTPBearer):

```python
import wallet_client
from wallet_client.models.transaction_schema import TransactionSchema
from wallet_client.models.transaction_schema_create_income import TransactionSchemaCreateIncome
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
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    transaction_schema_create_income = wallet_client.TransactionSchemaCreateIncome() # TransactionSchemaCreateIncome | 
    x_request_id = '85f5bd03-8af0-4a0f-8fab-b596be01f315' # str |  (optional) (default to '85f5bd03-8af0-4a0f-8fab-b596be01f315')

    try:
        # Users:Refill Transaction
        api_response = api_instance.v1_refill_transaction(user_id, transaction_schema_create_income, x_request_id=x_request_id)
        print("The response of TransactionApi->v1_refill_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->v1_refill_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **transaction_schema_create_income** | [**TransactionSchemaCreateIncome**](TransactionSchemaCreateIncome.md)|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;85f5bd03-8af0-4a0f-8fab-b596be01f315&#39;]

### Return type

[**TransactionSchema**](TransactionSchema.md)

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

