# wallet_client.TransactionApi

All URIs are relative to */wallet_service/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_act_close_acts_get**](TransactionApi.md#close_act_close_acts_get) | **GET** /close_acts | Close Act
[**confirming_invoices_confirming_invoices_get**](TransactionApi.md#confirming_invoices_confirming_invoices_get) | **GET** /confirming_invoices | Confirming Invoices
[**get_act_file_users_user_id_acts_act_id_file_post**](TransactionApi.md#get_act_file_users_user_id_acts_act_id_file_post) | **POST** /users/{user_id}/acts/{act_id}/file | Get Act File
[**get_expenses_users_user_id_expenses_get**](TransactionApi.md#get_expenses_users_user_id_expenses_get) | **GET** /users/{user_id}/expenses | Get Expenses
[**get_invoice_file_users_user_id_invoice_invoice_id_file_post**](TransactionApi.md#get_invoice_file_users_user_id_invoice_invoice_id_file_post) | **POST** /users/{user_id}/invoice/{invoice_id}/file | Get Invoice File
[**get_refills_users_user_id_refills_get**](TransactionApi.md#get_refills_users_user_id_refills_get) | **GET** /users/{user_id}/refills | Get Refills
[**get_transaction_users_user_id_transactions_transaction_id_get**](TransactionApi.md#get_transaction_users_user_id_transactions_transaction_id_get) | **GET** /users/{user_id}/transactions/{transaction_id} | Get Transaction
[**get_transactions_users_user_id_transactions_get**](TransactionApi.md#get_transactions_users_user_id_transactions_get) | **GET** /users/{user_id}/transactions | Get Transactions
[**payment_transaction_users_user_id_payment_transaction_post**](TransactionApi.md#payment_transaction_users_user_id_payment_transaction_post) | **POST** /users/{user_id}/payment_transaction | Payment Transaction
[**refill_transaction_users_user_id_refill_transaction_post**](TransactionApi.md#refill_transaction_users_user_id_refill_transaction_post) | **POST** /users/{user_id}/refill_transaction | Refill Transaction
[**update_transaction_users_user_id_transactions_transaction_id_put**](TransactionApi.md#update_transaction_users_user_id_transactions_transaction_id_put) | **PUT** /users/{user_id}/transactions/{transaction_id} | Update Transaction


# **close_act_close_acts_get**
> bool close_act_close_acts_get(x_request_id=x_request_id)

Close Act

### Example


```python
import wallet_client
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
    api_instance = wallet_client.TransactionApi(api_client)
    x_request_id = 'f5f2132b-ef09-4106-8a5e-aaaaa403448f' # str |  (optional) (default to 'f5f2132b-ef09-4106-8a5e-aaaaa403448f')

    try:
        # Close Act
        api_response = api_instance.close_act_close_acts_get(x_request_id=x_request_id)
        print("The response of TransactionApi->close_act_close_acts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->close_act_close_acts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**|  | [optional] [default to &#39;f5f2132b-ef09-4106-8a5e-aaaaa403448f&#39;]

### Return type

**bool**

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

# **confirming_invoices_confirming_invoices_get**
> List[str] confirming_invoices_confirming_invoices_get(x_request_id=x_request_id)

Confirming Invoices

### Example


```python
import wallet_client
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
    api_instance = wallet_client.TransactionApi(api_client)
    x_request_id = 'f5f2132b-ef09-4106-8a5e-aaaaa403448f' # str |  (optional) (default to 'f5f2132b-ef09-4106-8a5e-aaaaa403448f')

    try:
        # Confirming Invoices
        api_response = api_instance.confirming_invoices_confirming_invoices_get(x_request_id=x_request_id)
        print("The response of TransactionApi->confirming_invoices_confirming_invoices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->confirming_invoices_confirming_invoices_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**|  | [optional] [default to &#39;f5f2132b-ef09-4106-8a5e-aaaaa403448f&#39;]

### Return type

**List[str]**

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

# **get_act_file_users_user_id_acts_act_id_file_post**
> get_act_file_users_user_id_acts_act_id_file_post(user_id, act_id, x_request_id=x_request_id)

Get Act File

### Example


```python
import wallet_client
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
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    act_id = 56 # int | 
    x_request_id = 'f5f2132b-ef09-4106-8a5e-aaaaa403448f' # str |  (optional) (default to 'f5f2132b-ef09-4106-8a5e-aaaaa403448f')

    try:
        # Get Act File
        api_instance.get_act_file_users_user_id_acts_act_id_file_post(user_id, act_id, x_request_id=x_request_id)
    except Exception as e:
        print("Exception when calling TransactionApi->get_act_file_users_user_id_acts_act_id_file_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **act_id** | **int**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;f5f2132b-ef09-4106-8a5e-aaaaa403448f&#39;]

### Return type

void (empty response body)

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

# **get_expenses_users_user_id_expenses_get**
> ExpenseResponse get_expenses_users_user_id_expenses_get(user_id, days=days, x_request_id=x_request_id)

Get Expenses

### Example


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


# Enter a context with an instance of the API client
with wallet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    days = 30 # int |  (optional) (default to 30)
    x_request_id = 'f5f2132b-ef09-4106-8a5e-aaaaa403448f' # str |  (optional) (default to 'f5f2132b-ef09-4106-8a5e-aaaaa403448f')

    try:
        # Get Expenses
        api_response = api_instance.get_expenses_users_user_id_expenses_get(user_id, days=days, x_request_id=x_request_id)
        print("The response of TransactionApi->get_expenses_users_user_id_expenses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->get_expenses_users_user_id_expenses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **days** | **int**|  | [optional] [default to 30]
 **x_request_id** | **str**|  | [optional] [default to &#39;f5f2132b-ef09-4106-8a5e-aaaaa403448f&#39;]

### Return type

[**ExpenseResponse**](ExpenseResponse.md)

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

# **get_invoice_file_users_user_id_invoice_invoice_id_file_post**
> get_invoice_file_users_user_id_invoice_invoice_id_file_post(user_id, invoice_id, x_request_id=x_request_id)

Get Invoice File

### Example


```python
import wallet_client
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
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    invoice_id = 56 # int | 
    x_request_id = 'f5f2132b-ef09-4106-8a5e-aaaaa403448f' # str |  (optional) (default to 'f5f2132b-ef09-4106-8a5e-aaaaa403448f')

    try:
        # Get Invoice File
        api_instance.get_invoice_file_users_user_id_invoice_invoice_id_file_post(user_id, invoice_id, x_request_id=x_request_id)
    except Exception as e:
        print("Exception when calling TransactionApi->get_invoice_file_users_user_id_invoice_invoice_id_file_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **invoice_id** | **int**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;f5f2132b-ef09-4106-8a5e-aaaaa403448f&#39;]

### Return type

void (empty response body)

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

# **get_refills_users_user_id_refills_get**
> PaginationRequest get_refills_users_user_id_refills_get(user_id, page=page, size=size, x_request_id=x_request_id)

Get Refills

### Example


```python
import wallet_client
from wallet_client.models.pagination_request import PaginationRequest
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
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    size = 25 # int |  (optional) (default to 25)
    x_request_id = 'f5f2132b-ef09-4106-8a5e-aaaaa403448f' # str |  (optional) (default to 'f5f2132b-ef09-4106-8a5e-aaaaa403448f')

    try:
        # Get Refills
        api_response = api_instance.get_refills_users_user_id_refills_get(user_id, page=page, size=size, x_request_id=x_request_id)
        print("The response of TransactionApi->get_refills_users_user_id_refills_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->get_refills_users_user_id_refills_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **size** | **int**|  | [optional] [default to 25]
 **x_request_id** | **str**|  | [optional] [default to &#39;f5f2132b-ef09-4106-8a5e-aaaaa403448f&#39;]

### Return type

[**PaginationRequest**](PaginationRequest.md)

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

# **get_transaction_users_user_id_transactions_transaction_id_get**
> TransactionSchema get_transaction_users_user_id_transactions_transaction_id_get(user_id, transaction_id, x_request_id=x_request_id)

Get Transaction

### Example


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


# Enter a context with an instance of the API client
with wallet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    transaction_id = 'transaction_id_example' # str | 
    x_request_id = 'f5f2132b-ef09-4106-8a5e-aaaaa403448f' # str |  (optional) (default to 'f5f2132b-ef09-4106-8a5e-aaaaa403448f')

    try:
        # Get Transaction
        api_response = api_instance.get_transaction_users_user_id_transactions_transaction_id_get(user_id, transaction_id, x_request_id=x_request_id)
        print("The response of TransactionApi->get_transaction_users_user_id_transactions_transaction_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->get_transaction_users_user_id_transactions_transaction_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **transaction_id** | **str**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;f5f2132b-ef09-4106-8a5e-aaaaa403448f&#39;]

### Return type

[**TransactionSchema**](TransactionSchema.md)

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

# **get_transactions_users_user_id_transactions_get**
> PaginationRequestTransactionSchema get_transactions_users_user_id_transactions_get(user_id, page=page, size=size, x_request_id=x_request_id)

Get Transactions

### Example


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


# Enter a context with an instance of the API client
with wallet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    size = 25 # int |  (optional) (default to 25)
    x_request_id = 'f5f2132b-ef09-4106-8a5e-aaaaa403448f' # str |  (optional) (default to 'f5f2132b-ef09-4106-8a5e-aaaaa403448f')

    try:
        # Get Transactions
        api_response = api_instance.get_transactions_users_user_id_transactions_get(user_id, page=page, size=size, x_request_id=x_request_id)
        print("The response of TransactionApi->get_transactions_users_user_id_transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->get_transactions_users_user_id_transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **size** | **int**|  | [optional] [default to 25]
 **x_request_id** | **str**|  | [optional] [default to &#39;f5f2132b-ef09-4106-8a5e-aaaaa403448f&#39;]

### Return type

[**PaginationRequestTransactionSchema**](PaginationRequestTransactionSchema.md)

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

# **payment_transaction_users_user_id_payment_transaction_post**
> TransactionSchema payment_transaction_users_user_id_payment_transaction_post(user_id, transaction_schema_create_payment_services, x_request_id=x_request_id)

Payment Transaction

### Example


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


# Enter a context with an instance of the API client
with wallet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    transaction_schema_create_payment_services = wallet_client.TransactionSchemaCreatePaymentServices() # TransactionSchemaCreatePaymentServices | 
    x_request_id = 'f5f2132b-ef09-4106-8a5e-aaaaa403448f' # str |  (optional) (default to 'f5f2132b-ef09-4106-8a5e-aaaaa403448f')

    try:
        # Payment Transaction
        api_response = api_instance.payment_transaction_users_user_id_payment_transaction_post(user_id, transaction_schema_create_payment_services, x_request_id=x_request_id)
        print("The response of TransactionApi->payment_transaction_users_user_id_payment_transaction_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->payment_transaction_users_user_id_payment_transaction_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **transaction_schema_create_payment_services** | [**TransactionSchemaCreatePaymentServices**](TransactionSchemaCreatePaymentServices.md)|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;f5f2132b-ef09-4106-8a5e-aaaaa403448f&#39;]

### Return type

[**TransactionSchema**](TransactionSchema.md)

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

# **refill_transaction_users_user_id_refill_transaction_post**
> TransactionSchema refill_transaction_users_user_id_refill_transaction_post(user_id, transaction_schema_create_income, x_request_id=x_request_id)

Refill Transaction

### Example


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


# Enter a context with an instance of the API client
with wallet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    transaction_schema_create_income = wallet_client.TransactionSchemaCreateIncome() # TransactionSchemaCreateIncome | 
    x_request_id = 'f5f2132b-ef09-4106-8a5e-aaaaa403448f' # str |  (optional) (default to 'f5f2132b-ef09-4106-8a5e-aaaaa403448f')

    try:
        # Refill Transaction
        api_response = api_instance.refill_transaction_users_user_id_refill_transaction_post(user_id, transaction_schema_create_income, x_request_id=x_request_id)
        print("The response of TransactionApi->refill_transaction_users_user_id_refill_transaction_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->refill_transaction_users_user_id_refill_transaction_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **transaction_schema_create_income** | [**TransactionSchemaCreateIncome**](TransactionSchemaCreateIncome.md)|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;f5f2132b-ef09-4106-8a5e-aaaaa403448f&#39;]

### Return type

[**TransactionSchema**](TransactionSchema.md)

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

# **update_transaction_users_user_id_transactions_transaction_id_put**
> TransactionSchema update_transaction_users_user_id_transactions_transaction_id_put(user_id, transaction_id, transaction_change_status_request, x_request_id=x_request_id)

Update Transaction

### Example


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


# Enter a context with an instance of the API client
with wallet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet_client.TransactionApi(api_client)
    user_id = 'user_id_example' # str | 
    transaction_id = 'transaction_id_example' # str | 
    transaction_change_status_request = wallet_client.TransactionChangeStatusRequest() # TransactionChangeStatusRequest | 
    x_request_id = 'f5f2132b-ef09-4106-8a5e-aaaaa403448f' # str |  (optional) (default to 'f5f2132b-ef09-4106-8a5e-aaaaa403448f')

    try:
        # Update Transaction
        api_response = api_instance.update_transaction_users_user_id_transactions_transaction_id_put(user_id, transaction_id, transaction_change_status_request, x_request_id=x_request_id)
        print("The response of TransactionApi->update_transaction_users_user_id_transactions_transaction_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->update_transaction_users_user_id_transactions_transaction_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **transaction_id** | **str**|  | 
 **transaction_change_status_request** | [**TransactionChangeStatusRequest**](TransactionChangeStatusRequest.md)|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;f5f2132b-ef09-4106-8a5e-aaaaa403448f&#39;]

### Return type

[**TransactionSchema**](TransactionSchema.md)

### Authorization

No authorization required

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

