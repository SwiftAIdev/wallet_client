# TransactionSchemaCreatePaymentServices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** |  | 
**type** | [**TypeTransactionEnum**](TypeTransactionEnum.md) |  | 

## Example

```python
from wallet_client.models.transaction_schema_create_payment_services import TransactionSchemaCreatePaymentServices

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSchemaCreatePaymentServices from a JSON string
transaction_schema_create_payment_services_instance = TransactionSchemaCreatePaymentServices.from_json(json)
# print the JSON string representation of the object
print(TransactionSchemaCreatePaymentServices.to_json())

# convert the object into a dict
transaction_schema_create_payment_services_dict = transaction_schema_create_payment_services_instance.to_dict()
# create an instance of TransactionSchemaCreatePaymentServices from a dict
transaction_schema_create_payment_services_from_dict = TransactionSchemaCreatePaymentServices.from_dict(transaction_schema_create_payment_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


