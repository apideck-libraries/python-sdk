# apideck.AccountingApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balance_sheet_one**](AccountingApi.md#balance_sheet_one) | **GET** /accounting/balance-sheet | Get BalanceSheet
[**bills_add**](AccountingApi.md#bills_add) | **POST** /accounting/bills | Create Bill
[**bills_all**](AccountingApi.md#bills_all) | **GET** /accounting/bills | List Bills
[**bills_delete**](AccountingApi.md#bills_delete) | **DELETE** /accounting/bills/{id} | Delete Bill
[**bills_one**](AccountingApi.md#bills_one) | **GET** /accounting/bills/{id} | Get Bill
[**bills_update**](AccountingApi.md#bills_update) | **PATCH** /accounting/bills/{id} | Update Bill
[**company_info_one**](AccountingApi.md#company_info_one) | **GET** /accounting/company-info | Get company info
[**credit_notes_add**](AccountingApi.md#credit_notes_add) | **POST** /accounting/credit-notes | Create Credit Note
[**credit_notes_all**](AccountingApi.md#credit_notes_all) | **GET** /accounting/credit-notes | List Credit Notes
[**credit_notes_delete**](AccountingApi.md#credit_notes_delete) | **DELETE** /accounting/credit-notes/{id} | Delete Credit Note
[**credit_notes_one**](AccountingApi.md#credit_notes_one) | **GET** /accounting/credit-notes/{id} | Get Credit Note
[**credit_notes_update**](AccountingApi.md#credit_notes_update) | **PATCH** /accounting/credit-notes/{id} | Update Credit Note
[**customers_add**](AccountingApi.md#customers_add) | **POST** /accounting/customers | Create Customer
[**customers_all**](AccountingApi.md#customers_all) | **GET** /accounting/customers | List Customers
[**customers_delete**](AccountingApi.md#customers_delete) | **DELETE** /accounting/customers/{id} | Delete Customer
[**customers_one**](AccountingApi.md#customers_one) | **GET** /accounting/customers/{id} | Get Customer
[**customers_update**](AccountingApi.md#customers_update) | **PATCH** /accounting/customers/{id} | Update Customer
[**invoice_items_add**](AccountingApi.md#invoice_items_add) | **POST** /accounting/invoice-items | Create Invoice Item
[**invoice_items_all**](AccountingApi.md#invoice_items_all) | **GET** /accounting/invoice-items | List Invoice Items
[**invoice_items_delete**](AccountingApi.md#invoice_items_delete) | **DELETE** /accounting/invoice-items/{id} | Delete Invoice Item
[**invoice_items_one**](AccountingApi.md#invoice_items_one) | **GET** /accounting/invoice-items/{id} | Get Invoice Item
[**invoice_items_update**](AccountingApi.md#invoice_items_update) | **PATCH** /accounting/invoice-items/{id} | Update Invoice Item
[**invoices_add**](AccountingApi.md#invoices_add) | **POST** /accounting/invoices | Create Invoice
[**invoices_all**](AccountingApi.md#invoices_all) | **GET** /accounting/invoices | List Invoices
[**invoices_delete**](AccountingApi.md#invoices_delete) | **DELETE** /accounting/invoices/{id} | Delete Invoice
[**invoices_one**](AccountingApi.md#invoices_one) | **GET** /accounting/invoices/{id} | Get Invoice
[**invoices_update**](AccountingApi.md#invoices_update) | **PATCH** /accounting/invoices/{id} | Update Invoice
[**ledger_accounts_add**](AccountingApi.md#ledger_accounts_add) | **POST** /accounting/ledger-accounts | Create Ledger Account
[**ledger_accounts_all**](AccountingApi.md#ledger_accounts_all) | **GET** /accounting/ledger-accounts | List Ledger Accounts
[**ledger_accounts_delete**](AccountingApi.md#ledger_accounts_delete) | **DELETE** /accounting/ledger-accounts/{id} | Delete Ledger Account
[**ledger_accounts_one**](AccountingApi.md#ledger_accounts_one) | **GET** /accounting/ledger-accounts/{id} | Get Ledger Account
[**ledger_accounts_update**](AccountingApi.md#ledger_accounts_update) | **PATCH** /accounting/ledger-accounts/{id} | Update Ledger Account
[**payments_add**](AccountingApi.md#payments_add) | **POST** /accounting/payments | Create Payment
[**payments_all**](AccountingApi.md#payments_all) | **GET** /accounting/payments | List Payments
[**payments_delete**](AccountingApi.md#payments_delete) | **DELETE** /accounting/payments/{id} | Delete Payment
[**payments_one**](AccountingApi.md#payments_one) | **GET** /accounting/payments/{id} | Get Payment
[**payments_update**](AccountingApi.md#payments_update) | **PATCH** /accounting/payments/{id} | Update Payment
[**profit_and_loss_one**](AccountingApi.md#profit_and_loss_one) | **GET** /accounting/profit-and-loss | Get Profit and Loss
[**suppliers_add**](AccountingApi.md#suppliers_add) | **POST** /accounting/suppliers | Create Supplier
[**suppliers_all**](AccountingApi.md#suppliers_all) | **GET** /accounting/suppliers | List Suppliers
[**suppliers_delete**](AccountingApi.md#suppliers_delete) | **DELETE** /accounting/suppliers/{id} | Delete Supplier
[**suppliers_one**](AccountingApi.md#suppliers_one) | **GET** /accounting/suppliers/{id} | Get Supplier
[**suppliers_update**](AccountingApi.md#suppliers_update) | **PATCH** /accounting/suppliers/{id} | Update Supplier
[**tax_rates_add**](AccountingApi.md#tax_rates_add) | **POST** /accounting/tax-rates | Create Tax Rate
[**tax_rates_all**](AccountingApi.md#tax_rates_all) | **GET** /accounting/tax-rates | List Tax Rates
[**tax_rates_delete**](AccountingApi.md#tax_rates_delete) | **DELETE** /accounting/tax-rates/{id} | Delete Tax Rate
[**tax_rates_one**](AccountingApi.md#tax_rates_one) | **GET** /accounting/tax-rates/{id} | Get Tax Rate
[**tax_rates_update**](AccountingApi.md#tax_rates_update) | **PATCH** /accounting/tax-rates/{id} | Update Tax Rate


# **balance_sheet_one**
> GetBalanceSheetResponse balance_sheet_one()

Get BalanceSheet

Get BalanceSheet

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.balance_sheet_filter import BalanceSheetFilter
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.get_balance_sheet_response import GetBalanceSheetResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.passthrough import Passthrough
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    pass_through = Passthrough() # Passthrough | Optional unmapped key/values that will be passed through to downstream as query parameters (optional)
    filter = BalanceSheetFilter(
        start_date="2021-01-01",
        end_date="2021-12-31",
    ) # BalanceSheetFilter | Apply filters (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get BalanceSheet
        api_response = api_instance.balance_sheet_one(consumer_id=consumer_id, app_id=app_id, service_id=service_id, pass_through=pass_through, filter=filter, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->balance_sheet_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **pass_through** | **Passthrough**| Optional unmapped key/values that will be passed through to downstream as query parameters | [optional]
 **filter** | **BalanceSheetFilter**| Apply filters | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**GetBalanceSheetResponse**](GetBalanceSheetResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BalanceSheet |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **bills_add**
> CreateBillResponse bills_add(bill)

Create Bill

Create Bill

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.bill import Bill
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.create_bill_response import CreateBillResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    bill = Bill(
        supplier=LinkedSupplier(
            id="12345",
            display_name="Windsurf Shop",
            address=Address(
                id="123",
                type="primary",
                string="25 Spring Street, Blackburn, VIC 3130",
                name="HQ US",
                line1="Main street",
                line2="apt #",
                line3="Suite #",
                line4="delivery instructions",
                street_number="25",
                city="San Francisco",
                state="CA",
                postal_code="94104",
                country="US",
                latitude="40.759211",
                longitude="-73.984638",
                county="Santa Clara",
                contact_name="Elon Musk",
                salutation="Mr",
                phone_number="111-111-1111",
                fax="122-111-1111",
                email="elon@musk.com",
                website="https://elonmusk.com",
                row_version="1-12345",
            ),
        ),
        currency=Currency("USD"),
        currency_rate=0.69,
        tax_inclusive=True,
        bill_date=dateutil_parser('Wed Sep 30 00:00:00 UTC 2020').date(),
        due_date=dateutil_parser('Fri Oct 30 00:00:00 UTC 2020').date(),
        paid_date=dateutil_parser('Fri Oct 30 00:00:00 UTC 2020').date(),
        po_number="90000117",
        reference="123456",
        line_items=[
            BillLineItem(
                row_id="12345",
                code="120-C",
                line_number=1,
                description="Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
                type="expense_account",
                tax_amount=27500,
                total_amount=27500,
                quantity=1,
                unit_price=27500.5,
                unit_of_measure="pc.",
                discount_percentage=0.01,
                location_id="1234",
                department_id="1234",
                item=LinkedInvoiceItem(
                    id="12344",
                ),
                ledger_account=LinkedLedgerAccount(
                    id="123456",
                    nominal_code="N091",
                    code="453",
                ),
                tax_rate=LinkedTaxRate(
                    id="123456",
                ),
                row_version="1-12345",
            ),
        ],
        terms="Net 30 days",
        balance=27500,
        deposit=0,
        sub_total=27500,
        total_tax=2500,
        total=27500,
        tax_code="1234",
        notes="Some notes about this bill.",
        status="draft",
        ledger_account=LinkedLedgerAccount(
            id="123456",
            nominal_code="N091",
            code="453",
        ),
        bill_number="10001",
        row_version="1-12345",
    ) # Bill | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Bill
        api_response = api_instance.bills_add(bill)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->bills_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Bill
        api_response = api_instance.bills_add(bill, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->bills_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill** | [**Bill**](Bill.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateBillResponse**](CreateBillResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Bill created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **bills_all**
> GetBillsResponse bills_all()

List Bills

List Bills

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.get_bills_response import GetBillsResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of records to return (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Bills
        api_response = api_instance.bills_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->bills_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **limit** | **int**| Number of records to return | [optional] if omitted the server will use the default value of 20

### Return type

[**GetBillsResponse**](GetBillsResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bills |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **bills_delete**
> DeleteBillResponse bills_delete(id)

Delete Bill

Delete Bill

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.delete_bill_response import DeleteBillResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete Bill
        api_response = api_instance.bills_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->bills_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Bill
        api_response = api_instance.bills_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->bills_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**DeleteBillResponse**](DeleteBillResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bill deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **bills_one**
> GetBillResponse bills_one(id)

Get Bill

Get Bill

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.get_bill_response import GetBillResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get Bill
        api_response = api_instance.bills_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->bills_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Bill
        api_response = api_instance.bills_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->bills_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**GetBillResponse**](GetBillResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bill |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **bills_update**
> UpdateBillResponse bills_update(id, bill)

Update Bill

Update Bill

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.bill import Bill
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.update_bill_response import UpdateBillResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    bill = Bill(
        supplier=LinkedSupplier(
            id="12345",
            display_name="Windsurf Shop",
            address=Address(
                id="123",
                type="primary",
                string="25 Spring Street, Blackburn, VIC 3130",
                name="HQ US",
                line1="Main street",
                line2="apt #",
                line3="Suite #",
                line4="delivery instructions",
                street_number="25",
                city="San Francisco",
                state="CA",
                postal_code="94104",
                country="US",
                latitude="40.759211",
                longitude="-73.984638",
                county="Santa Clara",
                contact_name="Elon Musk",
                salutation="Mr",
                phone_number="111-111-1111",
                fax="122-111-1111",
                email="elon@musk.com",
                website="https://elonmusk.com",
                row_version="1-12345",
            ),
        ),
        currency=Currency("USD"),
        currency_rate=0.69,
        tax_inclusive=True,
        bill_date=dateutil_parser('Wed Sep 30 00:00:00 UTC 2020').date(),
        due_date=dateutil_parser('Fri Oct 30 00:00:00 UTC 2020').date(),
        paid_date=dateutil_parser('Fri Oct 30 00:00:00 UTC 2020').date(),
        po_number="90000117",
        reference="123456",
        line_items=[
            BillLineItem(
                row_id="12345",
                code="120-C",
                line_number=1,
                description="Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
                type="expense_account",
                tax_amount=27500,
                total_amount=27500,
                quantity=1,
                unit_price=27500.5,
                unit_of_measure="pc.",
                discount_percentage=0.01,
                location_id="1234",
                department_id="1234",
                item=LinkedInvoiceItem(
                    id="12344",
                ),
                ledger_account=LinkedLedgerAccount(
                    id="123456",
                    nominal_code="N091",
                    code="453",
                ),
                tax_rate=LinkedTaxRate(
                    id="123456",
                ),
                row_version="1-12345",
            ),
        ],
        terms="Net 30 days",
        balance=27500,
        deposit=0,
        sub_total=27500,
        total_tax=2500,
        total=27500,
        tax_code="1234",
        notes="Some notes about this bill.",
        status="draft",
        ledger_account=LinkedLedgerAccount(
            id="123456",
            nominal_code="N091",
            code="453",
        ),
        bill_number="10001",
        row_version="1-12345",
    ) # Bill | 
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update Bill
        api_response = api_instance.bills_update(id, bill)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->bills_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Bill
        api_response = api_instance.bills_update(id, bill, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->bills_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **bill** | [**Bill**](Bill.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateBillResponse**](UpdateBillResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bill Updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **company_info_one**
> GetCompanyInfoResponse company_info_one()

Get company info

Get company info

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.get_company_info_response import GetCompanyInfoResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get company info
        api_response = api_instance.company_info_one(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->company_info_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**GetCompanyInfoResponse**](GetCompanyInfoResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CompanyInfo |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **credit_notes_add**
> CreateCreditNoteResponse credit_notes_add(credit_note)

Create Credit Note

Create Credit Note

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.create_credit_note_response import CreateCreditNoteResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.credit_note import CreditNote
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    credit_note = CreditNote(
        number="OIT00546",
        customer=LinkedCustomer(
            id="12345",
            display_name="Windsurf Shop",
            name="Windsurf Shop",
        ),
        currency=Currency("USD"),
        currency_rate=0.69,
        tax_inclusive=True,
        sub_total=27500,
        total_amount=49.99,
        total_tax=2500,
        tax_code="1234",
        balance=27500,
        remaining_credit=27500,
        status="authorised",
        reference="123456",
        date_issued=dateutil_parser('2021-05-01T12:00:00Z'),
        date_paid=dateutil_parser('2021-05-01T12:00:00Z'),
        type="accounts_receivable_credit",
        account=LinkedLedgerAccount(
            id="123456",
            nominal_code="N091",
            code="453",
        ),
        line_items=[
            InvoiceLineItem(
                row_id="12345",
                code="120-C",
                line_number=1,
                description="Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
                type="sales_item",
                tax_amount=27500,
                total_amount=27500,
                quantity=1,
                unit_price=27500.5,
                unit_of_measure="pc.",
                discount_percentage=0.01,
                location_id="1234",
                department_id="1234",
                item=LinkedInvoiceItem(
                    id="12344",
                ),
                tax_rate=LinkedTaxRate(
                    id="123456",
                ),
                ledger_account=LinkedLedgerAccount(
                    id="123456",
                    nominal_code="N091",
                    code="453",
                ),
                row_version="1-12345",
            ),
        ],
        allocations=[
            None,
        ],
        note="Some notes about this credit note",
        row_version="1-12345",
    ) # CreditNote | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Credit Note
        api_response = api_instance.credit_notes_add(credit_note)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->credit_notes_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Credit Note
        api_response = api_instance.credit_notes_add(credit_note, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->credit_notes_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note** | [**CreditNote**](CreditNote.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateCreditNoteResponse**](CreateCreditNoteResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Credit Note created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **credit_notes_all**
> GetCreditNotesResponse credit_notes_all()

List Credit Notes

List Credit Notes

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.get_credit_notes_response import GetCreditNotesResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of records to return (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Credit Notes
        api_response = api_instance.credit_notes_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->credit_notes_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **limit** | **int**| Number of records to return | [optional] if omitted the server will use the default value of 20

### Return type

[**GetCreditNotesResponse**](GetCreditNotesResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Credit Notes |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **credit_notes_delete**
> DeleteCreditNoteResponse credit_notes_delete(id)

Delete Credit Note

Delete Credit Note

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.delete_credit_note_response import DeleteCreditNoteResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete Credit Note
        api_response = api_instance.credit_notes_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->credit_notes_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Credit Note
        api_response = api_instance.credit_notes_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->credit_notes_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**DeleteCreditNoteResponse**](DeleteCreditNoteResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Credit Note deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **credit_notes_one**
> GetCreditNoteResponse credit_notes_one(id)

Get Credit Note

Get Credit Note

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.get_credit_note_response import GetCreditNoteResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get Credit Note
        api_response = api_instance.credit_notes_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->credit_notes_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Credit Note
        api_response = api_instance.credit_notes_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->credit_notes_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**GetCreditNoteResponse**](GetCreditNoteResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Credit Note |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **credit_notes_update**
> UpdateCreditNoteResponse credit_notes_update(id, credit_note)

Update Credit Note

Update Credit Note

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.update_credit_note_response import UpdateCreditNoteResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.credit_note import CreditNote
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    credit_note = CreditNote(
        number="OIT00546",
        customer=LinkedCustomer(
            id="12345",
            display_name="Windsurf Shop",
            name="Windsurf Shop",
        ),
        currency=Currency("USD"),
        currency_rate=0.69,
        tax_inclusive=True,
        sub_total=27500,
        total_amount=49.99,
        total_tax=2500,
        tax_code="1234",
        balance=27500,
        remaining_credit=27500,
        status="authorised",
        reference="123456",
        date_issued=dateutil_parser('2021-05-01T12:00:00Z'),
        date_paid=dateutil_parser('2021-05-01T12:00:00Z'),
        type="accounts_receivable_credit",
        account=LinkedLedgerAccount(
            id="123456",
            nominal_code="N091",
            code="453",
        ),
        line_items=[
            InvoiceLineItem(
                row_id="12345",
                code="120-C",
                line_number=1,
                description="Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
                type="sales_item",
                tax_amount=27500,
                total_amount=27500,
                quantity=1,
                unit_price=27500.5,
                unit_of_measure="pc.",
                discount_percentage=0.01,
                location_id="1234",
                department_id="1234",
                item=LinkedInvoiceItem(
                    id="12344",
                ),
                tax_rate=LinkedTaxRate(
                    id="123456",
                ),
                ledger_account=LinkedLedgerAccount(
                    id="123456",
                    nominal_code="N091",
                    code="453",
                ),
                row_version="1-12345",
            ),
        ],
        allocations=[
            None,
        ],
        note="Some notes about this credit note",
        row_version="1-12345",
    ) # CreditNote | 
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update Credit Note
        api_response = api_instance.credit_notes_update(id, credit_note)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->credit_notes_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Credit Note
        api_response = api_instance.credit_notes_update(id, credit_note, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->credit_notes_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **credit_note** | [**CreditNote**](CreditNote.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateCreditNoteResponse**](UpdateCreditNoteResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Credit Note updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **customers_add**
> CreateCustomerResponse customers_add(accounting_customer)

Create Customer

Create Customer

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.accounting_customer import AccountingCustomer
from apideck.model.create_customer_response import CreateCustomerResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    accounting_customer = AccountingCustomer(
        display_id="EMP00101",
        display_name="Windsurf Shop",
        company_name="SpaceX",
        title="CEO",
        first_name="Elon",
        middle_name="D.",
        last_name="Musk",
        suffix="Jr.",
        individual=True,
        addresses=[
            Address(
                id="123",
                type="primary",
                string="25 Spring Street, Blackburn, VIC 3130",
                name="HQ US",
                line1="Main street",
                line2="apt #",
                line3="Suite #",
                line4="delivery instructions",
                street_number="25",
                city="San Francisco",
                state="CA",
                postal_code="94104",
                country="US",
                latitude="40.759211",
                longitude="-73.984638",
                county="Santa Clara",
                contact_name="Elon Musk",
                salutation="Mr",
                phone_number="111-111-1111",
                fax="122-111-1111",
                email="elon@musk.com",
                website="https://elonmusk.com",
                row_version="1-12345",
            ),
        ],
        notes="Some notes about this customer",
        phone_numbers=[
            PhoneNumber(
                id="12345",
                country_code="1",
                area_code="323",
                number="111-111-1111",
                extension="105",
                type="primary",
            ),
        ],
        emails=[
            Email(
                id="123",
                email="elon@musk.com",
                type="primary",
            ),
        ],
        websites=[
            Website(
                id="12345",
                url="http://example.com",
                type="primary",
            ),
        ],
        tax_rate=LinkedTaxRate(
            id="123456",
        ),
        tax_number="US123945459",
        currency=Currency("USD"),
        bank_accounts=[
            BankAccount(
                iban="CH2989144532982975332",
                bic="AUDSCHGGXXX",
                bsb_number="062-001",
                branch_identifier="001",
                bank_code="BNH",
                account_number="123465",
                account_name="SPACEX LLC",
                account_type="credit_card",
                currency=Currency("USD"),
            ),
        ],
        status="active",
        row_version="1-12345",
    ) # AccountingCustomer | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Customer
        api_response = api_instance.customers_add(accounting_customer)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->customers_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Customer
        api_response = api_instance.customers_add(accounting_customer, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->customers_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounting_customer** | [**AccountingCustomer**](AccountingCustomer.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateCustomerResponse**](CreateCustomerResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Customers |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **customers_all**
> GetCustomersResponse customers_all()

List Customers

List Customers

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.customers_filter import CustomersFilter
from apideck.model.get_customers_response import GetCustomersResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of records to return (optional) if omitted the server will use the default value of 20
    filter = CustomersFilter(
        company_name="SpaceX",
        display_name="Techno King",
        first_name="Elon",
        last_name="Musk",
        email="elon@spacex.com",
    ) # CustomersFilter | Apply filters (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Customers
        api_response = api_instance.customers_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, filter=filter)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->customers_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **limit** | **int**| Number of records to return | [optional] if omitted the server will use the default value of 20
 **filter** | **CustomersFilter**| Apply filters | [optional]

### Return type

[**GetCustomersResponse**](GetCustomersResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Customers |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **customers_delete**
> DeleteCustomerResponse customers_delete(id)

Delete Customer

Delete Customer

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.delete_customer_response import DeleteCustomerResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete Customer
        api_response = api_instance.customers_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->customers_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Customer
        api_response = api_instance.customers_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->customers_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**DeleteCustomerResponse**](DeleteCustomerResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Customers |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **customers_one**
> GetCustomerResponse customers_one(id)

Get Customer

Get Customer

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.get_customer_response import GetCustomerResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get Customer
        api_response = api_instance.customers_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->customers_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Customer
        api_response = api_instance.customers_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->customers_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**GetCustomerResponse**](GetCustomerResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Customer |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **customers_update**
> UpdateCustomerResponse customers_update(id, accounting_customer)

Update Customer

Update Customer

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.accounting_customer import AccountingCustomer
from apideck.model.update_customer_response import UpdateCustomerResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    accounting_customer = AccountingCustomer(
        display_id="EMP00101",
        display_name="Windsurf Shop",
        company_name="SpaceX",
        title="CEO",
        first_name="Elon",
        middle_name="D.",
        last_name="Musk",
        suffix="Jr.",
        individual=True,
        addresses=[
            Address(
                id="123",
                type="primary",
                string="25 Spring Street, Blackburn, VIC 3130",
                name="HQ US",
                line1="Main street",
                line2="apt #",
                line3="Suite #",
                line4="delivery instructions",
                street_number="25",
                city="San Francisco",
                state="CA",
                postal_code="94104",
                country="US",
                latitude="40.759211",
                longitude="-73.984638",
                county="Santa Clara",
                contact_name="Elon Musk",
                salutation="Mr",
                phone_number="111-111-1111",
                fax="122-111-1111",
                email="elon@musk.com",
                website="https://elonmusk.com",
                row_version="1-12345",
            ),
        ],
        notes="Some notes about this customer",
        phone_numbers=[
            PhoneNumber(
                id="12345",
                country_code="1",
                area_code="323",
                number="111-111-1111",
                extension="105",
                type="primary",
            ),
        ],
        emails=[
            Email(
                id="123",
                email="elon@musk.com",
                type="primary",
            ),
        ],
        websites=[
            Website(
                id="12345",
                url="http://example.com",
                type="primary",
            ),
        ],
        tax_rate=LinkedTaxRate(
            id="123456",
        ),
        tax_number="US123945459",
        currency=Currency("USD"),
        bank_accounts=[
            BankAccount(
                iban="CH2989144532982975332",
                bic="AUDSCHGGXXX",
                bsb_number="062-001",
                branch_identifier="001",
                bank_code="BNH",
                account_number="123465",
                account_name="SPACEX LLC",
                account_type="credit_card",
                currency=Currency("USD"),
            ),
        ],
        status="active",
        row_version="1-12345",
    ) # AccountingCustomer | 
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update Customer
        api_response = api_instance.customers_update(id, accounting_customer)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->customers_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Customer
        api_response = api_instance.customers_update(id, accounting_customer, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->customers_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **accounting_customer** | [**AccountingCustomer**](AccountingCustomer.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateCustomerResponse**](UpdateCustomerResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Customers |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **invoice_items_add**
> CreateInvoiceItemResponse invoice_items_add(invoice_item)

Create Invoice Item

Create Invoice Item

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.invoice_item import InvoiceItem
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.create_invoice_item_response import CreateInvoiceItemResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    invoice_item = InvoiceItem(
        name="Model Y",
        description="Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
        code="120-C",
        sold=True,
        purchased=True,
        tracked=True,
        inventory_date=dateutil_parser('Fri Oct 30 00:00:00 UTC 2020').date(),
        type="inventory",
        sales_details=InvoiceItemSalesDetails(
            unit_price=27500.5,
            unit_of_measure="pc.",
            tax_inclusive=True,
            tax_rate=LinkedTaxRate(
                id="123456",
            ),
        ),
        purchase_details=InvoiceItemSalesDetails(
            unit_price=27500.5,
            unit_of_measure="pc.",
            tax_inclusive=True,
            tax_rate=LinkedTaxRate(
                id="123456",
            ),
        ),
        quantity=1,
        unit_price=27500.5,
        asset_account=LinkedLedgerAccount(
            id="123456",
            nominal_code="N091",
            code="453",
        ),
        income_account=LinkedLedgerAccount(
            id="123456",
            nominal_code="N091",
            code="453",
        ),
        expense_account=LinkedLedgerAccount(
            id="123456",
            nominal_code="N091",
            code="453",
        ),
        active=True,
        row_version="1-12345",
    ) # InvoiceItem | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Invoice Item
        api_response = api_instance.invoice_items_add(invoice_item)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->invoice_items_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Invoice Item
        api_response = api_instance.invoice_items_add(invoice_item, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->invoice_items_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_item** | [**InvoiceItem**](InvoiceItem.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateInvoiceItemResponse**](CreateInvoiceItemResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | InvoiceItems |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **invoice_items_all**
> GetInvoiceItemsResponse invoice_items_all()

List Invoice Items

List Invoice Items

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.invoice_items_filter import InvoiceItemsFilter
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.get_invoice_items_response import GetInvoiceItemsResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of records to return (optional) if omitted the server will use the default value of 20
    filter = InvoiceItemsFilter(
        name="Widgets Large",
    ) # InvoiceItemsFilter | Apply filters (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Invoice Items
        api_response = api_instance.invoice_items_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, filter=filter)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->invoice_items_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **limit** | **int**| Number of records to return | [optional] if omitted the server will use the default value of 20
 **filter** | **InvoiceItemsFilter**| Apply filters | [optional]

### Return type

[**GetInvoiceItemsResponse**](GetInvoiceItemsResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | InvoiceItems |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **invoice_items_delete**
> DeleteTaxRateResponse invoice_items_delete(id)

Delete Invoice Item

Delete Invoice Item

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.delete_tax_rate_response import DeleteTaxRateResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete Invoice Item
        api_response = api_instance.invoice_items_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->invoice_items_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Invoice Item
        api_response = api_instance.invoice_items_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->invoice_items_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**DeleteTaxRateResponse**](DeleteTaxRateResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | InvoiceItems |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **invoice_items_one**
> GetInvoiceItemResponse invoice_items_one(id)

Get Invoice Item

Get Invoice Item

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.get_invoice_item_response import GetInvoiceItemResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get Invoice Item
        api_response = api_instance.invoice_items_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->invoice_items_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Invoice Item
        api_response = api_instance.invoice_items_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->invoice_items_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**GetInvoiceItemResponse**](GetInvoiceItemResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | InvoiceItems |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **invoice_items_update**
> UpdateInvoiceItemsResponse invoice_items_update(id, invoice_item)

Update Invoice Item

Update Invoice Item

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.invoice_item import InvoiceItem
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.update_invoice_items_response import UpdateInvoiceItemsResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    invoice_item = InvoiceItem(
        name="Model Y",
        description="Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
        code="120-C",
        sold=True,
        purchased=True,
        tracked=True,
        inventory_date=dateutil_parser('Fri Oct 30 00:00:00 UTC 2020').date(),
        type="inventory",
        sales_details=InvoiceItemSalesDetails(
            unit_price=27500.5,
            unit_of_measure="pc.",
            tax_inclusive=True,
            tax_rate=LinkedTaxRate(
                id="123456",
            ),
        ),
        purchase_details=InvoiceItemSalesDetails(
            unit_price=27500.5,
            unit_of_measure="pc.",
            tax_inclusive=True,
            tax_rate=LinkedTaxRate(
                id="123456",
            ),
        ),
        quantity=1,
        unit_price=27500.5,
        asset_account=LinkedLedgerAccount(
            id="123456",
            nominal_code="N091",
            code="453",
        ),
        income_account=LinkedLedgerAccount(
            id="123456",
            nominal_code="N091",
            code="453",
        ),
        expense_account=LinkedLedgerAccount(
            id="123456",
            nominal_code="N091",
            code="453",
        ),
        active=True,
        row_version="1-12345",
    ) # InvoiceItem | 
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update Invoice Item
        api_response = api_instance.invoice_items_update(id, invoice_item)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->invoice_items_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Invoice Item
        api_response = api_instance.invoice_items_update(id, invoice_item, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->invoice_items_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **invoice_item** | [**InvoiceItem**](InvoiceItem.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateInvoiceItemsResponse**](UpdateInvoiceItemsResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | InvoiceItems |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **invoices_add**
> CreateInvoiceResponse invoices_add(invoice)

Create Invoice

Create Invoice

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.invoice import Invoice
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.create_invoice_response import CreateInvoiceResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    invoice = Invoice(
        type="service",
        number="OIT00546",
        customer=LinkedCustomer(
            id="12345",
            display_name="Windsurf Shop",
            name="Windsurf Shop",
        ),
        invoice_date=dateutil_parser('Wed Sep 30 00:00:00 UTC 2020').date(),
        due_date=dateutil_parser('Wed Sep 30 00:00:00 UTC 2020').date(),
        terms="Net 30 days",
        po_number="90000117",
        reference="123456",
        status="draft",
        invoice_sent=True,
        currency=Currency("USD"),
        currency_rate=0.69,
        tax_inclusive=True,
        sub_total=27500,
        total_tax=2500,
        tax_code="1234",
        discount_percentage=5.5,
        total=27500,
        balance=27500,
        deposit=0,
        customer_memo="Thank you for your business and have a great day!",
        line_items=[
            InvoiceLineItem(
                row_id="12345",
                code="120-C",
                line_number=1,
                description="Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
                type="sales_item",
                tax_amount=27500,
                total_amount=27500,
                quantity=1,
                unit_price=27500.5,
                unit_of_measure="pc.",
                discount_percentage=0.01,
                location_id="1234",
                department_id="1234",
                item=LinkedInvoiceItem(
                    id="12344",
                ),
                tax_rate=LinkedTaxRate(
                    id="123456",
                ),
                ledger_account=LinkedLedgerAccount(
                    id="123456",
                    nominal_code="N091",
                    code="453",
                ),
                row_version="1-12345",
            ),
        ],
        billing_address=Address(
            id="123",
            type="primary",
            string="25 Spring Street, Blackburn, VIC 3130",
            name="HQ US",
            line1="Main street",
            line2="apt #",
            line3="Suite #",
            line4="delivery instructions",
            street_number="25",
            city="San Francisco",
            state="CA",
            postal_code="94104",
            country="US",
            latitude="40.759211",
            longitude="-73.984638",
            county="Santa Clara",
            contact_name="Elon Musk",
            salutation="Mr",
            phone_number="111-111-1111",
            fax="122-111-1111",
            email="elon@musk.com",
            website="https://elonmusk.com",
            row_version="1-12345",
        ),
        shipping_address=Address(
            id="123",
            type="primary",
            string="25 Spring Street, Blackburn, VIC 3130",
            name="HQ US",
            line1="Main street",
            line2="apt #",
            line3="Suite #",
            line4="delivery instructions",
            street_number="25",
            city="San Francisco",
            state="CA",
            postal_code="94104",
            country="US",
            latitude="40.759211",
            longitude="-73.984638",
            county="Santa Clara",
            contact_name="Elon Musk",
            salutation="Mr",
            phone_number="111-111-1111",
            fax="122-111-1111",
            email="elon@musk.com",
            website="https://elonmusk.com",
            row_version="1-12345",
        ),
        template_id="123456",
        source_document_url="https://www.invoicesolution.com/invoice/123456",
        row_version="1-12345",
    ) # Invoice | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Invoice
        api_response = api_instance.invoices_add(invoice)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->invoices_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Invoice
        api_response = api_instance.invoices_add(invoice, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->invoices_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice** | [**Invoice**](Invoice.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateInvoiceResponse**](CreateInvoiceResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Invoice created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **invoices_all**
> GetInvoicesResponse invoices_all()

List Invoices

List Invoices

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.invoices_sort import InvoicesSort
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.get_invoices_response import GetInvoicesResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of records to return (optional) if omitted the server will use the default value of 20
    sort = InvoicesSort(
        by="updated_at",
        direction=SortDirection("asc"),
    ) # InvoicesSort | Apply sorting (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Invoices
        api_response = api_instance.invoices_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, sort=sort)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->invoices_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **limit** | **int**| Number of records to return | [optional] if omitted the server will use the default value of 20
 **sort** | **InvoicesSort**| Apply sorting | [optional]

### Return type

[**GetInvoicesResponse**](GetInvoicesResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invoices |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **invoices_delete**
> DeleteInvoiceResponse invoices_delete(id)

Delete Invoice

Delete Invoice

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.delete_invoice_response import DeleteInvoiceResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete Invoice
        api_response = api_instance.invoices_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->invoices_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Invoice
        api_response = api_instance.invoices_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->invoices_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**DeleteInvoiceResponse**](DeleteInvoiceResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invoice deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **invoices_one**
> GetInvoiceResponse invoices_one(id)

Get Invoice

Get Invoice

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.get_invoice_response import GetInvoiceResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get Invoice
        api_response = api_instance.invoices_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->invoices_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Invoice
        api_response = api_instance.invoices_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->invoices_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**GetInvoiceResponse**](GetInvoiceResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invoice |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **invoices_update**
> UpdateInvoiceResponse invoices_update(id, invoice)

Update Invoice

Update Invoice

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.invoice import Invoice
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.update_invoice_response import UpdateInvoiceResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    invoice = Invoice(
        type="service",
        number="OIT00546",
        customer=LinkedCustomer(
            id="12345",
            display_name="Windsurf Shop",
            name="Windsurf Shop",
        ),
        invoice_date=dateutil_parser('Wed Sep 30 00:00:00 UTC 2020').date(),
        due_date=dateutil_parser('Wed Sep 30 00:00:00 UTC 2020').date(),
        terms="Net 30 days",
        po_number="90000117",
        reference="123456",
        status="draft",
        invoice_sent=True,
        currency=Currency("USD"),
        currency_rate=0.69,
        tax_inclusive=True,
        sub_total=27500,
        total_tax=2500,
        tax_code="1234",
        discount_percentage=5.5,
        total=27500,
        balance=27500,
        deposit=0,
        customer_memo="Thank you for your business and have a great day!",
        line_items=[
            InvoiceLineItem(
                row_id="12345",
                code="120-C",
                line_number=1,
                description="Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
                type="sales_item",
                tax_amount=27500,
                total_amount=27500,
                quantity=1,
                unit_price=27500.5,
                unit_of_measure="pc.",
                discount_percentage=0.01,
                location_id="1234",
                department_id="1234",
                item=LinkedInvoiceItem(
                    id="12344",
                ),
                tax_rate=LinkedTaxRate(
                    id="123456",
                ),
                ledger_account=LinkedLedgerAccount(
                    id="123456",
                    nominal_code="N091",
                    code="453",
                ),
                row_version="1-12345",
            ),
        ],
        billing_address=Address(
            id="123",
            type="primary",
            string="25 Spring Street, Blackburn, VIC 3130",
            name="HQ US",
            line1="Main street",
            line2="apt #",
            line3="Suite #",
            line4="delivery instructions",
            street_number="25",
            city="San Francisco",
            state="CA",
            postal_code="94104",
            country="US",
            latitude="40.759211",
            longitude="-73.984638",
            county="Santa Clara",
            contact_name="Elon Musk",
            salutation="Mr",
            phone_number="111-111-1111",
            fax="122-111-1111",
            email="elon@musk.com",
            website="https://elonmusk.com",
            row_version="1-12345",
        ),
        shipping_address=Address(
            id="123",
            type="primary",
            string="25 Spring Street, Blackburn, VIC 3130",
            name="HQ US",
            line1="Main street",
            line2="apt #",
            line3="Suite #",
            line4="delivery instructions",
            street_number="25",
            city="San Francisco",
            state="CA",
            postal_code="94104",
            country="US",
            latitude="40.759211",
            longitude="-73.984638",
            county="Santa Clara",
            contact_name="Elon Musk",
            salutation="Mr",
            phone_number="111-111-1111",
            fax="122-111-1111",
            email="elon@musk.com",
            website="https://elonmusk.com",
            row_version="1-12345",
        ),
        template_id="123456",
        source_document_url="https://www.invoicesolution.com/invoice/123456",
        row_version="1-12345",
    ) # Invoice | 
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update Invoice
        api_response = api_instance.invoices_update(id, invoice)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->invoices_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Invoice
        api_response = api_instance.invoices_update(id, invoice, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->invoices_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **invoice** | [**Invoice**](Invoice.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateInvoiceResponse**](UpdateInvoiceResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invoice updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **ledger_accounts_add**
> CreateLedgerAccountResponse ledger_accounts_add(ledger_account)

Create Ledger Account

Create Ledger Account

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.ledger_account import LedgerAccount
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.create_ledger_account_response import CreateLedgerAccountResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    ledger_account = LedgerAccount() # LedgerAccount | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Ledger Account
        api_response = api_instance.ledger_accounts_add(ledger_account)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->ledger_accounts_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Ledger Account
        api_response = api_instance.ledger_accounts_add(ledger_account, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->ledger_accounts_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger_account** | [**LedgerAccount**](LedgerAccount.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateLedgerAccountResponse**](CreateLedgerAccountResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | LedgerAccount created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **ledger_accounts_all**
> GetLedgerAccountsResponse ledger_accounts_all()

List Ledger Accounts

List Ledger Accounts

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.get_ledger_accounts_response import GetLedgerAccountsResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of records to return (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Ledger Accounts
        api_response = api_instance.ledger_accounts_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->ledger_accounts_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **limit** | **int**| Number of records to return | [optional] if omitted the server will use the default value of 20

### Return type

[**GetLedgerAccountsResponse**](GetLedgerAccountsResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LedgerAccounts |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **ledger_accounts_delete**
> DeleteLedgerAccountResponse ledger_accounts_delete(id)

Delete Ledger Account

Delete Ledger Account

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.delete_ledger_account_response import DeleteLedgerAccountResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete Ledger Account
        api_response = api_instance.ledger_accounts_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->ledger_accounts_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Ledger Account
        api_response = api_instance.ledger_accounts_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->ledger_accounts_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**DeleteLedgerAccountResponse**](DeleteLedgerAccountResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LedgerAccount deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **ledger_accounts_one**
> GetLedgerAccountResponse ledger_accounts_one(id)

Get Ledger Account

Get Ledger Account

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.get_ledger_account_response import GetLedgerAccountResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get Ledger Account
        api_response = api_instance.ledger_accounts_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->ledger_accounts_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Ledger Account
        api_response = api_instance.ledger_accounts_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->ledger_accounts_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**GetLedgerAccountResponse**](GetLedgerAccountResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LedgerAccount |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **ledger_accounts_update**
> UpdateLedgerAccountResponse ledger_accounts_update(id, ledger_account)

Update Ledger Account

Update Ledger Account

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.ledger_account import LedgerAccount
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.update_ledger_account_response import UpdateLedgerAccountResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    ledger_account = LedgerAccount() # LedgerAccount | 
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update Ledger Account
        api_response = api_instance.ledger_accounts_update(id, ledger_account)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->ledger_accounts_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Ledger Account
        api_response = api_instance.ledger_accounts_update(id, ledger_account, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->ledger_accounts_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **ledger_account** | [**LedgerAccount**](LedgerAccount.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateLedgerAccountResponse**](UpdateLedgerAccountResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LedgerAccount updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **payments_add**
> CreatePaymentResponse payments_add(payment)

Create Payment

Create Payment

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.create_payment_response import CreatePaymentResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.payment import Payment
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    payment = Payment(
        currency=Currency("USD"),
        currency_rate=0.69,
        total_amount=49.99,
        reference="123456",
        payment_method="Credit Card",
        payment_method_reference="123456",
        accounts_receivable_account_type="Account",
        accounts_receivable_account_id="123456",
        account=LinkedLedgerAccount(
            id="123456",
            nominal_code="N091",
            code="453",
        ),
        transaction_date=dateutil_parser('2021-05-01T12:00:00Z'),
        customer=LinkedCustomer(
            id="12345",
            display_name="Windsurf Shop",
            name="Windsurf Shop",
        ),
        supplier=LinkedSupplier(
            id="12345",
            display_name="Windsurf Shop",
            address=Address(
                id="123",
                type="primary",
                string="25 Spring Street, Blackburn, VIC 3130",
                name="HQ US",
                line1="Main street",
                line2="apt #",
                line3="Suite #",
                line4="delivery instructions",
                street_number="25",
                city="San Francisco",
                state="CA",
                postal_code="94104",
                country="US",
                latitude="40.759211",
                longitude="-73.984638",
                county="Santa Clara",
                contact_name="Elon Musk",
                salutation="Mr",
                phone_number="111-111-1111",
                fax="122-111-1111",
                email="elon@musk.com",
                website="https://elonmusk.com",
                row_version="1-12345",
            ),
        ),
        reconciled=True,
        status="authorised",
        type="accounts_receivable",
        allocations=[
            PaymentAllocations(
                id="123456",
                type="invoice",
                amount=49.99,
            ),
        ],
        note="Some notes about this payment",
        row_version="1-12345",
        display_id="123456",
    ) # Payment | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Payment
        api_response = api_instance.payments_add(payment)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->payments_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Payment
        api_response = api_instance.payments_add(payment, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->payments_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment** | [**Payment**](Payment.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreatePaymentResponse**](CreatePaymentResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Payment created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **payments_all**
> GetPaymentsResponse payments_all()

List Payments

List Payments

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.get_payments_response import GetPaymentsResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of records to return (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Payments
        api_response = api_instance.payments_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->payments_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **limit** | **int**| Number of records to return | [optional] if omitted the server will use the default value of 20

### Return type

[**GetPaymentsResponse**](GetPaymentsResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payments |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **payments_delete**
> DeletePaymentResponse payments_delete(id)

Delete Payment

Delete Payment

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.delete_payment_response import DeletePaymentResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete Payment
        api_response = api_instance.payments_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->payments_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Payment
        api_response = api_instance.payments_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->payments_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**DeletePaymentResponse**](DeletePaymentResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **payments_one**
> GetPaymentResponse payments_one(id)

Get Payment

Get Payment

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.get_payment_response import GetPaymentResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get Payment
        api_response = api_instance.payments_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->payments_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Payment
        api_response = api_instance.payments_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->payments_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**GetPaymentResponse**](GetPaymentResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **payments_update**
> UpdatePaymentResponse payments_update(id, payment)

Update Payment

Update Payment

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.update_payment_response import UpdatePaymentResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.payment import Payment
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    payment = Payment(
        currency=Currency("USD"),
        currency_rate=0.69,
        total_amount=49.99,
        reference="123456",
        payment_method="Credit Card",
        payment_method_reference="123456",
        accounts_receivable_account_type="Account",
        accounts_receivable_account_id="123456",
        account=LinkedLedgerAccount(
            id="123456",
            nominal_code="N091",
            code="453",
        ),
        transaction_date=dateutil_parser('2021-05-01T12:00:00Z'),
        customer=LinkedCustomer(
            id="12345",
            display_name="Windsurf Shop",
            name="Windsurf Shop",
        ),
        supplier=LinkedSupplier(
            id="12345",
            display_name="Windsurf Shop",
            address=Address(
                id="123",
                type="primary",
                string="25 Spring Street, Blackburn, VIC 3130",
                name="HQ US",
                line1="Main street",
                line2="apt #",
                line3="Suite #",
                line4="delivery instructions",
                street_number="25",
                city="San Francisco",
                state="CA",
                postal_code="94104",
                country="US",
                latitude="40.759211",
                longitude="-73.984638",
                county="Santa Clara",
                contact_name="Elon Musk",
                salutation="Mr",
                phone_number="111-111-1111",
                fax="122-111-1111",
                email="elon@musk.com",
                website="https://elonmusk.com",
                row_version="1-12345",
            ),
        ),
        reconciled=True,
        status="authorised",
        type="accounts_receivable",
        allocations=[
            PaymentAllocations(
                id="123456",
                type="invoice",
                amount=49.99,
            ),
        ],
        note="Some notes about this payment",
        row_version="1-12345",
        display_id="123456",
    ) # Payment | 
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update Payment
        api_response = api_instance.payments_update(id, payment)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->payments_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Payment
        api_response = api_instance.payments_update(id, payment, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->payments_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **payment** | [**Payment**](Payment.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdatePaymentResponse**](UpdatePaymentResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment Updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **profit_and_loss_one**
> GetProfitAndLossResponse profit_and_loss_one()

Get Profit and Loss

Get Profit and Loss

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.profit_and_loss_filter import ProfitAndLossFilter
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.get_profit_and_loss_response import GetProfitAndLossResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    filter = ProfitAndLossFilter(
        customer_id="123abc",
        start_date="2021-01-01",
        end_date="2021-12-31",
    ) # ProfitAndLossFilter | Apply filters (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Profit and Loss
        api_response = api_instance.profit_and_loss_one(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, filter=filter)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->profit_and_loss_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **filter** | **ProfitAndLossFilter**| Apply filters | [optional]

### Return type

[**GetProfitAndLossResponse**](GetProfitAndLossResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Profit &amp; Loss Report |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **suppliers_add**
> CreateSupplierResponse suppliers_add(supplier)

Create Supplier

Create Supplier

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.create_supplier_response import CreateSupplierResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.supplier import Supplier
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    supplier = Supplier(
        company_name="SpaceX",
        display_name="Windsurf Shop",
        title="CEO",
        first_name="Elon",
        middle_name="D.",
        last_name="Musk",
        suffix="Jr.",
        addresses=[
            Address(
                id="123",
                type="primary",
                string="25 Spring Street, Blackburn, VIC 3130",
                name="HQ US",
                line1="Main street",
                line2="apt #",
                line3="Suite #",
                line4="delivery instructions",
                street_number="25",
                city="San Francisco",
                state="CA",
                postal_code="94104",
                country="US",
                latitude="40.759211",
                longitude="-73.984638",
                county="Santa Clara",
                contact_name="Elon Musk",
                salutation="Mr",
                phone_number="111-111-1111",
                fax="122-111-1111",
                email="elon@musk.com",
                website="https://elonmusk.com",
                row_version="1-12345",
            ),
        ],
        notes="Some notes about this supplier",
        phone_numbers=[
            PhoneNumber(
                id="12345",
                country_code="1",
                area_code="323",
                number="111-111-1111",
                extension="105",
                type="primary",
            ),
        ],
        emails=[
            Email(
                id="123",
                email="elon@musk.com",
                type="primary",
            ),
        ],
        websites=[
            Website(
                id="12345",
                url="http://example.com",
                type="primary",
            ),
        ],
        bank_accounts=[
            BankAccount(
                iban="CH2989144532982975332",
                bic="AUDSCHGGXXX",
                bsb_number="062-001",
                branch_identifier="001",
                bank_code="BNH",
                account_number="123465",
                account_name="SPACEX LLC",
                account_type="credit_card",
                currency=Currency("USD"),
            ),
        ],
        tax_rate=LinkedTaxRate(
            id="123456",
        ),
        tax_number="US123945459",
        currency=Currency("USD"),
        account=LinkedLedgerAccount(
            id="123456",
            nominal_code="N091",
            code="453",
        ),
        status="active",
        row_version="1-12345",
    ) # Supplier | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Supplier
        api_response = api_instance.suppliers_add(supplier)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->suppliers_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Supplier
        api_response = api_instance.suppliers_add(supplier, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->suppliers_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier** | [**Supplier**](Supplier.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateSupplierResponse**](CreateSupplierResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Supplier created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **suppliers_all**
> GetSuppliersResponse suppliers_all()

List Suppliers

List Suppliers

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.get_suppliers_response import GetSuppliersResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of records to return (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Suppliers
        api_response = api_instance.suppliers_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->suppliers_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **limit** | **int**| Number of records to return | [optional] if omitted the server will use the default value of 20

### Return type

[**GetSuppliersResponse**](GetSuppliersResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Suppliers |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **suppliers_delete**
> DeleteSupplierResponse suppliers_delete(id)

Delete Supplier

Delete Supplier

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.delete_supplier_response import DeleteSupplierResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete Supplier
        api_response = api_instance.suppliers_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->suppliers_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Supplier
        api_response = api_instance.suppliers_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->suppliers_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**DeleteSupplierResponse**](DeleteSupplierResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Supplier deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **suppliers_one**
> GetSupplierResponse suppliers_one(id)

Get Supplier

Get Supplier

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.get_supplier_response import GetSupplierResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get Supplier
        api_response = api_instance.suppliers_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->suppliers_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Supplier
        api_response = api_instance.suppliers_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->suppliers_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**GetSupplierResponse**](GetSupplierResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Supplier |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **suppliers_update**
> UpdateSupplierResponse suppliers_update(id, supplier)

Update Supplier

Update Supplier

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.update_supplier_response import UpdateSupplierResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.supplier import Supplier
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    supplier = Supplier(
        company_name="SpaceX",
        display_name="Windsurf Shop",
        title="CEO",
        first_name="Elon",
        middle_name="D.",
        last_name="Musk",
        suffix="Jr.",
        addresses=[
            Address(
                id="123",
                type="primary",
                string="25 Spring Street, Blackburn, VIC 3130",
                name="HQ US",
                line1="Main street",
                line2="apt #",
                line3="Suite #",
                line4="delivery instructions",
                street_number="25",
                city="San Francisco",
                state="CA",
                postal_code="94104",
                country="US",
                latitude="40.759211",
                longitude="-73.984638",
                county="Santa Clara",
                contact_name="Elon Musk",
                salutation="Mr",
                phone_number="111-111-1111",
                fax="122-111-1111",
                email="elon@musk.com",
                website="https://elonmusk.com",
                row_version="1-12345",
            ),
        ],
        notes="Some notes about this supplier",
        phone_numbers=[
            PhoneNumber(
                id="12345",
                country_code="1",
                area_code="323",
                number="111-111-1111",
                extension="105",
                type="primary",
            ),
        ],
        emails=[
            Email(
                id="123",
                email="elon@musk.com",
                type="primary",
            ),
        ],
        websites=[
            Website(
                id="12345",
                url="http://example.com",
                type="primary",
            ),
        ],
        bank_accounts=[
            BankAccount(
                iban="CH2989144532982975332",
                bic="AUDSCHGGXXX",
                bsb_number="062-001",
                branch_identifier="001",
                bank_code="BNH",
                account_number="123465",
                account_name="SPACEX LLC",
                account_type="credit_card",
                currency=Currency("USD"),
            ),
        ],
        tax_rate=LinkedTaxRate(
            id="123456",
        ),
        tax_number="US123945459",
        currency=Currency("USD"),
        account=LinkedLedgerAccount(
            id="123456",
            nominal_code="N091",
            code="453",
        ),
        status="active",
        row_version="1-12345",
    ) # Supplier | 
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update Supplier
        api_response = api_instance.suppliers_update(id, supplier)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->suppliers_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Supplier
        api_response = api_instance.suppliers_update(id, supplier, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->suppliers_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **supplier** | [**Supplier**](Supplier.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateSupplierResponse**](UpdateSupplierResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Supplier updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **tax_rates_add**
> CreateTaxRateResponse tax_rates_add(tax_rate)

Create Tax Rate

Create Tax Rate

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.create_tax_rate_response import CreateTaxRateResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.tax_rate import TaxRate
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    tax_rate = TaxRate(
        id="1234",
        name="GST on Purchases",
        code="ABN",
        description="Reduced rate GST Purchases",
        effective_tax_rate=10,
        total_tax_rate=10,
        tax_payable_account_id="123456",
        tax_remitted_account_id="123456",
        components=[
            None,
        ],
        type="NONE",
        report_tax_type="NONE",
        original_tax_rate_id="12345",
        status="active",
        row_version="1-12345",
    ) # TaxRate | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Tax Rate
        api_response = api_instance.tax_rates_add(tax_rate)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->tax_rates_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Tax Rate
        api_response = api_instance.tax_rates_add(tax_rate, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->tax_rates_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_rate** | [**TaxRate**](TaxRate.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateTaxRateResponse**](CreateTaxRateResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | TaxRate created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **tax_rates_all**
> GetTaxRatesResponse tax_rates_all()

List Tax Rates

List Tax Rates. Note: Not all connectors return the actual rate/percentage value. In this case, only the tax code or reference is returned. Connectors Affected: Quickbooks 

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.get_tax_rates_response import GetTaxRatesResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.tax_rates_filter import TaxRatesFilter
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of records to return (optional) if omitted the server will use the default value of 20
    filter = TaxRatesFilter(
        assets=True,
        equity=True,
        expenses=True,
        liabilities=True,
        revenue=True,
    ) # TaxRatesFilter | Apply filters (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Tax Rates
        api_response = api_instance.tax_rates_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, filter=filter)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->tax_rates_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **limit** | **int**| Number of records to return | [optional] if omitted the server will use the default value of 20
 **filter** | **TaxRatesFilter**| Apply filters | [optional]

### Return type

[**GetTaxRatesResponse**](GetTaxRatesResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TaxRates |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **tax_rates_delete**
> DeleteTaxRateResponse tax_rates_delete(id)

Delete Tax Rate

Delete Tax Rate

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.delete_tax_rate_response import DeleteTaxRateResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete Tax Rate
        api_response = api_instance.tax_rates_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->tax_rates_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Tax Rate
        api_response = api_instance.tax_rates_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->tax_rates_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**DeleteTaxRateResponse**](DeleteTaxRateResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TaxRates deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **tax_rates_one**
> GetTaxRateResponse tax_rates_one(id)

Get Tax Rate

Get Tax Rate. Note: Not all connectors return the actual rate/percentage value. In this case, only the tax code or reference is returned. Support will soon be added to return the actual rate/percentage by doing additional calls in the background to provide the full view of a given tax rate. Connectors Affected: Quickbooks 

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.get_tax_rate_response import GetTaxRateResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get Tax Rate
        api_response = api_instance.tax_rates_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->tax_rates_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Tax Rate
        api_response = api_instance.tax_rates_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->tax_rates_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**GetTaxRateResponse**](GetTaxRateResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TaxRate |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **tax_rates_update**
> UpdateTaxRateResponse tax_rates_update(id, tax_rate)

Update Tax Rate

Update Tax Rate

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import accounting_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.update_tax_rate_response import UpdateTaxRateResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.tax_rate import TaxRate
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    tax_rate = TaxRate(
        id="1234",
        name="GST on Purchases",
        code="ABN",
        description="Reduced rate GST Purchases",
        effective_tax_rate=10,
        total_tax_rate=10,
        tax_payable_account_id="123456",
        tax_remitted_account_id="123456",
        components=[
            None,
        ],
        type="NONE",
        report_tax_type="NONE",
        original_tax_rate_id="12345",
        status="active",
        row_version="1-12345",
    ) # TaxRate | 
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "x-apideck-app-id_example" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update Tax Rate
        api_response = api_instance.tax_rates_update(id, tax_rate)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->tax_rates_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Tax Rate
        api_response = api_instance.tax_rates_update(id, tax_rate, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->tax_rates_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **tax_rate** | [**TaxRate**](TaxRate.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateTaxRateResponse**](UpdateTaxRateResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TaxRate updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

