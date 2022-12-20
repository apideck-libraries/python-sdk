# apideck.WebhookApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_logs_all**](WebhookApi.md#event_logs_all) | **GET** /webhook/logs | List event logs
[**webhooks_add**](WebhookApi.md#webhooks_add) | **POST** /webhook/webhooks | Create webhook subscription
[**webhooks_all**](WebhookApi.md#webhooks_all) | **GET** /webhook/webhooks | List webhook subscriptions
[**webhooks_delete**](WebhookApi.md#webhooks_delete) | **DELETE** /webhook/webhooks/{id} | Delete webhook subscription
[**webhooks_one**](WebhookApi.md#webhooks_one) | **GET** /webhook/webhooks/{id} | Get webhook subscription
[**webhooks_update**](WebhookApi.md#webhooks_update) | **PATCH** /webhook/webhooks/{id} | Update webhook subscription


# **event_logs_all**
> GetWebhookEventLogsResponse event_logs_all()

List event logs

List event logs

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import webhook_api
from apideck.model.get_webhook_event_logs_response import GetWebhookEventLogsResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.webhook_event_logs_filter import WebhookEventLogsFilter
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
    api_instance = webhook_api.WebhookApi(api_client)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of records to return (optional) if omitted the server will use the default value of 20
    filter = WebhookEventLogsFilter(
        exclude_apis="vault,proxy",
        service=WebhookEventLogsFilterService(
            id="id_example",
        ),
        consumer_id="test_user_id",
        entity_type="Connection",
        event_type="vault.connection.callable",
    ) # WebhookEventLogsFilter | Filter results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List event logs
        api_response = api_instance.event_logs_all(app_id=app_id, cursor=cursor, limit=limit, filter=filter)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling WebhookApi->event_logs_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The ID of your Unify application | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **limit** | **int**| Number of records to return | [optional] if omitted the server will use the default value of 20
 **filter** | **WebhookEventLogsFilter**| Filter results | [optional]

### Return type

[**GetWebhookEventLogsResponse**](GetWebhookEventLogsResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EventLogs |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **webhooks_add**
> CreateWebhookResponse webhooks_add(create_webhook_request)

Create webhook subscription

Create a webhook subscription to receive events

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import webhook_api
from apideck.model.create_webhook_response import CreateWebhookResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.create_webhook_request import CreateWebhookRequest
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
    api_instance = webhook_api.WebhookApi(api_client)
    create_webhook_request = CreateWebhookRequest(
        description="A description",
        unified_api=UnifiedApiId("crm"),
        status=Status("enabled"),
        delivery_url=DeliveryUrl("https://example.com/my/webhook/endpoint"),
        events=[
            WebhookEventType("["vault.connection.created","vault.connection.updated"]"),
        ],
    ) # CreateWebhookRequest | 
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create webhook subscription
        api_response = api_instance.webhooks_add(create_webhook_request)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling WebhookApi->webhooks_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create webhook subscription
        api_response = api_instance.webhooks_add(create_webhook_request, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling WebhookApi->webhooks_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook_request** | [**CreateWebhookRequest**](CreateWebhookRequest.md)|  |
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

[**CreateWebhookResponse**](CreateWebhookResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Webhooks |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **webhooks_all**
> GetWebhooksResponse webhooks_all()

List webhook subscriptions

List all webhook subscriptions

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import webhook_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.get_webhooks_response import GetWebhooksResponse
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
    api_instance = webhook_api.WebhookApi(api_client)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of records to return (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List webhook subscriptions
        api_response = api_instance.webhooks_all(app_id=app_id, cursor=cursor, limit=limit)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling WebhookApi->webhooks_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The ID of your Unify application | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **limit** | **int**| Number of records to return | [optional] if omitted the server will use the default value of 20

### Return type

[**GetWebhooksResponse**](GetWebhooksResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhooks |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **webhooks_delete**
> DeleteWebhookResponse webhooks_delete(id)

Delete webhook subscription

Delete a webhook subscription

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import webhook_api
from apideck.model.delete_webhook_response import DeleteWebhookResponse
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
    api_instance = webhook_api.WebhookApi(api_client)
    id = "id_example" # str | JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete webhook subscription
        api_response = api_instance.webhooks_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling WebhookApi->webhooks_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete webhook subscription
        api_response = api_instance.webhooks_delete(id, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling WebhookApi->webhooks_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. |
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

[**DeleteWebhookResponse**](DeleteWebhookResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhooks |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **webhooks_one**
> GetWebhookResponse webhooks_one(id)

Get webhook subscription

Get the webhook subscription details

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import webhook_api
from apideck.model.get_webhook_response import GetWebhookResponse
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
    api_instance = webhook_api.WebhookApi(api_client)
    id = "id_example" # str | JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get webhook subscription
        api_response = api_instance.webhooks_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling WebhookApi->webhooks_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get webhook subscription
        api_response = api_instance.webhooks_one(id, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling WebhookApi->webhooks_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. |
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

[**GetWebhookResponse**](GetWebhookResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhooks |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **webhooks_update**
> UpdateWebhookResponse webhooks_update(id, update_webhook_request)

Update webhook subscription

Update a webhook subscription

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import webhook_api
from apideck.model.update_webhook_response import UpdateWebhookResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.not_found_response import NotFoundResponse
from apideck.model.update_webhook_request import UpdateWebhookRequest
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
    api_instance = webhook_api.WebhookApi(api_client)
    id = "id_example" # str | JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.
    update_webhook_request = UpdateWebhookRequest(
        description="A description",
        status=Status("enabled"),
        delivery_url=DeliveryUrl("https://example.com/my/webhook/endpoint"),
        events=[
            WebhookEventType("["vault.connection.created","vault.connection.updated"]"),
        ],
    ) # UpdateWebhookRequest | 
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update webhook subscription
        api_response = api_instance.webhooks_update(id, update_webhook_request)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling WebhookApi->webhooks_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update webhook subscription
        api_response = api_instance.webhooks_update(id, update_webhook_request, app_id=app_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling WebhookApi->webhooks_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. |
 **update_webhook_request** | [**UpdateWebhookRequest**](UpdateWebhookRequest.md)|  |
 **app_id** | **str**| The ID of your Unify application | [optional]

### Return type

[**UpdateWebhookResponse**](UpdateWebhookResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhooks |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

