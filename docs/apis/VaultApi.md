# apideck.VaultApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connection_custom_mappings_all**](VaultApi.md#connection_custom_mappings_all) | **GET** /vault/connections/{unified_api}/{service_id}/{resource}/custom-mappings | List connection custom mappings
[**connection_settings_all**](VaultApi.md#connection_settings_all) | **GET** /vault/connections/{unified_api}/{service_id}/{resource}/config | Get resource settings
[**connection_settings_update**](VaultApi.md#connection_settings_update) | **PATCH** /vault/connections/{unified_api}/{service_id}/{resource}/config | Update settings
[**connections_all**](VaultApi.md#connections_all) | **GET** /vault/connections | Get all connections
[**connections_delete**](VaultApi.md#connections_delete) | **DELETE** /vault/connections/{unified_api}/{service_id} | Deletes a connection
[**connections_import**](VaultApi.md#connections_import) | **POST** /vault/connections/{unified_api}/{service_id}/import | Import connection
[**connections_one**](VaultApi.md#connections_one) | **GET** /vault/connections/{unified_api}/{service_id} | Get connection
[**connections_token**](VaultApi.md#connections_token) | **POST** /vault/connections/{unified_api}/{service_id}/token | Authorize Access Token
[**connections_update**](VaultApi.md#connections_update) | **PATCH** /vault/connections/{unified_api}/{service_id} | Update connection
[**consumer_request_counts_all**](VaultApi.md#consumer_request_counts_all) | **GET** /vault/consumers/{consumer_id}/stats | Consumer request counts
[**consumers_add**](VaultApi.md#consumers_add) | **POST** /vault/consumers | Create consumer
[**consumers_all**](VaultApi.md#consumers_all) | **GET** /vault/consumers | Get all consumers
[**consumers_delete**](VaultApi.md#consumers_delete) | **DELETE** /vault/consumers/{consumer_id} | Delete consumer
[**consumers_one**](VaultApi.md#consumers_one) | **GET** /vault/consumers/{consumer_id} | Get consumer
[**consumers_update**](VaultApi.md#consumers_update) | **PATCH** /vault/consumers/{consumer_id} | Update consumer
[**custom_fields_all**](VaultApi.md#custom_fields_all) | **GET** /vault/connections/{unified_api}/{service_id}/{resource}/custom-fields | Get resource custom fields
[**custom_mappings_all**](VaultApi.md#custom_mappings_all) | **GET** /vault/custom-mappings/{unified_api}/{service_id} | List custom mappings
[**logs_all**](VaultApi.md#logs_all) | **GET** /vault/logs | Get all consumer request logs
[**sessions_create**](VaultApi.md#sessions_create) | **POST** /vault/sessions | Create Session
[**validate_connection_state**](VaultApi.md#validate_connection_state) | **POST** /vault/connections/{unified_api}/{service_id}/validate | Validate Connection State


# **connection_custom_mappings_all**
> GetCustomMappingsResponse connection_custom_mappings_all(unified_api, service_id, resource)

List connection custom mappings

This endpoint returns a list of custom mappings for a connection.

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.get_custom_mappings_response import GetCustomMappingsResponse
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
    api_instance = vault_api.VaultApi(api_client)
    unified_api = "crm" # str | Unified API
    service_id = "pipedrive" # str | Service ID of the resource to return
    resource = "leads" # str | Name of the resource (plural)
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    resource_id = "1234" # str | This is the id of the resource you want to fetch when listing custom fields. For example, if you want to fetch custom fields for a specific contact, you would use the contact id. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List connection custom mappings
        api_response = api_instance.connection_custom_mappings_all(unified_api, service_id, resource)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->connection_custom_mappings_all: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List connection custom mappings
        api_response = api_instance.connection_custom_mappings_all(unified_api, service_id, resource, consumer_id=consumer_id, app_id=app_id, resource_id=resource_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->connection_custom_mappings_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unified_api** | **str**| Unified API |
 **service_id** | **str**| Service ID of the resource to return |
 **resource** | **str**| Name of the resource (plural) |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **resource_id** | **str**| This is the id of the resource you want to fetch when listing custom fields. For example, if you want to fetch custom fields for a specific contact, you would use the contact id. | [optional]

### Return type

[**GetCustomMappingsResponse**](GetCustomMappingsResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom mapping |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **connection_settings_all**
> GetConnectionResponse connection_settings_all(unified_api, service_id, resource)

Get resource settings

This endpoint returns custom settings and their defaults required by connection for a given resource. 

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
from apideck.model.get_connection_response import GetConnectionResponse
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
    api_instance = vault_api.VaultApi(api_client)
    unified_api = "crm" # str | Unified API
    service_id = "pipedrive" # str | Service ID of the resource to return
    resource = "leads" # str | Name of the resource (plural)
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get resource settings
        api_response = api_instance.connection_settings_all(unified_api, service_id, resource)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->connection_settings_all: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get resource settings
        api_response = api_instance.connection_settings_all(unified_api, service_id, resource, consumer_id=consumer_id, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->connection_settings_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unified_api** | **str**| Unified API |
 **service_id** | **str**| Service ID of the resource to return |
 **resource** | **str**| Name of the resource (plural) |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

[**GetConnectionResponse**](GetConnectionResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **connection_settings_update**
> UpdateConnectionResponse connection_settings_update(service_id, unified_api, resource, connection)

Update settings

Update default values for a connection's resource settings

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
from apideck.model.connection import Connection
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.update_connection_response import UpdateConnectionResponse
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
    api_instance = vault_api.VaultApi(api_client)
    service_id = "pipedrive" # str | Service ID of the resource to return
    unified_api = "crm" # str | Unified API
    resource = "leads" # str | Name of the resource (plural)
    connection = Connection(
        enabled=True,
        settings={},
        metadata={},
        configuration=[
            ConnectionConfiguration(
                resource="leads",
                defaults=[
                    ConnectionDefaults(
                        id="ProductInterest",
                        options=[
                            FormFieldOption(None),
                        ],
                        value=None,
                    ),
                ],
            ),
        ],
        custom_mappings=[
            CustomMapping(
                value="$.root.training.first_aid",
            ),
        ],
    ) # Connection | Fields that need to be updated on the resource
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update settings
        api_response = api_instance.connection_settings_update(service_id, unified_api, resource, connection)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->connection_settings_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update settings
        api_response = api_instance.connection_settings_update(service_id, unified_api, resource, connection, consumer_id=consumer_id, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->connection_settings_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Service ID of the resource to return |
 **unified_api** | **str**| Unified API |
 **resource** | **str**| Name of the resource (plural) |
 **connection** | [**Connection**](Connection.md)| Fields that need to be updated on the resource |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

[**UpdateConnectionResponse**](UpdateConnectionResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **connections_all**
> GetConnectionsResponse connections_all()

Get all connections

This endpoint includes all the configured integrations and contains the required assets to build an integrations page where your users can install integrations. OAuth2 supported integrations will contain authorize and revoke links to handle the authentication flows. 

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
from apideck.model.get_connections_response import GetConnectionsResponse
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
    api_instance = vault_api.VaultApi(api_client)
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    api = "crm" # str | Scope results to Unified API (optional)
    configured = True # bool | Scopes results to connections that have been configured or not (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all connections
        api_response = api_instance.connections_all(consumer_id=consumer_id, app_id=app_id, api=api, configured=configured)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->connections_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **api** | **str**| Scope results to Unified API | [optional]
 **configured** | **bool**| Scopes results to connections that have been configured or not | [optional]

### Return type

[**GetConnectionsResponse**](GetConnectionsResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connections |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **connections_delete**
> connections_delete(service_id, unified_api)

Deletes a connection

Deletes a connection

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
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
    api_instance = vault_api.VaultApi(api_client)
    service_id = "pipedrive" # str | Service ID of the resource to return
    unified_api = "crm" # str | Unified API
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes a connection
        api_instance.connections_delete(service_id, unified_api)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->connections_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes a connection
        api_instance.connections_delete(service_id, unified_api, consumer_id=consumer_id, app_id=app_id)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->connections_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Service ID of the resource to return |
 **unified_api** | **str**| Unified API |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

void (empty response body)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **connections_import**
> CreateConnectionResponse connections_import(service_id, unified_api, connection_import_data)

Import connection

Import an authorized connection. 

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
from apideck.model.connection_import_data import ConnectionImportData
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.create_connection_response import CreateConnectionResponse
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
    api_instance = vault_api.VaultApi(api_client)
    service_id = "pipedrive" # str | Service ID of the resource to return
    unified_api = "crm" # str | Unified API
    connection_import_data = ConnectionImportData(
        credentials=ConnectionImportDataCredentials(
            refresh_token="1234567890abcdefghijklmnopqrstuvwxyz",
            access_token="1234567890abcdefghijklmnopqrstuvwxyz",
            issued_at=dateutil_parser('2020-01-01T00:00:00Z'),
            expires_in=3600,
        ),
        settings={},
        metadata={},
    ) # ConnectionImportData | Fields that need to be persisted on the resource
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Import connection
        api_response = api_instance.connections_import(service_id, unified_api, connection_import_data)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->connections_import: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import connection
        api_response = api_instance.connections_import(service_id, unified_api, connection_import_data, consumer_id=consumer_id, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->connections_import: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Service ID of the resource to return |
 **unified_api** | **str**| Unified API |
 **connection_import_data** | [**ConnectionImportData**](ConnectionImportData.md)| Fields that need to be persisted on the resource |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

[**CreateConnectionResponse**](CreateConnectionResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **connections_one**
> GetConnectionResponse connections_one(service_id, unified_api)

Get connection

Get a connection

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
from apideck.model.get_connection_response import GetConnectionResponse
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
    api_instance = vault_api.VaultApi(api_client)
    service_id = "pipedrive" # str | Service ID of the resource to return
    unified_api = "crm" # str | Unified API
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get connection
        api_response = api_instance.connections_one(service_id, unified_api)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->connections_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get connection
        api_response = api_instance.connections_one(service_id, unified_api, consumer_id=consumer_id, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->connections_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Service ID of the resource to return |
 **unified_api** | **str**| Unified API |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

[**GetConnectionResponse**](GetConnectionResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **connections_token**
> GetConnectionResponse connections_token(service_id, unified_api)

Authorize Access Token

Triggers exchanging persisted connection credentials for an access token and store it in Vault. Currently supported for connections with the `client_credentials` or `password` OAuth grant type.  Note:   - Do not include any credentials in the request body. This operation does not persist changes, but only triggers the exchange of persisted connection credentials for an access token.   - The access token will not be returned in the response. A 200 response code indicates the authorization was successful and that a valid access token was stored on the connection.   - The access token will be used for subsequent API requests. 

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
from apideck.model.get_connection_response import GetConnectionResponse
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
    api_instance = vault_api.VaultApi(api_client)
    service_id = "pipedrive" # str | Service ID of the resource to return
    unified_api = "crm" # str | Unified API
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    body = {} # dict |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Authorize Access Token
        api_response = api_instance.connections_token(service_id, unified_api)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->connections_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Authorize Access Token
        api_response = api_instance.connections_token(service_id, unified_api, consumer_id=consumer_id, app_id=app_id, body=body)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->connections_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Service ID of the resource to return |
 **unified_api** | **str**| Unified API |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **body** | **dict**|  | [optional]

### Return type

[**GetConnectionResponse**](GetConnectionResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **connections_update**
> UpdateConnectionResponse connections_update(service_id, unified_api, connection)

Update connection

Update a connection

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
from apideck.model.connection import Connection
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.update_connection_response import UpdateConnectionResponse
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
    api_instance = vault_api.VaultApi(api_client)
    service_id = "pipedrive" # str | Service ID of the resource to return
    unified_api = "crm" # str | Unified API
    connection = Connection(
        enabled=True,
        settings={},
        metadata={},
        configuration=[
            ConnectionConfiguration(
                resource="leads",
                defaults=[
                    ConnectionDefaults(
                        id="ProductInterest",
                        options=[
                            FormFieldOption(None),
                        ],
                        value=None,
                    ),
                ],
            ),
        ],
        custom_mappings=[
            CustomMapping(
                value="$.root.training.first_aid",
            ),
        ],
    ) # Connection | Fields that need to be updated on the resource
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update connection
        api_response = api_instance.connections_update(service_id, unified_api, connection)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->connections_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update connection
        api_response = api_instance.connections_update(service_id, unified_api, connection, consumer_id=consumer_id, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->connections_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Service ID of the resource to return |
 **unified_api** | **str**| Unified API |
 **connection** | [**Connection**](Connection.md)| Fields that need to be updated on the resource |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

[**UpdateConnectionResponse**](UpdateConnectionResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **consumer_request_counts_all**
> ConsumerRequestCountsInDateRangeResponse consumer_request_counts_all(consumer_id, start_datetime, end_datetime)

Consumer request counts

Get consumer request counts within a given datetime range. 

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.consumer_request_counts_in_date_range_response import ConsumerRequestCountsInDateRangeResponse
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
    api_instance = vault_api.VaultApi(api_client)
    consumer_id = "test_user_id" # str | ID of the consumer to return
    start_datetime = "2021-05-01T12:00:00.000Z" # str | Scopes results to requests that happened after datetime
    end_datetime = "2021-05-30T12:00:00.000Z" # str | Scopes results to requests that happened before datetime
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Consumer request counts
        api_response = api_instance.consumer_request_counts_all(consumer_id, start_datetime, end_datetime)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->consumer_request_counts_all: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Consumer request counts
        api_response = api_instance.consumer_request_counts_all(consumer_id, start_datetime, end_datetime, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->consumer_request_counts_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**| ID of the consumer to return |
 **start_datetime** | **str**| Scopes results to requests that happened after datetime |
 **end_datetime** | **str**| Scopes results to requests that happened before datetime |
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

[**ConsumerRequestCountsInDateRangeResponse**](ConsumerRequestCountsInDateRangeResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consumers Request Counts within Date Range |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **consumers_add**
> CreateConsumerResponse consumers_add(consumer)

Create consumer

Create a consumer

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
from apideck.model.create_consumer_response import CreateConsumerResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.consumer import Consumer
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
    api_instance = vault_api.VaultApi(api_client)
    consumer = Consumer(
        consumer_id="test_consumer_id",
        metadata=ConsumerMetadata(
            account_name="SpaceX",
            user_name="Elon Musk",
            email="elon@musk.com",
            image="https://www.spacex.com/static/images/share.jpg",
        ),
    ) # Consumer | 
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create consumer
        api_response = api_instance.consumers_add(consumer)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->consumers_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create consumer
        api_response = api_instance.consumers_add(consumer, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->consumers_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer** | [**Consumer**](Consumer.md)|  |
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

[**CreateConsumerResponse**](CreateConsumerResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consumer created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **consumers_all**
> GetConsumersResponse consumers_all()

Get all consumers

This endpoint includes all application consumers, along with an aggregated count of requests made. 

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.get_consumers_response import GetConsumersResponse
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
    api_instance = vault_api.VaultApi(api_client)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of results to return. Minimum 1, Maximum 200, Default 20 (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all consumers
        api_response = api_instance.consumers_all(app_id=app_id, cursor=cursor, limit=limit)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->consumers_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The ID of your Unify application | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **limit** | **int**| Number of results to return. Minimum 1, Maximum 200, Default 20 | [optional] if omitted the server will use the default value of 20

### Return type

[**GetConsumersResponse**](GetConsumersResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consumers |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **consumers_delete**
> DeleteConsumerResponse consumers_delete(consumer_id)

Delete consumer

Delete consumer and all their connections, including credentials.

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.delete_consumer_response import DeleteConsumerResponse
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
    api_instance = vault_api.VaultApi(api_client)
    consumer_id = "test_user_id" # str | ID of the consumer to return
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete consumer
        api_response = api_instance.consumers_delete(consumer_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->consumers_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete consumer
        api_response = api_instance.consumers_delete(consumer_id, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->consumers_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**| ID of the consumer to return |
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

[**DeleteConsumerResponse**](DeleteConsumerResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consumer deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **consumers_one**
> GetConsumerResponse consumers_one(consumer_id)

Get consumer

Consumer detail including their aggregated counts with the connections they have authorized. 

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.get_consumer_response import GetConsumerResponse
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
    api_instance = vault_api.VaultApi(api_client)
    consumer_id = "test_user_id" # str | ID of the consumer to return
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get consumer
        api_response = api_instance.consumers_one(consumer_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->consumers_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get consumer
        api_response = api_instance.consumers_one(consumer_id, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->consumers_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**| ID of the consumer to return |
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

[**GetConsumerResponse**](GetConsumerResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consumer |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **consumers_update**
> UpdateConsumerResponse consumers_update(consumer_id, update_consumer_request)

Update consumer

Update consumer metadata such as name and email.

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.update_consumer_request import UpdateConsumerRequest
from apideck.model.update_consumer_response import UpdateConsumerResponse
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
    api_instance = vault_api.VaultApi(api_client)
    consumer_id = "test_user_id" # str | ID of the consumer to return
    update_consumer_request = UpdateConsumerRequest(
        metadata=ConsumerMetadata(
            account_name="SpaceX",
            user_name="Elon Musk",
            email="elon@musk.com",
            image="https://www.spacex.com/static/images/share.jpg",
        ),
    ) # UpdateConsumerRequest | 
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update consumer
        api_response = api_instance.consumers_update(consumer_id, update_consumer_request)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->consumers_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update consumer
        api_response = api_instance.consumers_update(consumer_id, update_consumer_request, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->consumers_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**| ID of the consumer to return |
 **update_consumer_request** | [**UpdateConsumerRequest**](UpdateConsumerRequest.md)|  |
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

[**UpdateConsumerResponse**](UpdateConsumerResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consumer updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **custom_fields_all**
> GetCustomFieldsResponse custom_fields_all(unified_api, service_id, resource)

Get resource custom fields

This endpoint returns an custom fields on a connection resource. 

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
from apideck.model.get_custom_fields_response import GetCustomFieldsResponse
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
    api_instance = vault_api.VaultApi(api_client)
    unified_api = "crm" # str | Unified API
    service_id = "pipedrive" # str | Service ID of the resource to return
    resource = "leads" # str | Name of the resource (plural)
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    resource_id = "1234" # str | This is the id of the resource you want to fetch when listing custom fields. For example, if you want to fetch custom fields for a specific contact, you would use the contact id. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get resource custom fields
        api_response = api_instance.custom_fields_all(unified_api, service_id, resource)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->custom_fields_all: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get resource custom fields
        api_response = api_instance.custom_fields_all(unified_api, service_id, resource, consumer_id=consumer_id, app_id=app_id, resource_id=resource_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->custom_fields_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unified_api** | **str**| Unified API |
 **service_id** | **str**| Service ID of the resource to return |
 **resource** | **str**| Name of the resource (plural) |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **resource_id** | **str**| This is the id of the resource you want to fetch when listing custom fields. For example, if you want to fetch custom fields for a specific contact, you would use the contact id. | [optional]

### Return type

[**GetCustomFieldsResponse**](GetCustomFieldsResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom mapping |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **custom_mappings_all**
> GetCustomMappingsResponse custom_mappings_all(unified_api, service_id)

List custom mappings

This endpoint returns a list of custom mappings.

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.get_custom_mappings_response import GetCustomMappingsResponse
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
    api_instance = vault_api.VaultApi(api_client)
    unified_api = "crm" # str | Unified API
    service_id = "pipedrive" # str | Service ID of the resource to return
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # List custom mappings
        api_response = api_instance.custom_mappings_all(unified_api, service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->custom_mappings_all: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List custom mappings
        api_response = api_instance.custom_mappings_all(unified_api, service_id, consumer_id=consumer_id, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->custom_mappings_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unified_api** | **str**| Unified API |
 **service_id** | **str**| Service ID of the resource to return |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

[**GetCustomMappingsResponse**](GetCustomMappingsResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom mapping |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **logs_all**
> GetLogsResponse logs_all()

Get all consumer request logs

This endpoint includes all consumer request logs. 

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
from apideck.model.logs_filter import LogsFilter
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.get_logs_response import GetLogsResponse
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
    api_instance = vault_api.VaultApi(api_client)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    filter = LogsFilter(
        connector_id="crm+salesforce",
        status_code=201,
        exclude_unified_apis="vault,proxy",
    ) # LogsFilter | Filter results (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of results to return. Minimum 1, Maximum 200, Default 20 (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all consumer request logs
        api_response = api_instance.logs_all(app_id=app_id, consumer_id=consumer_id, filter=filter, cursor=cursor, limit=limit)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->logs_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The ID of your Unify application | [optional]
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **filter** | **LogsFilter**| Filter results | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **limit** | **int**| Number of results to return. Minimum 1, Maximum 200, Default 20 | [optional] if omitted the server will use the default value of 20

### Return type

[**GetLogsResponse**](GetLogsResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Logs |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **sessions_create**
> CreateSessionResponse sessions_create()

Create Session

Making a POST request to this endpoint will initiate a Hosted Vault session. Redirect the consumer to the returned URL to allow temporary access to manage their integrations and settings.  Note: This is a short lived token that will expire after 1 hour (TTL: 3600). 

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.create_session_response import CreateSessionResponse
from apideck.model.session import Session
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
    api_instance = vault_api.VaultApi(api_client)
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    session = Session(
        consumer_metadata=ConsumerMetadata(
            account_name="SpaceX",
            user_name="Elon Musk",
            email="elon@musk.com",
            image="https://www.spacex.com/static/images/share.jpg",
        ),
        redirect_uri="https://mysaas.com/dashboard",
        settings=SessionSettings(
            unified_apis=[
                UnifiedApiId("crm"),
            ],
            hide_resource_settings=False,
            sandbox_mode=False,
            isolation_mode=False,
            session_length="30m",
            show_logs=True,
            show_suggestions=False,
            show_sidebar=True,
            auto_redirect=False,
            hide_guides=False,
            allow_actions=[
                "delete",
            ],
        ),
        theme=SessionTheme(
            favicon="https://res.cloudinary.com/apideck/icons/intercom",
            logo="https://res.cloudinary.com/apideck/icons/intercom",
            primary_color="#286efa",
            sidepanel_background_color="#286efa",
            sidepanel_text_color="#FFFFFF",
            vault_name="Intercom",
            privacy_url="https://compliance.apideck.com/privacy-policy",
            terms_url="https://www.termsfeed.com/terms-conditions/957c85c1b089ae9e3219c83eff65377e",
        ),
        custom_consumer_settings={},
    ) # Session | Additional redirect uri and/or consumer metadata (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Session
        api_response = api_instance.sessions_create(consumer_id=consumer_id, app_id=app_id, session=session)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->sessions_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **session** | [**Session**](Session.md)| Additional redirect uri and/or consumer metadata | [optional]

### Return type

[**CreateSessionResponse**](CreateSessionResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Session created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **validate_connection_state**
> ValidateConnectionStateResponse validate_connection_state(service_id, unified_api)

Validate Connection State

This endpoint validates the current state of a given connection. This will perform different checks based on the connection auth type. For basic and apiKey auth types, the presence of required fields is checked. For connectors that implement OAuth2, this operation forces the refresh flow for an access token regardless of its expiry.  Note:   - Do not include any credentials in the request body. This operation does not persist changes, but only triggers the validation of connection state.   - If a refresh token flow was performed and successful, the new access token will then be used for subsequent API requests. 

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import vault_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.validate_connection_state_response import ValidateConnectionStateResponse
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
    api_instance = vault_api.VaultApi(api_client)
    service_id = "pipedrive" # str | Service ID of the resource to return
    unified_api = "crm" # str | Unified API
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    body = {} # dict |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Validate Connection State
        api_response = api_instance.validate_connection_state(service_id, unified_api)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->validate_connection_state: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Validate Connection State
        api_response = api_instance.validate_connection_state(service_id, unified_api, consumer_id=consumer_id, app_id=app_id, body=body)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling VaultApi->validate_connection_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Service ID of the resource to return |
 **unified_api** | **str**| Unified API |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **body** | **dict**|  | [optional]

### Return type

[**ValidateConnectionStateResponse**](ValidateConnectionStateResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection access token refreshed |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

