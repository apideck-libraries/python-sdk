# apideck.FileStorageApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**drive_groups_add**](FileStorageApi.md#drive_groups_add) | **POST** /file-storage/drive-groups | Create DriveGroup
[**drive_groups_all**](FileStorageApi.md#drive_groups_all) | **GET** /file-storage/drive-groups | List DriveGroups
[**drive_groups_delete**](FileStorageApi.md#drive_groups_delete) | **DELETE** /file-storage/drive-groups/{id} | Delete DriveGroup
[**drive_groups_one**](FileStorageApi.md#drive_groups_one) | **GET** /file-storage/drive-groups/{id} | Get DriveGroup
[**drive_groups_update**](FileStorageApi.md#drive_groups_update) | **PATCH** /file-storage/drive-groups/{id} | Update DriveGroup
[**drives_add**](FileStorageApi.md#drives_add) | **POST** /file-storage/drives | Create Drive
[**drives_all**](FileStorageApi.md#drives_all) | **GET** /file-storage/drives | List Drives
[**drives_delete**](FileStorageApi.md#drives_delete) | **DELETE** /file-storage/drives/{id} | Delete Drive
[**drives_one**](FileStorageApi.md#drives_one) | **GET** /file-storage/drives/{id} | Get Drive
[**drives_update**](FileStorageApi.md#drives_update) | **PATCH** /file-storage/drives/{id} | Update Drive
[**files_all**](FileStorageApi.md#files_all) | **GET** /file-storage/files | List Files
[**files_delete**](FileStorageApi.md#files_delete) | **DELETE** /file-storage/files/{id} | Delete File
[**files_download**](FileStorageApi.md#files_download) | **GET** /file-storage/files/{id}/download | Download File
[**files_export**](FileStorageApi.md#files_export) | **GET** /file-storage/files/{id}/export | Export File
[**files_one**](FileStorageApi.md#files_one) | **GET** /file-storage/files/{id} | Get File
[**files_search**](FileStorageApi.md#files_search) | **POST** /file-storage/files/search | Search Files
[**files_update**](FileStorageApi.md#files_update) | **PATCH** /file-storage/files/{id} | Rename or move File
[**folders_add**](FileStorageApi.md#folders_add) | **POST** /file-storage/folders | Create Folder
[**folders_copy**](FileStorageApi.md#folders_copy) | **POST** /file-storage/folders/{id}/copy | Copy Folder
[**folders_delete**](FileStorageApi.md#folders_delete) | **DELETE** /file-storage/folders/{id} | Delete Folder
[**folders_one**](FileStorageApi.md#folders_one) | **GET** /file-storage/folders/{id} | Get Folder
[**folders_update**](FileStorageApi.md#folders_update) | **PATCH** /file-storage/folders/{id} | Rename or move Folder
[**shared_links_add**](FileStorageApi.md#shared_links_add) | **POST** /file-storage/shared-links | Create Shared Link
[**shared_links_all**](FileStorageApi.md#shared_links_all) | **GET** /file-storage/shared-links | List SharedLinks
[**shared_links_delete**](FileStorageApi.md#shared_links_delete) | **DELETE** /file-storage/shared-links/{id} | Delete Shared Link
[**shared_links_one**](FileStorageApi.md#shared_links_one) | **GET** /file-storage/shared-links/{id} | Get Shared Link
[**shared_links_update**](FileStorageApi.md#shared_links_update) | **PATCH** /file-storage/shared-links/{id} | Update Shared Link
[**upload_sessions_add**](FileStorageApi.md#upload_sessions_add) | **POST** /file-storage/upload-sessions | Start Upload Session
[**upload_sessions_delete**](FileStorageApi.md#upload_sessions_delete) | **DELETE** /file-storage/upload-sessions/{id} | Abort Upload Session
[**upload_sessions_finish**](FileStorageApi.md#upload_sessions_finish) | **POST** /file-storage/upload-sessions/{id}/finish | Finish Upload Session
[**upload_sessions_one**](FileStorageApi.md#upload_sessions_one) | **GET** /file-storage/upload-sessions/{id} | Get Upload Session


# **drive_groups_add**
> CreateDriveGroupResponse drive_groups_add(drive_group)

Create DriveGroup

Create DriveGroup

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.drive_group import DriveGroup
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.create_drive_group_response import CreateDriveGroupResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    drive_group = DriveGroup(
        name="accounting",
        display_name="accounting",
        description="A description",
        pass_through=PassThroughBody([
            {
                service_id="service_id_example",
                operation_id="operation_id_example",
                extend_object={},
                extend_paths=[
                    {
                        path="$.nested.property",
                        value=None,
                    },
                ],
            },
        ]),
    ) # DriveGroup | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create DriveGroup
        api_response = api_instance.drive_groups_add(drive_group)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->drive_groups_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create DriveGroup
        api_response = api_instance.drive_groups_add(drive_group, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->drive_groups_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_group** | [**DriveGroup**](DriveGroup.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateDriveGroupResponse**](CreateDriveGroupResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | DriveGroups |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **drive_groups_all**
> GetDriveGroupsResponse drive_groups_all()

List DriveGroups

List DriveGroups

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.pass_through_query import PassThroughQuery
from apideck.model.get_drive_groups_response import GetDriveGroupsResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.drive_groups_filter import DriveGroupsFilter
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of results to return. Minimum 1, Maximum 200, Default 20 (optional) if omitted the server will use the default value of 20
    filter = DriveGroupsFilter(
        parent_group_id="1234",
    ) # DriveGroupsFilter | Apply filters (optional)
    pass_through = PassThroughQuery() # PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List DriveGroups
        api_response = api_instance.drive_groups_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, filter=filter, pass_through=pass_through, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->drive_groups_all: %s\n" % e)
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
 **filter** | **DriveGroupsFilter**| Apply filters | [optional]
 **pass_through** | **PassThroughQuery**| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional]
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

[**GetDriveGroupsResponse**](GetDriveGroupsResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DriveGroups |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **drive_groups_delete**
> DeleteDriveGroupResponse drive_groups_delete(id)

Delete DriveGroup

Delete DriveGroup

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.delete_drive_group_response import DeleteDriveGroupResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete DriveGroup
        api_response = api_instance.drive_groups_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->drive_groups_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete DriveGroup
        api_response = api_instance.drive_groups_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->drive_groups_delete: %s\n" % e)
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

[**DeleteDriveGroupResponse**](DeleteDriveGroupResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DriveGroups |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **drive_groups_one**
> GetDriveGroupResponse drive_groups_one(id)

Get DriveGroup

Get DriveGroup

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.get_drive_group_response import GetDriveGroupResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get DriveGroup
        api_response = api_instance.drive_groups_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->drive_groups_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get DriveGroup
        api_response = api_instance.drive_groups_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->drive_groups_one: %s\n" % e)
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

[**GetDriveGroupResponse**](GetDriveGroupResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DriveGroups |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **drive_groups_update**
> UpdateDriveGroupResponse drive_groups_update(id, drive_group)

Update DriveGroup

Update DriveGroup

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.drive_group import DriveGroup
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.update_drive_group_response import UpdateDriveGroupResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    drive_group = DriveGroup(
        name="accounting",
        display_name="accounting",
        description="A description",
        pass_through=PassThroughBody([
            {
                service_id="service_id_example",
                operation_id="operation_id_example",
                extend_object={},
                extend_paths=[
                    {
                        path="$.nested.property",
                        value=None,
                    },
                ],
            },
        ]),
    ) # DriveGroup | 
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update DriveGroup
        api_response = api_instance.drive_groups_update(id, drive_group)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->drive_groups_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update DriveGroup
        api_response = api_instance.drive_groups_update(id, drive_group, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->drive_groups_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **drive_group** | [**DriveGroup**](DriveGroup.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateDriveGroupResponse**](UpdateDriveGroupResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DriveGroups |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **drives_add**
> CreateDriveResponse drives_add(drive)

Create Drive

Create Drive

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.drive import Drive
from apideck.model.create_drive_response import CreateDriveResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    drive = Drive(
        name="Project Resources",
        description="A description",
        pass_through=PassThroughBody([
            {
                service_id="service_id_example",
                operation_id="operation_id_example",
                extend_object={},
                extend_paths=[
                    {
                        path="$.nested.property",
                        value=None,
                    },
                ],
            },
        ]),
    ) # Drive | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Drive
        api_response = api_instance.drives_add(drive)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->drives_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Drive
        api_response = api_instance.drives_add(drive, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->drives_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive** | [**Drive**](Drive.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateDriveResponse**](CreateDriveResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Drives |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **drives_all**
> GetDrivesResponse drives_all()

List Drives

List Drives

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.get_drives_response import GetDrivesResponse
from apideck.model.drives_filter import DrivesFilter
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of results to return. Minimum 1, Maximum 200, Default 20 (optional) if omitted the server will use the default value of 20
    filter = DrivesFilter(
        group_id="1234",
    ) # DrivesFilter | Apply filters (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Drives
        api_response = api_instance.drives_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, filter=filter, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->drives_all: %s\n" % e)
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
 **filter** | **DrivesFilter**| Apply filters | [optional]
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

[**GetDrivesResponse**](GetDrivesResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Drives |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **drives_delete**
> DeleteDriveResponse drives_delete(id)

Delete Drive

Delete Drive

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.delete_drive_response import DeleteDriveResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete Drive
        api_response = api_instance.drives_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->drives_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Drive
        api_response = api_instance.drives_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->drives_delete: %s\n" % e)
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

[**DeleteDriveResponse**](DeleteDriveResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Drives |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **drives_one**
> GetDriveResponse drives_one(id)

Get Drive

Get Drive

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.get_drive_response import GetDriveResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Drive
        api_response = api_instance.drives_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->drives_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Drive
        api_response = api_instance.drives_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->drives_one: %s\n" % e)
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

[**GetDriveResponse**](GetDriveResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Drives |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **drives_update**
> UpdateDriveResponse drives_update(id, drive)

Update Drive

Update Drive

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.drive import Drive
from apideck.model.update_drive_response import UpdateDriveResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    drive = Drive(
        name="Project Resources",
        description="A description",
        pass_through=PassThroughBody([
            {
                service_id="service_id_example",
                operation_id="operation_id_example",
                extend_object={},
                extend_paths=[
                    {
                        path="$.nested.property",
                        value=None,
                    },
                ],
            },
        ]),
    ) # Drive | 
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update Drive
        api_response = api_instance.drives_update(id, drive)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->drives_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Drive
        api_response = api_instance.drives_update(id, drive, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->drives_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **drive** | [**Drive**](Drive.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateDriveResponse**](UpdateDriveResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Drives |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **files_all**
> GetFilesResponse files_all()

List Files

List Files

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.pass_through_query import PassThroughQuery
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.files_sort import FilesSort
from apideck.model.files_filter import FilesFilter
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.get_files_response import GetFilesResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of results to return. Minimum 1, Maximum 200, Default 20 (optional) if omitted the server will use the default value of 20
    filter = FilesFilter(
        drive_id="1234",
        folder_id="root",
        shared=True,
    ) # FilesFilter | Apply filters (optional)
    sort = FilesSort(
        by="updated_at",
        direction=SortDirection("asc"),
    ) # FilesSort | Apply sorting (optional)
    pass_through = PassThroughQuery() # PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Files
        api_response = api_instance.files_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, filter=filter, sort=sort, pass_through=pass_through, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->files_all: %s\n" % e)
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
 **filter** | **FilesFilter**| Apply filters | [optional]
 **sort** | **FilesSort**| Apply sorting | [optional]
 **pass_through** | **PassThroughQuery**| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional]
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

[**GetFilesResponse**](GetFilesResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Files |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **files_delete**
> DeleteFileResponse files_delete(id)

Delete File

Delete File

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.delete_file_response import DeleteFileResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete File
        api_response = api_instance.files_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->files_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete File
        api_response = api_instance.files_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->files_delete: %s\n" % e)
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

[**DeleteFileResponse**](DeleteFileResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Files |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **files_download**
> file_type files_download(id)

Download File

Download File

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Download File
        api_response = api_instance.files_download(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->files_download: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Download File
        api_response = api_instance.files_download(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->files_download: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

**file_type**

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File Download |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **files_export**
> file_type files_export(id, format)

Export File

Export File

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    format = "pdf" # str | File format to export this file to. A list of available file formats for the current file is available as `export_formats` on the File resource.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export File
        api_response = api_instance.files_export(id, format)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->files_export: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export File
        api_response = api_instance.files_export(id, format, consumer_id=consumer_id, app_id=app_id, service_id=service_id, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->files_export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **format** | **str**| File format to export this file to. A list of available file formats for the current file is available as &#x60;export_formats&#x60; on the File resource. |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

**file_type**

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File Download |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **files_one**
> GetFileResponse files_one(id)

Get File

Get File

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.get_file_response import GetFileResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get File
        api_response = api_instance.files_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->files_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get File
        api_response = api_instance.files_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->files_one: %s\n" % e)
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

[**GetFileResponse**](GetFileResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **files_search**
> GetFilesResponse files_search(files_search)

Search Files

Search Files

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.pass_through_query import PassThroughQuery
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.files_filter import FilesFilter
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.get_files_response import GetFilesResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.files_search import FilesSearch
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    files_search = FilesSearch(
        query="logo jpg",
        drive_id="1234",
        pass_through=PassThroughBody([
            {
                service_id="service_id_example",
                operation_id="operation_id_example",
                extend_object={},
                extend_paths=[
                    {
                        path="$.nested.property",
                        value=None,
                    },
                ],
            },
        ]),
    ) # FilesSearch | 
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    pass_through = PassThroughQuery() # PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of results to return. Minimum 1, Maximum 200, Default 20 (optional) if omitted the server will use the default value of 20
    filter = FilesFilter(
        drive_id="1234",
        folder_id="root",
        shared=True,
    ) # FilesFilter | Apply filters (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search Files
        api_response = api_instance.files_search(files_search)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->files_search: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Files
        api_response = api_instance.files_search(files_search, consumer_id=consumer_id, app_id=app_id, service_id=service_id, pass_through=pass_through, fields=fields, cursor=cursor, limit=limit, filter=filter)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->files_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **files_search** | [**FilesSearch**](FilesSearch.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **pass_through** | **PassThroughQuery**| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional]
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **limit** | **int**| Number of results to return. Minimum 1, Maximum 200, Default 20 | [optional] if omitted the server will use the default value of 20
 **filter** | **FilesFilter**| Apply filters | [optional]

### Return type

[**GetFilesResponse**](GetFilesResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Files |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **files_update**
> UpdateFileResponse files_update(id, update_file_request)

Rename or move File

Rename or move File

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.update_file_response import UpdateFileResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.update_file_request import UpdateFileRequest
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    update_file_request = UpdateFileRequest(
        name="New Name.pdf",
        description="Renamed PDF Document",
        parent_folder_id="1234",
        pass_through=PassThroughBody([
            {
                service_id="service_id_example",
                operation_id="operation_id_example",
                extend_object={},
                extend_paths=[
                    {
                        path="$.nested.property",
                        value=None,
                    },
                ],
            },
        ]),
    ) # UpdateFileRequest | 
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Rename or move File
        api_response = api_instance.files_update(id, update_file_request)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->files_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Rename or move File
        api_response = api_instance.files_update(id, update_file_request, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->files_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **update_file_request** | [**UpdateFileRequest**](UpdateFileRequest.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateFileResponse**](UpdateFileResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Files |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **folders_add**
> CreateFolderResponse folders_add(create_folder_request)

Create Folder

Create Folder

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.create_folder_request import CreateFolderRequest
from apideck.model.create_folder_response import CreateFolderResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    create_folder_request = CreateFolderRequest(
        name="Documents",
        description="My Personal Documents",
        parent_folder_id="1234",
        drive_id="1234",
        pass_through=PassThroughBody([
            {
                service_id="service_id_example",
                operation_id="operation_id_example",
                extend_object={},
                extend_paths=[
                    {
                        path="$.nested.property",
                        value=None,
                    },
                ],
            },
        ]),
    ) # CreateFolderRequest | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Folder
        api_response = api_instance.folders_add(create_folder_request)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->folders_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Folder
        api_response = api_instance.folders_add(create_folder_request, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->folders_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_folder_request** | [**CreateFolderRequest**](CreateFolderRequest.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

[**CreateFolderResponse**](CreateFolderResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Folders |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **folders_copy**
> UpdateFolderResponse folders_copy(id, copy_folder_request)

Copy Folder

Copy Folder

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.update_folder_response import UpdateFolderResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.copy_folder_request import CopyFolderRequest
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    copy_folder_request = CopyFolderRequest(
        name="Documents",
        parent_folder_id="1234",
        pass_through=PassThroughBody([
            {
                service_id="service_id_example",
                operation_id="operation_id_example",
                extend_object={},
                extend_paths=[
                    {
                        path="$.nested.property",
                        value=None,
                    },
                ],
            },
        ]),
    ) # CopyFolderRequest | 
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Copy Folder
        api_response = api_instance.folders_copy(id, copy_folder_request)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->folders_copy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Copy Folder
        api_response = api_instance.folders_copy(id, copy_folder_request, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->folders_copy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **copy_folder_request** | [**CopyFolderRequest**](CopyFolderRequest.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

[**UpdateFolderResponse**](UpdateFolderResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folders |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **folders_delete**
> DeleteFolderResponse folders_delete(id)

Delete Folder

Delete Folder

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.delete_folder_response import DeleteFolderResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete Folder
        api_response = api_instance.folders_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->folders_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Folder
        api_response = api_instance.folders_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->folders_delete: %s\n" % e)
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

[**DeleteFolderResponse**](DeleteFolderResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folders |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **folders_one**
> GetFolderResponse folders_one(id)

Get Folder

Get Folder

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.get_folder_response import GetFolderResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Folder
        api_response = api_instance.folders_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->folders_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Folder
        api_response = api_instance.folders_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->folders_one: %s\n" % e)
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

[**GetFolderResponse**](GetFolderResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folders |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **folders_update**
> UpdateFolderResponse folders_update(id, update_folder_request)

Rename or move Folder

Rename or move Folder

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.update_folder_request import UpdateFolderRequest
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.update_folder_response import UpdateFolderResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    update_folder_request = UpdateFolderRequest(
        name="Documents",
        description="My Personal Documents",
        parent_folder_id="1234",
        pass_through=PassThroughBody([
            {
                service_id="service_id_example",
                operation_id="operation_id_example",
                extend_object={},
                extend_paths=[
                    {
                        path="$.nested.property",
                        value=None,
                    },
                ],
            },
        ]),
    ) # UpdateFolderRequest | 
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Rename or move Folder
        api_response = api_instance.folders_update(id, update_folder_request)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->folders_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Rename or move Folder
        api_response = api_instance.folders_update(id, update_folder_request, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->folders_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **update_folder_request** | [**UpdateFolderRequest**](UpdateFolderRequest.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateFolderResponse**](UpdateFolderResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folders |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **shared_links_add**
> CreateSharedLinkResponse shared_links_add(shared_link)

Create Shared Link

Create Shared Link

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.create_shared_link_response import CreateSharedLinkResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.shared_link import SharedLink
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    shared_link = SharedLink(
        download_url="https://www.box.com/shared/static/rh935iit6ewrmw0unyul.jpeg",
        target_id="target_id_example",
        scope="company",
        password="password_example",
        pass_through=PassThroughBody([
            {
                service_id="service_id_example",
                operation_id="operation_id_example",
                extend_object={},
                extend_paths=[
                    {
                        path="$.nested.property",
                        value=None,
                    },
                ],
            },
        ]),
    ) # SharedLink | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Shared Link
        api_response = api_instance.shared_links_add(shared_link)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->shared_links_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Shared Link
        api_response = api_instance.shared_links_add(shared_link, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->shared_links_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_link** | [**SharedLink**](SharedLink.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateSharedLinkResponse**](CreateSharedLinkResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Shared Links |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **shared_links_all**
> GetSharedLinksResponse shared_links_all()

List SharedLinks

List SharedLinks

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.pass_through_query import PassThroughQuery
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.get_shared_links_response import GetSharedLinksResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
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
        # List SharedLinks
        api_response = api_instance.shared_links_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, pass_through=pass_through, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->shared_links_all: %s\n" % e)
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

[**GetSharedLinksResponse**](GetSharedLinksResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Shared Links |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **shared_links_delete**
> DeleteSharedLinkResponse shared_links_delete(id)

Delete Shared Link

Delete Shared Link

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.delete_shared_link_response import DeleteSharedLinkResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete Shared Link
        api_response = api_instance.shared_links_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->shared_links_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Shared Link
        api_response = api_instance.shared_links_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->shared_links_delete: %s\n" % e)
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

[**DeleteSharedLinkResponse**](DeleteSharedLinkResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Shared Links |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **shared_links_one**
> GetSharedLinkResponse shared_links_one(id)

Get Shared Link

Get Shared Link

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.get_shared_link_response import GetSharedLinkResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Shared Link
        api_response = api_instance.shared_links_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->shared_links_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Shared Link
        api_response = api_instance.shared_links_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->shared_links_one: %s\n" % e)
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

[**GetSharedLinkResponse**](GetSharedLinkResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Shared Link |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **shared_links_update**
> UpdateSharedLinkResponse shared_links_update(id, shared_link)

Update Shared Link

Update Shared Link

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.update_shared_link_response import UpdateSharedLinkResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.shared_link import SharedLink
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    shared_link = SharedLink(
        download_url="https://www.box.com/shared/static/rh935iit6ewrmw0unyul.jpeg",
        target_id="target_id_example",
        scope="company",
        password="password_example",
        pass_through=PassThroughBody([
            {
                service_id="service_id_example",
                operation_id="operation_id_example",
                extend_object={},
                extend_paths=[
                    {
                        path="$.nested.property",
                        value=None,
                    },
                ],
            },
        ]),
    ) # SharedLink | 
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update Shared Link
        api_response = api_instance.shared_links_update(id, shared_link)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->shared_links_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Shared Link
        api_response = api_instance.shared_links_update(id, shared_link, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->shared_links_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **shared_link** | [**SharedLink**](SharedLink.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateSharedLinkResponse**](UpdateSharedLinkResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Shared Links |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **upload_sessions_add**
> CreateUploadSessionResponse upload_sessions_add(create_upload_session_request)

Start Upload Session

Start an Upload Session. Upload sessions are used to upload large files, use the [Upload File](#operation/filesUpload) endpoint to upload smaller files (up to 100MB). Note that the base URL is upload.apideck.com instead of unify.apideck.com. For more information on uploads, refer to the [file upload guide](/guides/file-upload).

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.create_upload_session_response import CreateUploadSessionResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.create_upload_session_request import CreateUploadSessionRequest
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    create_upload_session_request = CreateUploadSessionRequest(
        name="Documents",
        parent_folder_id="1234",
        drive_id="1234",
        size=1810673,
        pass_through=PassThroughBody([
            {
                service_id="service_id_example",
                operation_id="operation_id_example",
                extend_object={},
                extend_paths=[
                    {
                        path="$.nested.property",
                        value=None,
                    },
                ],
            },
        ]),
    ) # CreateUploadSessionRequest | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Start Upload Session
        api_response = api_instance.upload_sessions_add(create_upload_session_request)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->upload_sessions_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start Upload Session
        api_response = api_instance.upload_sessions_add(create_upload_session_request, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->upload_sessions_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_upload_session_request** | [**CreateUploadSessionRequest**](CreateUploadSessionRequest.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateUploadSessionResponse**](CreateUploadSessionResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | UploadSessions |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **upload_sessions_delete**
> DeleteUploadSessionResponse upload_sessions_delete(id)

Abort Upload Session

Abort Upload Session. Note that the base URL is upload.apideck.com instead of unify.apideck.com. For more information on uploads, refer to the [file upload guide](/guides/file-upload).

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.delete_upload_session_response import DeleteUploadSessionResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Abort Upload Session
        api_response = api_instance.upload_sessions_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->upload_sessions_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Abort Upload Session
        api_response = api_instance.upload_sessions_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->upload_sessions_delete: %s\n" % e)
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

[**DeleteUploadSessionResponse**](DeleteUploadSessionResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UploadSessions |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **upload_sessions_finish**
> GetFileResponse upload_sessions_finish(id)

Finish Upload Session

Finish Upload Session. Only call this endpoint after all File parts have been uploaded to [Upload part of File](#operation/uploadSessionsUpload). Note that the base URL is upload.apideck.com instead of unify.apideck.com. For more information on uploads, refer to the [file upload guide](/guides/file-upload).

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.get_file_response import GetFileResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    digest = "sha=fpRyg5eVQletdZqEKaFlqwBXJzM=" # str | The RFC3230 message digest of the uploaded part. Only required for the Box connector. More information on the Box API docs [here](https://developer.box.com/reference/put-files-upload-sessions-id/#param-digest) (optional)
    body = {} # dict |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Finish Upload Session
        api_response = api_instance.upload_sessions_finish(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->upload_sessions_finish: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Finish Upload Session
        api_response = api_instance.upload_sessions_finish(id, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, digest=digest, body=body)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->upload_sessions_finish: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **digest** | **str**| The RFC3230 message digest of the uploaded part. Only required for the Box connector. More information on the Box API docs [here](https://developer.box.com/reference/put-files-upload-sessions-id/#param-digest) | [optional]
 **body** | **dict**|  | [optional]

### Return type

[**GetFileResponse**](GetFileResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | File |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **upload_sessions_one**
> GetUploadSessionResponse upload_sessions_one(id)

Get Upload Session

Get Upload Session. Use the `part_size` to split your file into parts. Upload the parts to the [Upload part of File](#operation/uploadSessionsUpload) endpoint. Note that the base URL is upload.apideck.com instead of unify.apideck.com. For more information on uploads, refer to the [file upload guide](/guides/file-upload).

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import file_storage_api
from apideck.model.get_upload_session_response import GetUploadSessionResponse
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
    api_instance = file_storage_api.FileStorageApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Upload Session
        api_response = api_instance.upload_sessions_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->upload_sessions_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Upload Session
        api_response = api_instance.upload_sessions_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling FileStorageApi->upload_sessions_one: %s\n" % e)
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

[**GetUploadSessionResponse**](GetUploadSessionResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UploadSessions |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

