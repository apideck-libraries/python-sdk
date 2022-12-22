# apideck.ConnectorApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_resource_coverage_one**](ConnectorApi.md#api_resource_coverage_one) | **GET** /connector/apis/{id}/resources/{resource_id}/coverage | Get API Resource Coverage
[**api_resources_one**](ConnectorApi.md#api_resources_one) | **GET** /connector/apis/{id}/resources/{resource_id} | Get API Resource
[**apis_all**](ConnectorApi.md#apis_all) | **GET** /connector/apis | List APIs
[**apis_one**](ConnectorApi.md#apis_one) | **GET** /connector/apis/{id} | Get API
[**connector_docs_one**](ConnectorApi.md#connector_docs_one) | **GET** /connector/connectors/{id}/docs/{doc_id} | Get Connector Doc content
[**connector_resources_one**](ConnectorApi.md#connector_resources_one) | **GET** /connector/connectors/{id}/resources/{resource_id} | Get Connector Resource
[**connectors_all**](ConnectorApi.md#connectors_all) | **GET** /connector/connectors | List Connectors
[**connectors_one**](ConnectorApi.md#connectors_one) | **GET** /connector/connectors/{id} | Get Connector


# **api_resource_coverage_one**
> GetApiResourceCoverageResponse api_resource_coverage_one(id, resource_id)

Get API Resource Coverage

Get API Resource Coverage

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import connector_api
from apideck.model.get_api_resource_coverage_response import GetApiResourceCoverageResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
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
    api_instance = connector_api.ConnectorApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    resource_id = "resource_id_example" # str | ID of the resource you are acting upon.
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get API Resource Coverage
        api_response = api_instance.api_resource_coverage_one(id, resource_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling ConnectorApi->api_resource_coverage_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get API Resource Coverage
        api_response = api_instance.api_resource_coverage_one(id, resource_id, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling ConnectorApi->api_resource_coverage_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **resource_id** | **str**| ID of the resource you are acting upon. |
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

[**GetApiResourceCoverageResponse**](GetApiResourceCoverageResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ApiResources |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **api_resources_one**
> GetApiResourceResponse api_resources_one(id, resource_id)

Get API Resource

Get API Resource

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import connector_api
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.get_api_resource_response import GetApiResourceResponse
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
    api_instance = connector_api.ConnectorApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    resource_id = "resource_id_example" # str | ID of the resource you are acting upon.
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get API Resource
        api_response = api_instance.api_resources_one(id, resource_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling ConnectorApi->api_resources_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get API Resource
        api_response = api_instance.api_resources_one(id, resource_id, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling ConnectorApi->api_resources_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **resource_id** | **str**| ID of the resource you are acting upon. |
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

[**GetApiResourceResponse**](GetApiResourceResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ApiResources |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **apis_all**
> GetApisResponse apis_all()

List APIs

List APIs

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import connector_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.apis_filter import ApisFilter
from apideck.model.get_apis_response import GetApisResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
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
    api_instance = connector_api.ConnectorApi(api_client)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of records to return (optional) if omitted the server will use the default value of 20
    filter = ApisFilter(
        status=ApiStatus("live"),
    ) # ApisFilter | Apply filters (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List APIs
        api_response = api_instance.apis_all(app_id=app_id, cursor=cursor, limit=limit, filter=filter)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling ConnectorApi->apis_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The ID of your Unify application | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **limit** | **int**| Number of records to return | [optional] if omitted the server will use the default value of 20
 **filter** | **ApisFilter**| Apply filters | [optional]

### Return type

[**GetApisResponse**](GetApisResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Apis |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **apis_one**
> GetApiResponse apis_one(id)

Get API

Get API

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import connector_api
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.get_api_response import GetApiResponse
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
    api_instance = connector_api.ConnectorApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get API
        api_response = api_instance.apis_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling ConnectorApi->apis_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get API
        api_response = api_instance.apis_one(id, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling ConnectorApi->apis_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

[**GetApiResponse**](GetApiResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Apis |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **connector_docs_one**
> str connector_docs_one(id, doc_id)

Get Connector Doc content

Get Connector Doc content

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import connector_api
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
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
    api_instance = connector_api.ConnectorApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    doc_id = "doc_id_example" # str | ID of the Doc
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Connector Doc content
        api_response = api_instance.connector_docs_one(id, doc_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling ConnectorApi->connector_docs_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Connector Doc content
        api_response = api_instance.connector_docs_one(id, doc_id, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling ConnectorApi->connector_docs_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **doc_id** | **str**| ID of the Doc |
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

**str**

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/markdown, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connectors |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **connector_resources_one**
> GetConnectorResourceResponse connector_resources_one(id, resource_id)

Get Connector Resource

Get Connector Resource

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import connector_api
from apideck.model.get_connector_resource_response import GetConnectorResourceResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unified_api_id import UnifiedApiId
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
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
    api_instance = connector_api.ConnectorApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    resource_id = "resource_id_example" # str | ID of the resource you are acting upon.
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    unified_api = UnifiedApiId("crm") # UnifiedApiId | Specify unified API for the connector resource. This is useful when a resource appears in multiple APIs (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Connector Resource
        api_response = api_instance.connector_resources_one(id, resource_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling ConnectorApi->connector_resources_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Connector Resource
        api_response = api_instance.connector_resources_one(id, resource_id, app_id=app_id, unified_api=unified_api)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling ConnectorApi->connector_resources_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **resource_id** | **str**| ID of the resource you are acting upon. |
 **app_id** | **str**| The ID of your Unify application | [optional]
 **unified_api** | **UnifiedApiId**| Specify unified API for the connector resource. This is useful when a resource appears in multiple APIs | [optional]

### Return type

[**GetConnectorResourceResponse**](GetConnectorResourceResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConnectorResources |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **connectors_all**
> GetConnectorsResponse connectors_all()

List Connectors

List Connectors

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import connector_api
from apideck.model.connectors_filter import ConnectorsFilter
from apideck.model.get_connectors_response import GetConnectorsResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
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
    api_instance = connector_api.ConnectorApi(api_client)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of records to return (optional) if omitted the server will use the default value of 20
    filter = ConnectorsFilter(
        unified_api=UnifiedApiId("crm"),
        status=ConnectorStatus("live"),
    ) # ConnectorsFilter | Apply filters (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Connectors
        api_response = api_instance.connectors_all(app_id=app_id, cursor=cursor, limit=limit, filter=filter)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling ConnectorApi->connectors_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The ID of your Unify application | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **limit** | **int**| Number of records to return | [optional] if omitted the server will use the default value of 20
 **filter** | **ConnectorsFilter**| Apply filters | [optional]

### Return type

[**GetConnectorsResponse**](GetConnectorsResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connectors |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **connectors_one**
> GetConnectorResponse connectors_one(id)

Get Connector

Get Connector

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import connector_api
from apideck.model.get_connector_response import GetConnectorResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
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
    api_instance = connector_api.ConnectorApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Connector
        api_response = api_instance.connectors_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling ConnectorApi->connectors_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Connector
        api_response = api_instance.connectors_one(id, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling ConnectorApi->connectors_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

[**GetConnectorResponse**](GetConnectorResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connectors |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

