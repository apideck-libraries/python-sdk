# apideck.EcommerceApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_all**](EcommerceApi.md#customers_all) | **GET** /ecommerce/customers | List Customers
[**customers_one**](EcommerceApi.md#customers_one) | **GET** /ecommerce/customers/{id} | Get Customer
[**orders_all**](EcommerceApi.md#orders_all) | **GET** /ecommerce/orders | List Orders
[**orders_one**](EcommerceApi.md#orders_one) | **GET** /ecommerce/orders/{id} | Get Order
[**products_all**](EcommerceApi.md#products_all) | **GET** /ecommerce/products | List Products
[**products_one**](EcommerceApi.md#products_one) | **GET** /ecommerce/products/{id} | Get Product
[**stores_one**](EcommerceApi.md#stores_one) | **GET** /ecommerce/store | Get Store


# **customers_all**
> GetEcommerceCustomersResponse customers_all()

List Customers

List Customers

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import ecommerce_api
from apideck.model.pass_through_query import PassThroughQuery
from apideck.model.get_ecommerce_customers_response import GetEcommerceCustomersResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.ecommerce_customers_filter import EcommerceCustomersFilter
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
    api_instance = ecommerce_api.EcommerceApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of results to return. Minimum 1, Maximum 200, Default 20 (optional) if omitted the server will use the default value of 20
    filter = EcommerceCustomersFilter(
        email="elon@musk.com",
        phone_number="111-111-1111",
    ) # EcommerceCustomersFilter | Apply filters (optional)
    pass_through = PassThroughQuery() # PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Customers
        api_response = api_instance.customers_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, filter=filter, pass_through=pass_through, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling EcommerceApi->customers_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **limit** | **int**| Number of results to return. Minimum 1, Maximum 200, Default 20 | [optional] if omitted the server will use the default value of 20
 **filter** | **EcommerceCustomersFilter**| Apply filters | [optional]
 **pass_through** | **PassThroughQuery**| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional]
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

[**GetEcommerceCustomersResponse**](GetEcommerceCustomersResponse.md)

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
> GetEcommerceCustomerResponse customers_one(id)

Get Customer

Get Customer

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import ecommerce_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.get_ecommerce_customer_response import GetEcommerceCustomerResponse
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
    api_instance = ecommerce_api.EcommerceApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Customer
        api_response = api_instance.customers_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling EcommerceApi->customers_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Customer
        api_response = api_instance.customers_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling EcommerceApi->customers_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

[**GetEcommerceCustomerResponse**](GetEcommerceCustomerResponse.md)

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

# **orders_all**
> GetEcommerceOrdersResponse orders_all()

List Orders

List Orders

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import ecommerce_api
from apideck.model.pass_through_query import PassThroughQuery
from apideck.model.ecommerce_orders_filter import EcommerceOrdersFilter
from apideck.model.orders_sort import OrdersSort
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.get_ecommerce_orders_response import GetEcommerceOrdersResponse
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
    api_instance = ecommerce_api.EcommerceApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of results to return. Minimum 1, Maximum 200, Default 20 (optional) if omitted the server will use the default value of 20
    filter = EcommerceOrdersFilter(
        email="elon@musk.com",
        customer_id="123",
        updated_since="2020-09-30T07:43:32.000Z",
        created_since="2020-09-30T07:43:32.000Z",
    ) # EcommerceOrdersFilter | Apply filters (optional)
    sort = OrdersSort(
        by="created_at",
        direction=SortDirection("asc"),
    ) # OrdersSort | Apply sorting (optional)
    pass_through = PassThroughQuery() # PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Orders
        api_response = api_instance.orders_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, filter=filter, sort=sort, pass_through=pass_through, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling EcommerceApi->orders_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **limit** | **int**| Number of results to return. Minimum 1, Maximum 200, Default 20 | [optional] if omitted the server will use the default value of 20
 **filter** | **EcommerceOrdersFilter**| Apply filters | [optional]
 **sort** | **OrdersSort**| Apply sorting | [optional]
 **pass_through** | **PassThroughQuery**| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional]
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

[**GetEcommerceOrdersResponse**](GetEcommerceOrdersResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Orders |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **orders_one**
> GetEcommerceOrderResponse orders_one(id)

Get Order

Get Order

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import ecommerce_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.get_ecommerce_order_response import GetEcommerceOrderResponse
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
    api_instance = ecommerce_api.EcommerceApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Order
        api_response = api_instance.orders_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling EcommerceApi->orders_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Order
        api_response = api_instance.orders_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling EcommerceApi->orders_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

[**GetEcommerceOrderResponse**](GetEcommerceOrderResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Orders |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **products_all**
> GetProductsResponse products_all()

List Products

List Products

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import ecommerce_api
from apideck.model.pass_through_query import PassThroughQuery
from apideck.model.get_products_response import GetProductsResponse
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
    api_instance = ecommerce_api.EcommerceApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of results to return. Minimum 1, Maximum 200, Default 20 (optional) if omitted the server will use the default value of 20
    pass_through = PassThroughQuery() # PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Products
        api_response = api_instance.products_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, pass_through=pass_through, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling EcommerceApi->products_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **limit** | **int**| Number of results to return. Minimum 1, Maximum 200, Default 20 | [optional] if omitted the server will use the default value of 20
 **pass_through** | **PassThroughQuery**| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional]
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

[**GetProductsResponse**](GetProductsResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Products |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **products_one**
> GetProductResponse products_one(id)

Get Product

Get Product

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import ecommerce_api
from apideck.model.get_product_response import GetProductResponse
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
    api_instance = ecommerce_api.EcommerceApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Product
        api_response = api_instance.products_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling EcommerceApi->products_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Product
        api_response = api_instance.products_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling EcommerceApi->products_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

[**GetProductResponse**](GetProductResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Products |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **stores_one**
> GetStoreResponse stores_one()

Get Store

Get Store

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import ecommerce_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.get_store_response import GetStoreResponse
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
    api_instance = ecommerce_api.EcommerceApi(api_client)
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Store
        api_response = api_instance.stores_one(consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling EcommerceApi->stores_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

[**GetStoreResponse**](GetStoreResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stores |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

