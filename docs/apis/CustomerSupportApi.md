# apideck.CustomerSupportApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_add**](CustomerSupportApi.md#customers_add) | **POST** /customer-support/customers | Create Customer Support Customer
[**customers_all**](CustomerSupportApi.md#customers_all) | **GET** /customer-support/customers | List Customer Support Customers
[**customers_delete**](CustomerSupportApi.md#customers_delete) | **DELETE** /customer-support/customers/{id} | Delete Customer Support Customer
[**customers_one**](CustomerSupportApi.md#customers_one) | **GET** /customer-support/customers/{id} | Get Customer Support Customer
[**customers_update**](CustomerSupportApi.md#customers_update) | **PATCH** /customer-support/customers/{id} | Update Customer Support Customer


# **customers_add**
> CreateCustomerSupportCustomerResponse customers_add(customer_support_customer)

Create Customer Support Customer

Create Customer Support Customer

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import customer_support_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.create_customer_support_customer_response import CreateCustomerSupportCustomerResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.customer_support_customer import CustomerSupportCustomer
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
    api_instance = customer_support_api.CustomerSupportApi(api_client)
    customer_support_customer = CustomerSupportCustomer(
        company_name="SpaceX",
        first_name="Elon",
        last_name="Musk",
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
        tax_number="US123945459",
        currency=Currency("USD"),
        bank_accounts=BankAccount(
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
        status="active",
    ) # CustomerSupportCustomer | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Customer Support Customer
        api_response = api_instance.customers_add(customer_support_customer)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CustomerSupportApi->customers_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Customer Support Customer
        api_response = api_instance.customers_add(customer_support_customer, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CustomerSupportApi->customers_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_support_customer** | [**CustomerSupportCustomer**](CustomerSupportCustomer.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateCustomerSupportCustomerResponse**](CreateCustomerSupportCustomerResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CustomerSupportCustomers |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **customers_all**
> GetCustomerSupportCustomersResponse customers_all()

List Customer Support Customers

List Customer Support Customers

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import customer_support_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.get_customer_support_customers_response import GetCustomerSupportCustomersResponse
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
    api_instance = customer_support_api.CustomerSupportApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of records to return (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Customer Support Customers
        api_response = api_instance.customers_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CustomerSupportApi->customers_all: %s\n" % e)
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

[**GetCustomerSupportCustomersResponse**](GetCustomerSupportCustomersResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CustomerSupportCustomers |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **customers_delete**
> DeleteCustomerSupportCustomerResponse customers_delete(id)

Delete Customer Support Customer

Delete Customer Support Customer

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import customer_support_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.delete_customer_support_customer_response import DeleteCustomerSupportCustomerResponse
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
    api_instance = customer_support_api.CustomerSupportApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete Customer Support Customer
        api_response = api_instance.customers_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CustomerSupportApi->customers_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Customer Support Customer
        api_response = api_instance.customers_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CustomerSupportApi->customers_delete: %s\n" % e)
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

[**DeleteCustomerSupportCustomerResponse**](DeleteCustomerSupportCustomerResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CustomerSupportCustomers |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **customers_one**
> GetCustomerSupportCustomerResponse customers_one(id)

Get Customer Support Customer

Get Customer Support Customer

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import customer_support_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.get_customer_support_customer_response import GetCustomerSupportCustomerResponse
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
    api_instance = customer_support_api.CustomerSupportApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get Customer Support Customer
        api_response = api_instance.customers_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CustomerSupportApi->customers_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Customer Support Customer
        api_response = api_instance.customers_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CustomerSupportApi->customers_one: %s\n" % e)
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

[**GetCustomerSupportCustomerResponse**](GetCustomerSupportCustomerResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CustomerSupportCustomers |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **customers_update**
> UpdateCustomerSupportCustomerResponse customers_update(id, customer_support_customer)

Update Customer Support Customer

Update Customer Support Customer

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import customer_support_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.update_customer_support_customer_response import UpdateCustomerSupportCustomerResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.customer_support_customer import CustomerSupportCustomer
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
    api_instance = customer_support_api.CustomerSupportApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    customer_support_customer = CustomerSupportCustomer(
        company_name="SpaceX",
        first_name="Elon",
        last_name="Musk",
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
        tax_number="US123945459",
        currency=Currency("USD"),
        bank_accounts=BankAccount(
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
        status="active",
    ) # CustomerSupportCustomer | 
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update Customer Support Customer
        api_response = api_instance.customers_update(id, customer_support_customer)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CustomerSupportApi->customers_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Customer Support Customer
        api_response = api_instance.customers_update(id, customer_support_customer, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CustomerSupportApi->customers_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **customer_support_customer** | [**CustomerSupportCustomer**](CustomerSupportCustomer.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateCustomerSupportCustomerResponse**](UpdateCustomerSupportCustomerResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CustomerSupportCustomers |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

