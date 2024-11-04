# wallet-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0
- Package version: 1.0.0
- Generator version: 7.10.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import wallet_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wallet_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    api_instance = wallet_client.CompanyApi(api_client)
    inn = 'inn_example' # str | 
    x_request_id = '4bb1364c-a33a-49d9-aa65-5b982ec0f864' # str |  (optional) (default to '4bb1364c-a33a-49d9-aa65-5b982ec0f864')

    try:
        # Company:Info
        api_response = api_instance.v1_get_company_info(inn, x_request_id=x_request_id)
        print("The response of CompanyApi->v1_get_company_info:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CompanyApi->v1_get_company_info: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to */wallet_service/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CompanyApi* | [**v1_get_company_info**](docs/CompanyApi.md#v1_get_company_info) | **GET** /v1/company/{inn}/info | Company:Info
*InvoiceApi* | [**v1_create_invoice**](docs/InvoiceApi.md#v1_create_invoice) | **POST** /v1/users/{user_id}/invoices | Users:Create Invoice
*InvoiceApi* | [**v1_get_invoice_by_id**](docs/InvoiceApi.md#v1_get_invoice_by_id) | **GET** /v1/users/{user_id}/invoices/{invoice_id} | Users:Get Invoice By Id
*InvoiceApi* | [**v1_get_invoices**](docs/InvoiceApi.md#v1_get_invoices) | **GET** /v1/users/{user_id}/invoices | Users:Get Invoices
*TransactionApi* | [**v1_change_status_transaction**](docs/TransactionApi.md#v1_change_status_transaction) | **PUT** /v1/users/{user_id}/transactions/{transaction_id} | Users:Change Status Transaction
*TransactionApi* | [**v1_close_acts**](docs/TransactionApi.md#v1_close_acts) | **POST** /v1/users/close_acts | Users:Close Acts
*TransactionApi* | [**v1_confirming_invoices**](docs/TransactionApi.md#v1_confirming_invoices) | **GET** /v1/users/confirming_invoices | Users:Confirming Invoices
*TransactionApi* | [**v1_end_old_transactions**](docs/TransactionApi.md#v1_end_old_transactions) | **POST** /v1/users/end_old_transactions | Users:End Old Transactions
*TransactionApi* | [**v1_get_expenses**](docs/TransactionApi.md#v1_get_expenses) | **GET** /v1/users/{user_id}/expenses | Users:Get Expenses
*TransactionApi* | [**v1_get_file_act_by_id**](docs/TransactionApi.md#v1_get_file_act_by_id) | **GET** /v1/users/{user_id}/acts/{act_id}/file | Users:Get Act By Id:File
*TransactionApi* | [**v1_get_file_invoice_by_id**](docs/TransactionApi.md#v1_get_file_invoice_by_id) | **GET** /v1/users/{user_id}/invoice/{invoice_id}/file | Users:Get Invoice By Id:File
*TransactionApi* | [**v1_get_refills**](docs/TransactionApi.md#v1_get_refills) | **GET** /v1/users/{user_id}/refills | Users:Get Refills
*TransactionApi* | [**v1_get_transaction_by_id**](docs/TransactionApi.md#v1_get_transaction_by_id) | **GET** /v1/users/{user_id}/transactions/{transaction_id} | Users:Get Transaction By Id
*TransactionApi* | [**v1_get_transactions**](docs/TransactionApi.md#v1_get_transactions) | **GET** /v1/users/{user_id}/transactions | Users:Get Transactions
*TransactionApi* | [**v1_payment_transaction**](docs/TransactionApi.md#v1_payment_transaction) | **POST** /v1/users/{user_id}/payment_transaction | Users:Payment Transaction
*TransactionApi* | [**v1_refill_transaction**](docs/TransactionApi.md#v1_refill_transaction) | **POST** /v1/users/{user_id}/refill_transaction | Users:Refill Transaction
*WalletApi* | [**v1_create_wallet**](docs/WalletApi.md#v1_create_wallet) | **POST** /v1/users/{user_id}/wallet | Users:Create Wallet
*WalletApi* | [**v1_end_wallet_testing**](docs/WalletApi.md#v1_end_wallet_testing) | **POST** /v1/users/{user_id}/wallet/testing/end | Users:End Wallet Testing
*WalletApi* | [**v1_get_wallet**](docs/WalletApi.md#v1_get_wallet) | **GET** /v1/users/{user_id}/wallet | Users:Get Wallet
*WalletApi* | [**v1_get_wallets**](docs/WalletApi.md#v1_get_wallets) | **GET** /v1/users/wallets | Users:Get Wallets
*WalletApi* | [**v1_get_wallets_invited**](docs/WalletApi.md#v1_get_wallets_invited) | **GET** /v1/users/{user_id}/invited/all | Users:Get Wallets Invited
*WalletApi* | [**v1_resume_wallet_testing**](docs/WalletApi.md#v1_resume_wallet_testing) | **POST** /v1/users/{user_id}/wallet/testing/resume | Users:Resume Wallet Testing
*WalletApi* | [**v1_start_wallet_testing**](docs/WalletApi.md#v1_start_wallet_testing) | **POST** /v1/users/{user_id}/wallet/testing/start | Users:Start Wallet Testing
*WalletApi* | [**v1_stop_wallet_testing**](docs/WalletApi.md#v1_stop_wallet_testing) | **POST** /v1/users/{user_id}/wallet/testing/stop | Users:Stop Wallet Testing
*DefaultApi* | [**health_check_health_get**](docs/DefaultApi.md#health_check_health_get) | **GET** /health | Health Check


## Documentation For Models

 - [ActSchema](docs/ActSchema.md)
 - [CategoryTransactionEnum](docs/CategoryTransactionEnum.md)
 - [CompanyData](docs/CompanyData.md)
 - [ExpenseResponse](docs/ExpenseResponse.md)
 - [HealthCheckDetailsSchema](docs/HealthCheckDetailsSchema.md)
 - [HealthCheckResponse](docs/HealthCheckResponse.md)
 - [InvoiceCreateResponse](docs/InvoiceCreateResponse.md)
 - [InvoiceResponse](docs/InvoiceResponse.md)
 - [InvoiceSchema](docs/InvoiceSchema.md)
 - [PaginationRequestInvoiceResponse](docs/PaginationRequestInvoiceResponse.md)
 - [PaginationRequestTransactionSchema](docs/PaginationRequestTransactionSchema.md)
 - [PaginationRequestTransactionSchemaRefill](docs/PaginationRequestTransactionSchemaRefill.md)
 - [PaginationRequestWalletSchema](docs/PaginationRequestWalletSchema.md)
 - [ServiceErrorPydantic](docs/ServiceErrorPydantic.md)
 - [StatusDatabase](docs/StatusDatabase.md)
 - [StatusRedis](docs/StatusRedis.md)
 - [StatusTransactionEnum](docs/StatusTransactionEnum.md)
 - [TestingSchema](docs/TestingSchema.md)
 - [TransactionBonusIntegrator](docs/TransactionBonusIntegrator.md)
 - [TransactionChangeStatusRequest](docs/TransactionChangeStatusRequest.md)
 - [TransactionCreateRefill](docs/TransactionCreateRefill.md)
 - [TransactionPaymentServicesCall](docs/TransactionPaymentServicesCall.md)
 - [TransactionSchema](docs/TransactionSchema.md)
 - [TransactionSchemaCreateIncome](docs/TransactionSchemaCreateIncome.md)
 - [TransactionSchemaCreatePaymentServices](docs/TransactionSchemaCreatePaymentServices.md)
 - [TransactionSchemaData](docs/TransactionSchemaData.md)
 - [TransactionSchemaRefill](docs/TransactionSchemaRefill.md)
 - [TypeErrorEnum](docs/TypeErrorEnum.md)
 - [TypeTransactionEnum](docs/TypeTransactionEnum.md)
 - [UserWalletResponse](docs/UserWalletResponse.md)
 - [WalletSchema](docs/WalletSchema.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="HTTPBearer"></a>
### HTTPBearer

- **Type**: Bearer authentication


## Author




