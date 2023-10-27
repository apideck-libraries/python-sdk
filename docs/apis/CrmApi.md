# apideck.CrmApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activities_add**](CrmApi.md#activities_add) | **POST** /crm/activities | Create activity
[**activities_all**](CrmApi.md#activities_all) | **GET** /crm/activities | List activities
[**activities_delete**](CrmApi.md#activities_delete) | **DELETE** /crm/activities/{id} | Delete activity
[**activities_one**](CrmApi.md#activities_one) | **GET** /crm/activities/{id} | Get activity
[**activities_update**](CrmApi.md#activities_update) | **PATCH** /crm/activities/{id} | Update activity
[**companies_add**](CrmApi.md#companies_add) | **POST** /crm/companies | Create company
[**companies_all**](CrmApi.md#companies_all) | **GET** /crm/companies | List companies
[**companies_delete**](CrmApi.md#companies_delete) | **DELETE** /crm/companies/{id} | Delete company
[**companies_one**](CrmApi.md#companies_one) | **GET** /crm/companies/{id} | Get company
[**companies_update**](CrmApi.md#companies_update) | **PATCH** /crm/companies/{id} | Update company
[**contacts_add**](CrmApi.md#contacts_add) | **POST** /crm/contacts | Create contact
[**contacts_all**](CrmApi.md#contacts_all) | **GET** /crm/contacts | List contacts
[**contacts_delete**](CrmApi.md#contacts_delete) | **DELETE** /crm/contacts/{id} | Delete contact
[**contacts_one**](CrmApi.md#contacts_one) | **GET** /crm/contacts/{id} | Get contact
[**contacts_update**](CrmApi.md#contacts_update) | **PATCH** /crm/contacts/{id} | Update contact
[**leads_add**](CrmApi.md#leads_add) | **POST** /crm/leads | Create lead
[**leads_all**](CrmApi.md#leads_all) | **GET** /crm/leads | List leads
[**leads_delete**](CrmApi.md#leads_delete) | **DELETE** /crm/leads/{id} | Delete lead
[**leads_one**](CrmApi.md#leads_one) | **GET** /crm/leads/{id} | Get lead
[**leads_update**](CrmApi.md#leads_update) | **PATCH** /crm/leads/{id} | Update lead
[**notes_add**](CrmApi.md#notes_add) | **POST** /crm/notes | Create note
[**notes_all**](CrmApi.md#notes_all) | **GET** /crm/notes | List notes
[**notes_delete**](CrmApi.md#notes_delete) | **DELETE** /crm/notes/{id} | Delete note
[**notes_one**](CrmApi.md#notes_one) | **GET** /crm/notes/{id} | Get note
[**notes_update**](CrmApi.md#notes_update) | **PATCH** /crm/notes/{id} | Update note
[**opportunities_add**](CrmApi.md#opportunities_add) | **POST** /crm/opportunities | Create opportunity
[**opportunities_all**](CrmApi.md#opportunities_all) | **GET** /crm/opportunities | List opportunities
[**opportunities_delete**](CrmApi.md#opportunities_delete) | **DELETE** /crm/opportunities/{id} | Delete opportunity
[**opportunities_one**](CrmApi.md#opportunities_one) | **GET** /crm/opportunities/{id} | Get opportunity
[**opportunities_update**](CrmApi.md#opportunities_update) | **PATCH** /crm/opportunities/{id} | Update opportunity
[**pipelines_add**](CrmApi.md#pipelines_add) | **POST** /crm/pipelines | Create pipeline
[**pipelines_all**](CrmApi.md#pipelines_all) | **GET** /crm/pipelines | List pipelines
[**pipelines_delete**](CrmApi.md#pipelines_delete) | **DELETE** /crm/pipelines/{id} | Delete pipeline
[**pipelines_one**](CrmApi.md#pipelines_one) | **GET** /crm/pipelines/{id} | Get pipeline
[**pipelines_update**](CrmApi.md#pipelines_update) | **PATCH** /crm/pipelines/{id} | Update pipeline
[**users_add**](CrmApi.md#users_add) | **POST** /crm/users | Create user
[**users_all**](CrmApi.md#users_all) | **GET** /crm/users | List users
[**users_delete**](CrmApi.md#users_delete) | **DELETE** /crm/users/{id} | Delete user
[**users_one**](CrmApi.md#users_one) | **GET** /crm/users/{id} | Get user
[**users_update**](CrmApi.md#users_update) | **PATCH** /crm/users/{id} | Update user


# **activities_add**
> CreateActivityResponse activities_add(activity)

Create activity

Create activity

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.create_activity_response import CreateActivityResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.activity import Activity
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
    api_instance = crm_api.CrmApi(api_client)
    activity = Activity(
        activity_datetime="2021-05-01T12:00:00.000Z",
        duration_seconds=1800,
        user_id="12345",
        account_id="12345",
        contact_id="12345",
        company_id="12345",
        opportunity_id="12345",
        lead_id="12345",
        owner_id="12345",
        campaign_id="12345",
        case_id="12345",
        asset_id="12345",
        contract_id="12345",
        product_id="12345",
        solution_id="12345",
        custom_object_id="12345",
        type="meeting",
        title="Meeting",
        description="More info about the meeting",
        note="An internal note about the meeting",
        location="Space",
        location_address=Address(
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
            notes="Address notes or delivery instructions.",
            row_version="1-12345",
        ),
        all_day_event=False,
        private=True,
        group_event=True,
        event_sub_type="debrief",
        group_event_type="Proposed",
        child=False,
        archived=False,
        deleted=False,
        show_as="busy",
        done=False,
        start_datetime="2021-05-01T12:00:00.000Z",
        end_datetime="2021-05-01T12:30:00.000Z",
        activity_date="2021-05-01",
        end_date="2021-05-01",
        recurrent=False,
        reminder_datetime="2021-05-01T17:00:00.000Z",
        reminder_set=False,
        video_conference_url="https://us02web.zoom.us/j/88120759396",
        video_conference_id="zoom:88120759396",
        custom_fields=[
            CustomField(
                id="2389328923893298",
                name="employee_level",
                description="Employee Level",
                value=None,
            ),
        ],
        attendees=[
            ActivityAttendee(
                name="Elon Musk",
                first_name="Elon",
                middle_name="D.",
                last_name="Musk",
                prefix="Mr.",
                suffix="PhD",
                email_address="elon@musk.com",
                is_organizer=True,
                status="accepted",
            ),
        ],
    ) # Activity | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create activity
        api_response = api_instance.activities_add(activity)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->activities_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create activity
        api_response = api_instance.activities_add(activity, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->activities_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity** | [**Activity**](Activity.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateActivityResponse**](CreateActivityResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Activity created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **activities_all**
> GetActivitiesResponse activities_all()

List activities

List activities

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.pass_through_query import PassThroughQuery
from apideck.model.get_activities_response import GetActivitiesResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.activities_filter import ActivitiesFilter
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
    api_instance = crm_api.CrmApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of results to return. Minimum 1, Maximum 200, Default 20 (optional) if omitted the server will use the default value of 20
    filter = ActivitiesFilter(
        updated_since=dateutil_parser('2020-09-30T07:43:32Z'),
    ) # ActivitiesFilter | Apply filters (optional)
    pass_through = PassThroughQuery() # PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List activities
        api_response = api_instance.activities_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, filter=filter, pass_through=pass_through, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->activities_all: %s\n" % e)
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
 **filter** | **ActivitiesFilter**| Apply filters | [optional]
 **pass_through** | **PassThroughQuery**| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional]
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

[**GetActivitiesResponse**](GetActivitiesResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Activities |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **activities_delete**
> DeleteActivityResponse activities_delete(id)

Delete activity

Delete activity

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.delete_activity_response import DeleteActivityResponse
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete activity
        api_response = api_instance.activities_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->activities_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete activity
        api_response = api_instance.activities_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->activities_delete: %s\n" % e)
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

[**DeleteActivityResponse**](DeleteActivityResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Activity deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **activities_one**
> GetActivityResponse activities_one(id)

Get activity

Get activity

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.get_activity_response import GetActivityResponse
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get activity
        api_response = api_instance.activities_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->activities_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get activity
        api_response = api_instance.activities_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->activities_one: %s\n" % e)
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

[**GetActivityResponse**](GetActivityResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Activity |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **activities_update**
> UpdateActivityResponse activities_update(id, activity)

Update activity

Update activity

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.update_activity_response import UpdateActivityResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.activity import Activity
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    activity = Activity(
        activity_datetime="2021-05-01T12:00:00.000Z",
        duration_seconds=1800,
        user_id="12345",
        account_id="12345",
        contact_id="12345",
        company_id="12345",
        opportunity_id="12345",
        lead_id="12345",
        owner_id="12345",
        campaign_id="12345",
        case_id="12345",
        asset_id="12345",
        contract_id="12345",
        product_id="12345",
        solution_id="12345",
        custom_object_id="12345",
        type="meeting",
        title="Meeting",
        description="More info about the meeting",
        note="An internal note about the meeting",
        location="Space",
        location_address=Address(
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
            notes="Address notes or delivery instructions.",
            row_version="1-12345",
        ),
        all_day_event=False,
        private=True,
        group_event=True,
        event_sub_type="debrief",
        group_event_type="Proposed",
        child=False,
        archived=False,
        deleted=False,
        show_as="busy",
        done=False,
        start_datetime="2021-05-01T12:00:00.000Z",
        end_datetime="2021-05-01T12:30:00.000Z",
        activity_date="2021-05-01",
        end_date="2021-05-01",
        recurrent=False,
        reminder_datetime="2021-05-01T17:00:00.000Z",
        reminder_set=False,
        video_conference_url="https://us02web.zoom.us/j/88120759396",
        video_conference_id="zoom:88120759396",
        custom_fields=[
            CustomField(
                id="2389328923893298",
                name="employee_level",
                description="Employee Level",
                value=None,
            ),
        ],
        attendees=[
            ActivityAttendee(
                name="Elon Musk",
                first_name="Elon",
                middle_name="D.",
                last_name="Musk",
                prefix="Mr.",
                suffix="PhD",
                email_address="elon@musk.com",
                is_organizer=True,
                status="accepted",
            ),
        ],
    ) # Activity | 
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update activity
        api_response = api_instance.activities_update(id, activity)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->activities_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update activity
        api_response = api_instance.activities_update(id, activity, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->activities_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **activity** | [**Activity**](Activity.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateActivityResponse**](UpdateActivityResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Activity updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **companies_add**
> CreateCompanyResponse companies_add(company)

Create company

Create company

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.create_company_response import CreateCompanyResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.company import Company
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
    api_instance = crm_api.CrmApi(api_client)
    company = Company(
        name="SpaceX",
        owner_id="12345",
        image="https://www.spacex.com/static/images/share.jpg",
        description="Space Exploration Technologies Corp. is an American aerospace manufacturer, space transportation services and communications company headquartered in Hawthorne, California.",
        vat_number="BE0689615164",
        currency=Currency("USD"),
        status="Open",
        fax="+12129876543",
        annual_revenue="+$35m",
        number_of_employees="500-1000",
        industry="Apparel",
        ownership="Public",
        sales_tax_number="12456EN",
        payee_number="78932EN",
        abn_or_tfn="46 115 614 695",
        abn_branch="123",
        acn="XXX XXX XXX",
        first_name="Elon",
        last_name="Musk",
        bank_accounts=[
            BankAccount(
                bank_name="Monzo",
                account_number="123465",
                account_name="SPACEX LLC",
                account_type="credit_card",
                iban="CH2989144532982975332",
                bic="AUDSCHGGXXX",
                routing_number="012345678",
                bsb_number="062-001",
                branch_identifier="001",
                bank_code="BNH",
                currency=Currency("USD"),
            ),
        ],
        websites=[
            Website(
                id="12345",
                url="http://example.com",
                type="primary",
            ),
        ],
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
                notes="Address notes or delivery instructions.",
                row_version="1-12345",
            ),
        ],
        social_links=[
            SocialLink(
                id="12345",
                url="https://www.twitter.com/apideck",
                type="twitter",
            ),
        ],
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
        row_type=CompanyRowType(
            id="12345",
            name="Customer Account",
        ),
        custom_fields=[
            CustomField(
                id="2389328923893298",
                name="employee_level",
                description="Employee Level",
                value=None,
            ),
        ],
        tags=Tags(["New"]),
        read_only=False,
        salutation="Mr",
        birthday=dateutil_parser('Sat Aug 12 00:00:00 UTC 2000').date(),
    ) # Company | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create company
        api_response = api_instance.companies_add(company)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->companies_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create company
        api_response = api_instance.companies_add(company, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->companies_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company** | [**Company**](Company.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateCompanyResponse**](CreateCompanyResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Company created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **companies_all**
> GetCompaniesResponse companies_all()

List companies

List companies

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.pass_through_query import PassThroughQuery
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.companies_sort import CompaniesSort
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.get_companies_response import GetCompaniesResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.companies_filter import CompaniesFilter
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
    api_instance = crm_api.CrmApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of results to return. Minimum 1, Maximum 200, Default 20 (optional) if omitted the server will use the default value of 20
    filter = CompaniesFilter(
        name="SpaceX",
    ) # CompaniesFilter | Apply filters (optional)
    sort = CompaniesSort(
        by="created_at",
        direction=SortDirection("asc"),
    ) # CompaniesSort | Apply sorting (optional)
    pass_through = PassThroughQuery() # PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List companies
        api_response = api_instance.companies_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, filter=filter, sort=sort, pass_through=pass_through, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->companies_all: %s\n" % e)
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
 **filter** | **CompaniesFilter**| Apply filters | [optional]
 **sort** | **CompaniesSort**| Apply sorting | [optional]
 **pass_through** | **PassThroughQuery**| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional]
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

[**GetCompaniesResponse**](GetCompaniesResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Companies |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **companies_delete**
> DeleteCompanyResponse companies_delete(id)

Delete company

Delete company

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.delete_company_response import DeleteCompanyResponse
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete company
        api_response = api_instance.companies_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->companies_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete company
        api_response = api_instance.companies_delete(id, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->companies_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**DeleteCompanyResponse**](DeleteCompanyResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Company deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **companies_one**
> GetCompanyResponse companies_one(id)

Get company

Get company

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.get_company_response import GetCompanyResponse
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get company
        api_response = api_instance.companies_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->companies_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get company
        api_response = api_instance.companies_one(id, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->companies_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

[**GetCompanyResponse**](GetCompanyResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Company |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **companies_update**
> UpdateCompanyResponse companies_update(id, company)

Update company

Update company

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.update_company_response import UpdateCompanyResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.company import Company
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    company = Company(
        name="SpaceX",
        owner_id="12345",
        image="https://www.spacex.com/static/images/share.jpg",
        description="Space Exploration Technologies Corp. is an American aerospace manufacturer, space transportation services and communications company headquartered in Hawthorne, California.",
        vat_number="BE0689615164",
        currency=Currency("USD"),
        status="Open",
        fax="+12129876543",
        annual_revenue="+$35m",
        number_of_employees="500-1000",
        industry="Apparel",
        ownership="Public",
        sales_tax_number="12456EN",
        payee_number="78932EN",
        abn_or_tfn="46 115 614 695",
        abn_branch="123",
        acn="XXX XXX XXX",
        first_name="Elon",
        last_name="Musk",
        bank_accounts=[
            BankAccount(
                bank_name="Monzo",
                account_number="123465",
                account_name="SPACEX LLC",
                account_type="credit_card",
                iban="CH2989144532982975332",
                bic="AUDSCHGGXXX",
                routing_number="012345678",
                bsb_number="062-001",
                branch_identifier="001",
                bank_code="BNH",
                currency=Currency("USD"),
            ),
        ],
        websites=[
            Website(
                id="12345",
                url="http://example.com",
                type="primary",
            ),
        ],
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
                notes="Address notes or delivery instructions.",
                row_version="1-12345",
            ),
        ],
        social_links=[
            SocialLink(
                id="12345",
                url="https://www.twitter.com/apideck",
                type="twitter",
            ),
        ],
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
        row_type=CompanyRowType(
            id="12345",
            name="Customer Account",
        ),
        custom_fields=[
            CustomField(
                id="2389328923893298",
                name="employee_level",
                description="Employee Level",
                value=None,
            ),
        ],
        tags=Tags(["New"]),
        read_only=False,
        salutation="Mr",
        birthday=dateutil_parser('Sat Aug 12 00:00:00 UTC 2000').date(),
    ) # Company | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update company
        api_response = api_instance.companies_update(id, company)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->companies_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update company
        api_response = api_instance.companies_update(id, company, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->companies_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **company** | [**Company**](Company.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**UpdateCompanyResponse**](UpdateCompanyResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Company updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **contacts_add**
> CreateContactResponse contacts_add(contact)

Create contact

Create contact

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.create_contact_response import CreateContactResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.contact import Contact
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
    api_instance = crm_api.CrmApi(api_client)
    contact = Contact(
        name="Elon Musk",
        owner_id="54321",
        type="personal",
        company_id="23456",
        company_name="23456",
        lead_id="34567",
        first_name="Elon",
        middle_name="D.",
        last_name="Musk",
        prefix="Mr.",
        suffix="PhD",
        title="CEO",
        department="Engineering",
        language="EN",
        gender="female",
        birthday="2000-08-12",
        image="https://unavatar.io/elon-musk",
        photo_url="https://unavatar.io/elon-musk",
        lead_source="Cold Call",
        fax="+12129876543",
        description="Internal champion",
        current_balance=10.5,
        status="open",
        active=True,
        websites=[
            Website(
                id="12345",
                url="http://example.com",
                type="primary",
            ),
        ],
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
                notes="Address notes or delivery instructions.",
                row_version="1-12345",
            ),
        ],
        social_links=[
            SocialLink(
                id="12345",
                url="https://www.twitter.com/apideck",
                type="twitter",
            ),
        ],
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
        email_domain="gmail.com",
        custom_fields=[
            CustomField(
                id="2389328923893298",
                name="employee_level",
                description="Employee Level",
                value=None,
            ),
        ],
        tags=Tags(["New"]),
    ) # Contact | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create contact
        api_response = api_instance.contacts_add(contact)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->contacts_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create contact
        api_response = api_instance.contacts_add(contact, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->contacts_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact** | [**Contact**](Contact.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateContactResponse**](CreateContactResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Contact created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **contacts_all**
> GetContactsResponse contacts_all()

List contacts

List contacts

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.get_contacts_response import GetContactsResponse
from apideck.model.pass_through_query import PassThroughQuery
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.contacts_sort import ContactsSort
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.contacts_filter import ContactsFilter
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
    api_instance = crm_api.CrmApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of results to return. Minimum 1, Maximum 200, Default 20 (optional) if omitted the server will use the default value of 20
    filter = ContactsFilter(
        name="Elon Musk",
        first_name="Elon",
        last_name="Musk",
        email="elon@tesla.com",
        company_id="12345",
    ) # ContactsFilter | Apply filters (optional)
    sort = ContactsSort(
        by="created_at",
        direction=SortDirection("asc"),
    ) # ContactsSort | Apply sorting (optional)
    pass_through = PassThroughQuery() # PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List contacts
        api_response = api_instance.contacts_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, filter=filter, sort=sort, pass_through=pass_through, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->contacts_all: %s\n" % e)
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
 **filter** | **ContactsFilter**| Apply filters | [optional]
 **sort** | **ContactsSort**| Apply sorting | [optional]
 **pass_through** | **PassThroughQuery**| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional]
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

[**GetContactsResponse**](GetContactsResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contacts |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **contacts_delete**
> DeleteContactResponse contacts_delete(id)

Delete contact

Delete contact

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.delete_contact_response import DeleteContactResponse
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete contact
        api_response = api_instance.contacts_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->contacts_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete contact
        api_response = api_instance.contacts_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->contacts_delete: %s\n" % e)
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

[**DeleteContactResponse**](DeleteContactResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **contacts_one**
> GetContactResponse contacts_one(id)

Get contact

Get contact

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.get_contact_response import GetContactResponse
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get contact
        api_response = api_instance.contacts_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->contacts_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get contact
        api_response = api_instance.contacts_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->contacts_one: %s\n" % e)
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

[**GetContactResponse**](GetContactResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **contacts_update**
> UpdateContactResponse contacts_update(id, contact)

Update contact

Update contact

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.update_contact_response import UpdateContactResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.contact import Contact
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    contact = Contact(
        name="Elon Musk",
        owner_id="54321",
        type="personal",
        company_id="23456",
        company_name="23456",
        lead_id="34567",
        first_name="Elon",
        middle_name="D.",
        last_name="Musk",
        prefix="Mr.",
        suffix="PhD",
        title="CEO",
        department="Engineering",
        language="EN",
        gender="female",
        birthday="2000-08-12",
        image="https://unavatar.io/elon-musk",
        photo_url="https://unavatar.io/elon-musk",
        lead_source="Cold Call",
        fax="+12129876543",
        description="Internal champion",
        current_balance=10.5,
        status="open",
        active=True,
        websites=[
            Website(
                id="12345",
                url="http://example.com",
                type="primary",
            ),
        ],
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
                notes="Address notes or delivery instructions.",
                row_version="1-12345",
            ),
        ],
        social_links=[
            SocialLink(
                id="12345",
                url="https://www.twitter.com/apideck",
                type="twitter",
            ),
        ],
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
        email_domain="gmail.com",
        custom_fields=[
            CustomField(
                id="2389328923893298",
                name="employee_level",
                description="Employee Level",
                value=None,
            ),
        ],
        tags=Tags(["New"]),
    ) # Contact | 
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update contact
        api_response = api_instance.contacts_update(id, contact)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->contacts_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update contact
        api_response = api_instance.contacts_update(id, contact, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->contacts_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **contact** | [**Contact**](Contact.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateContactResponse**](UpdateContactResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **leads_add**
> CreateLeadResponse leads_add(lead)

Create lead

Create lead

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.create_lead_response import CreateLeadResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.lead import Lead
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
    api_instance = crm_api.CrmApi(api_client)
    lead = Lead(
        name="Elon Musk",
        company_name="Spacex",
        owner_id="54321",
        company_id="2",
        lead_id="2",
        lead_source="Cold Call",
        first_name="Elon",
        last_name="Musk",
        description="A thinker",
        prefix="Sir",
        title="CEO",
        language="EN",
        status="New",
        monetary_amount=75000,
        currency=Currency("USD"),
        fax="+12129876543",
        websites=[
            Website(
                id="12345",
                url="http://example.com",
                type="primary",
            ),
        ],
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
                notes="Address notes or delivery instructions.",
                row_version="1-12345",
            ),
        ],
        social_links=[
            SocialLink(
                id="12345",
                url="https://www.twitter.com/apideck",
                type="twitter",
            ),
        ],
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
        custom_fields=[
            CustomField(
                id="2389328923893298",
                name="employee_level",
                description="Employee Level",
                value=None,
            ),
        ],
        tags=Tags(["New"]),
    ) # Lead | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create lead
        api_response = api_instance.leads_add(lead)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->leads_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create lead
        api_response = api_instance.leads_add(lead, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->leads_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead** | [**Lead**](Lead.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateLeadResponse**](CreateLeadResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Lead created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **leads_all**
> GetLeadsResponse leads_all()

List leads

List leads

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.pass_through_query import PassThroughQuery
from apideck.model.leads_filter import LeadsFilter
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.get_leads_response import GetLeadsResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.leads_sort import LeadsSort
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
    api_instance = crm_api.CrmApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of results to return. Minimum 1, Maximum 200, Default 20 (optional) if omitted the server will use the default value of 20
    filter = LeadsFilter(
        name="Elon Musk",
        first_name="Elon",
        last_name="Musk",
        email="elon@tesla.com",
    ) # LeadsFilter | Apply filters (optional)
    sort = LeadsSort(
        by="created_at",
        direction=SortDirection("asc"),
    ) # LeadsSort | Apply sorting (optional)
    pass_through = PassThroughQuery() # PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List leads
        api_response = api_instance.leads_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, filter=filter, sort=sort, pass_through=pass_through, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->leads_all: %s\n" % e)
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
 **filter** | **LeadsFilter**| Apply filters | [optional]
 **sort** | **LeadsSort**| Apply sorting | [optional]
 **pass_through** | **PassThroughQuery**| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional]
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

[**GetLeadsResponse**](GetLeadsResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Leads |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **leads_delete**
> DeleteLeadResponse leads_delete(id)

Delete lead

Delete lead

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.delete_lead_response import DeleteLeadResponse
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete lead
        api_response = api_instance.leads_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->leads_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete lead
        api_response = api_instance.leads_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->leads_delete: %s\n" % e)
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

[**DeleteLeadResponse**](DeleteLeadResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lead deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **leads_one**
> GetLeadResponse leads_one(id)

Get lead

Get lead

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.get_lead_response import GetLeadResponse
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get lead
        api_response = api_instance.leads_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->leads_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get lead
        api_response = api_instance.leads_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->leads_one: %s\n" % e)
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

[**GetLeadResponse**](GetLeadResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lead |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **leads_update**
> UpdateLeadResponse leads_update(id, lead)

Update lead

Update lead

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.update_lead_response import UpdateLeadResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.lead import Lead
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    lead = Lead(
        name="Elon Musk",
        company_name="Spacex",
        owner_id="54321",
        company_id="2",
        lead_id="2",
        lead_source="Cold Call",
        first_name="Elon",
        last_name="Musk",
        description="A thinker",
        prefix="Sir",
        title="CEO",
        language="EN",
        status="New",
        monetary_amount=75000,
        currency=Currency("USD"),
        fax="+12129876543",
        websites=[
            Website(
                id="12345",
                url="http://example.com",
                type="primary",
            ),
        ],
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
                notes="Address notes or delivery instructions.",
                row_version="1-12345",
            ),
        ],
        social_links=[
            SocialLink(
                id="12345",
                url="https://www.twitter.com/apideck",
                type="twitter",
            ),
        ],
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
        custom_fields=[
            CustomField(
                id="2389328923893298",
                name="employee_level",
                description="Employee Level",
                value=None,
            ),
        ],
        tags=Tags(["New"]),
    ) # Lead | 
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update lead
        api_response = api_instance.leads_update(id, lead)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->leads_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update lead
        api_response = api_instance.leads_update(id, lead, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->leads_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **lead** | [**Lead**](Lead.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateLeadResponse**](UpdateLeadResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lead updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **notes_add**
> CreateNoteResponse notes_add(note)

Create note

Create note

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.note import Note
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.create_note_response import CreateNoteResponse
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
    api_instance = crm_api.CrmApi(api_client)
    note = Note(
        title="Meeting Notes",
        content="Office hours are 9AM-6PM",
        owner_id="12345",
        contact_id="12345",
        company_id="12345",
        opportunity_id="12345",
        lead_id="12345",
        active=True,
    ) # Note | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create note
        api_response = api_instance.notes_add(note)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->notes_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create note
        api_response = api_instance.notes_add(note, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->notes_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note** | [**Note**](Note.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateNoteResponse**](CreateNoteResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Note created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **notes_all**
> GetNotesResponse notes_all()

List notes

List notes

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.pass_through_query import PassThroughQuery
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.get_notes_response import GetNotesResponse
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
    api_instance = crm_api.CrmApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of results to return. Minimum 1, Maximum 200, Default 20 (optional) if omitted the server will use the default value of 20
    pass_through = PassThroughQuery() # PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List notes
        api_response = api_instance.notes_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, pass_through=pass_through, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->notes_all: %s\n" % e)
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

[**GetNotesResponse**](GetNotesResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Notes |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **notes_delete**
> DeleteNoteResponse notes_delete(id)

Delete note

Delete note

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.delete_note_response import DeleteNoteResponse
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete note
        api_response = api_instance.notes_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->notes_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete note
        api_response = api_instance.notes_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->notes_delete: %s\n" % e)
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

[**DeleteNoteResponse**](DeleteNoteResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Note deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **notes_one**
> GetNoteResponse notes_one(id)

Get note

Get note

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.get_note_response import GetNoteResponse
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get note
        api_response = api_instance.notes_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->notes_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get note
        api_response = api_instance.notes_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->notes_one: %s\n" % e)
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

[**GetNoteResponse**](GetNoteResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Note |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **notes_update**
> UpdateNoteResponse notes_update(id, note)

Update note

Update note

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.note import Note
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.update_note_response import UpdateNoteResponse
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    note = Note(
        title="Meeting Notes",
        content="Office hours are 9AM-6PM",
        owner_id="12345",
        contact_id="12345",
        company_id="12345",
        opportunity_id="12345",
        lead_id="12345",
        active=True,
    ) # Note | 
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update note
        api_response = api_instance.notes_update(id, note)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->notes_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update note
        api_response = api_instance.notes_update(id, note, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->notes_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **note** | [**Note**](Note.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateNoteResponse**](UpdateNoteResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Note updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **opportunities_add**
> CreateOpportunityResponse opportunities_add(opportunity)

Create opportunity

Create opportunity

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.create_opportunity_response import CreateOpportunityResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.opportunity import Opportunity
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
    api_instance = crm_api.CrmApi(api_client)
    opportunity = Opportunity(
        title="New Rocket",
        primary_contact_id="12345",
        description="Opportunities are created for People and Companies that are interested in buying your products or services. Create Opportunities for People and Companies to move them through one of your Pipelines.",
        type="Existing Customer - Upgrade",
        monetary_amount=75000,
        currency=Currency("USD"),
        win_probability=40,
        close_date=dateutil_parser('Fri Oct 30 00:00:00 UTC 2020').date(),
        loss_reason_id="12345",
        loss_reason="No budget",
        won_reason_id="12345",
        won_reason="Best pitch",
        pipeline_id="12345",
        pipeline_stage_id="12345",
        source_id="12345",
        lead_id="12345",
        lead_source="Website",
        contact_id="12345",
        contact_ids=[
            "12345",
        ],
        company_id="12345",
        company_name="Copper",
        owner_id="12345",
        priority="None",
        status="Open",
        status_id="12345",
        tags=Tags(["New"]),
        custom_fields=[
            CustomField(
                id="2389328923893298",
                name="employee_level",
                description="Employee Level",
                value=None,
            ),
        ],
        stage_last_changed_at=dateutil_parser('2020-09-30T07:43:32Z'),
    ) # Opportunity | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create opportunity
        api_response = api_instance.opportunities_add(opportunity)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->opportunities_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create opportunity
        api_response = api_instance.opportunities_add(opportunity, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->opportunities_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opportunity** | [**Opportunity**](Opportunity.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateOpportunityResponse**](CreateOpportunityResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Opportunity created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **opportunities_all**
> GetOpportunitiesResponse opportunities_all()

List opportunities

List opportunities

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.opportunities_sort import OpportunitiesSort
from apideck.model.pass_through_query import PassThroughQuery
from apideck.model.opportunities_filter import OpportunitiesFilter
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.get_opportunities_response import GetOpportunitiesResponse
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
    api_instance = crm_api.CrmApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of results to return. Minimum 1, Maximum 200, Default 20 (optional) if omitted the server will use the default value of 20
    filter = OpportunitiesFilter(
        title="Tesla deal",
        status="Completed",
        monetary_amount=75000,
        win_probability=50,
        company_id="1234",
    ) # OpportunitiesFilter | Apply filters (optional)
    sort = OpportunitiesSort(
        by="created_at",
        direction=SortDirection("asc"),
    ) # OpportunitiesSort | Apply sorting (optional)
    pass_through = PassThroughQuery() # PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List opportunities
        api_response = api_instance.opportunities_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, filter=filter, sort=sort, pass_through=pass_through, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->opportunities_all: %s\n" % e)
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
 **filter** | **OpportunitiesFilter**| Apply filters | [optional]
 **sort** | **OpportunitiesSort**| Apply sorting | [optional]
 **pass_through** | **PassThroughQuery**| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional]
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

[**GetOpportunitiesResponse**](GetOpportunitiesResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Opportunities |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **opportunities_delete**
> DeleteOpportunityResponse opportunities_delete(id)

Delete opportunity

Delete opportunity

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.delete_opportunity_response import DeleteOpportunityResponse
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete opportunity
        api_response = api_instance.opportunities_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->opportunities_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete opportunity
        api_response = api_instance.opportunities_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->opportunities_delete: %s\n" % e)
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

[**DeleteOpportunityResponse**](DeleteOpportunityResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Opportunity deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **opportunities_one**
> GetOpportunityResponse opportunities_one(id)

Get opportunity

Get opportunity

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.get_opportunity_response import GetOpportunityResponse
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get opportunity
        api_response = api_instance.opportunities_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->opportunities_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get opportunity
        api_response = api_instance.opportunities_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->opportunities_one: %s\n" % e)
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

[**GetOpportunityResponse**](GetOpportunityResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Opportunity |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **opportunities_update**
> UpdateOpportunityResponse opportunities_update(id, opportunity)

Update opportunity

Update opportunity

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.update_opportunity_response import UpdateOpportunityResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.opportunity import Opportunity
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    opportunity = Opportunity(
        title="New Rocket",
        primary_contact_id="12345",
        description="Opportunities are created for People and Companies that are interested in buying your products or services. Create Opportunities for People and Companies to move them through one of your Pipelines.",
        type="Existing Customer - Upgrade",
        monetary_amount=75000,
        currency=Currency("USD"),
        win_probability=40,
        close_date=dateutil_parser('Fri Oct 30 00:00:00 UTC 2020').date(),
        loss_reason_id="12345",
        loss_reason="No budget",
        won_reason_id="12345",
        won_reason="Best pitch",
        pipeline_id="12345",
        pipeline_stage_id="12345",
        source_id="12345",
        lead_id="12345",
        lead_source="Website",
        contact_id="12345",
        contact_ids=[
            "12345",
        ],
        company_id="12345",
        company_name="Copper",
        owner_id="12345",
        priority="None",
        status="Open",
        status_id="12345",
        tags=Tags(["New"]),
        custom_fields=[
            CustomField(
                id="2389328923893298",
                name="employee_level",
                description="Employee Level",
                value=None,
            ),
        ],
        stage_last_changed_at=dateutil_parser('2020-09-30T07:43:32Z'),
    ) # Opportunity | 
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update opportunity
        api_response = api_instance.opportunities_update(id, opportunity)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->opportunities_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update opportunity
        api_response = api_instance.opportunities_update(id, opportunity, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->opportunities_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **opportunity** | [**Opportunity**](Opportunity.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateOpportunityResponse**](UpdateOpportunityResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Opportunity updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **pipelines_add**
> CreatePipelineResponse pipelines_add(pipeline)

Create pipeline

Create pipeline

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.create_pipeline_response import CreatePipelineResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.pipeline import Pipeline
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
    api_instance = crm_api.CrmApi(api_client)
    pipeline = Pipeline(
        id="default",
        name="Sales Pipeline",
        currency=Currency("USD"),
        archived=False,
        active=False,
        display_order=1,
        win_probability_enabled=True,
        stages=[
            PipelineStages(
                name="Contract Sent",
                value="CONTRACT_SENT",
                win_probability=50,
                display_order=1,
            ),
        ],
    ) # Pipeline | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create pipeline
        api_response = api_instance.pipelines_add(pipeline)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->pipelines_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create pipeline
        api_response = api_instance.pipelines_add(pipeline, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->pipelines_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline** | [**Pipeline**](Pipeline.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreatePipelineResponse**](CreatePipelineResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Pipeline created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **pipelines_all**
> GetPipelinesResponse pipelines_all()

List pipelines

List pipelines

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.pass_through_query import PassThroughQuery
from apideck.model.get_pipelines_response import GetPipelinesResponse
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
    api_instance = crm_api.CrmApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of results to return. Minimum 1, Maximum 200, Default 20 (optional) if omitted the server will use the default value of 20
    pass_through = PassThroughQuery() # PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List pipelines
        api_response = api_instance.pipelines_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, pass_through=pass_through, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->pipelines_all: %s\n" % e)
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

[**GetPipelinesResponse**](GetPipelinesResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pipelines |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **pipelines_delete**
> DeletePipelineResponse pipelines_delete(id)

Delete pipeline

Delete pipeline

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.delete_pipeline_response import DeletePipelineResponse
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete pipeline
        api_response = api_instance.pipelines_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->pipelines_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete pipeline
        api_response = api_instance.pipelines_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->pipelines_delete: %s\n" % e)
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

[**DeletePipelineResponse**](DeletePipelineResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pipeline deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **pipelines_one**
> GetPipelineResponse pipelines_one(id)

Get pipeline

Get pipeline

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.get_pipeline_response import GetPipelineResponse
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get pipeline
        api_response = api_instance.pipelines_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->pipelines_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get pipeline
        api_response = api_instance.pipelines_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->pipelines_one: %s\n" % e)
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

[**GetPipelineResponse**](GetPipelineResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pipeline |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **pipelines_update**
> UpdatePipelineResponse pipelines_update(id, pipeline)

Update pipeline

Update pipeline

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.update_pipeline_response import UpdatePipelineResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.pipeline import Pipeline
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    pipeline = Pipeline(
        id="default",
        name="Sales Pipeline",
        currency=Currency("USD"),
        archived=False,
        active=False,
        display_order=1,
        win_probability_enabled=True,
        stages=[
            PipelineStages(
                name="Contract Sent",
                value="CONTRACT_SENT",
                win_probability=50,
                display_order=1,
            ),
        ],
    ) # Pipeline | 
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update pipeline
        api_response = api_instance.pipelines_update(id, pipeline)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->pipelines_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update pipeline
        api_response = api_instance.pipelines_update(id, pipeline, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->pipelines_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **pipeline** | [**Pipeline**](Pipeline.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdatePipelineResponse**](UpdatePipelineResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pipeline updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **users_add**
> CreateUserResponse users_add(user)

Create user

Create user

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.create_user_response import CreateUserResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.user import User
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
    api_instance = crm_api.CrmApi(api_client)
    user = User(
        parent_id="54321",
        username="masterofcoin",
        first_name="Elon",
        last_name="Musk",
        title="CEO",
        division="Europe",
        department="R&D",
        company_name="SpaceX",
        employee_number="123456-AB",
        description="A description",
        image="https://logo.clearbit.com/spacex.com?s=128",
        language="EN",
        status="active",
        password="supersecretpassword",
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
                notes="Address notes or delivery instructions.",
                row_version="1-12345",
            ),
        ],
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
    ) # User | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create user
        api_response = api_instance.users_add(user)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->users_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create user
        api_response = api_instance.users_add(user, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->users_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **users_all**
> GetUsersResponse users_all()

List users

List users

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.pass_through_query import PassThroughQuery
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.get_users_response import GetUsersResponse
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
    api_instance = crm_api.CrmApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of results to return. Minimum 1, Maximum 200, Default 20 (optional) if omitted the server will use the default value of 20
    pass_through = PassThroughQuery() # PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List users
        api_response = api_instance.users_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, pass_through=pass_through, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->users_all: %s\n" % e)
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

[**GetUsersResponse**](GetUsersResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **users_delete**
> DeleteUserResponse users_delete(id)

Delete user

Delete user

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.delete_user_response import DeleteUserResponse
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete user
        api_response = api_instance.users_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->users_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete user
        api_response = api_instance.users_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->users_delete: %s\n" % e)
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

[**DeleteUserResponse**](DeleteUserResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **users_one**
> GetUserResponse users_one(id)

Get user

Get user

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.get_user_response import GetUserResponse
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get user
        api_response = api_instance.users_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->users_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get user
        api_response = api_instance.users_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->users_one: %s\n" % e)
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

[**GetUserResponse**](GetUserResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **users_update**
> UpdateUserResponse users_update(id, user)

Update user

Update user

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import crm_api
from apideck.model.update_user_response import UpdateUserResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.user import User
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
    api_instance = crm_api.CrmApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    user = User(
        parent_id="54321",
        username="masterofcoin",
        first_name="Elon",
        last_name="Musk",
        title="CEO",
        division="Europe",
        department="R&D",
        company_name="SpaceX",
        employee_number="123456-AB",
        description="A description",
        image="https://logo.clearbit.com/spacex.com?s=128",
        language="EN",
        status="active",
        password="supersecretpassword",
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
                notes="Address notes or delivery instructions.",
                row_version="1-12345",
            ),
        ],
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
    ) # User | 
    consumer_id = "x-apideck-consumer-id_example" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "x-apideck-service-id_example" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update user
        api_response = api_instance.users_update(id, user)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->users_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update user
        api_response = api_instance.users_update(id, user, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->users_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **user** | [**User**](User.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateUserResponse**](UpdateUserResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

