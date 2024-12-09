# apideck.AtsApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicants_add**](AtsApi.md#applicants_add) | **POST** /ats/applicants | Create Applicant
[**applicants_all**](AtsApi.md#applicants_all) | **GET** /ats/applicants | List Applicants
[**applicants_delete**](AtsApi.md#applicants_delete) | **DELETE** /ats/applicants/{id} | Delete Applicant
[**applicants_one**](AtsApi.md#applicants_one) | **GET** /ats/applicants/{id} | Get Applicant
[**applicants_update**](AtsApi.md#applicants_update) | **PATCH** /ats/applicants/{id} | Update Applicant
[**applications_add**](AtsApi.md#applications_add) | **POST** /ats/applications | Create Application
[**applications_all**](AtsApi.md#applications_all) | **GET** /ats/applications | List Applications
[**applications_delete**](AtsApi.md#applications_delete) | **DELETE** /ats/applications/{id} | Delete Application
[**applications_one**](AtsApi.md#applications_one) | **GET** /ats/applications/{id} | Get Application
[**applications_update**](AtsApi.md#applications_update) | **PATCH** /ats/applications/{id} | Update Application
[**jobs_all**](AtsApi.md#jobs_all) | **GET** /ats/jobs | List Jobs
[**jobs_one**](AtsApi.md#jobs_one) | **GET** /ats/jobs/{id} | Get Job


# **applicants_add**
> CreateApplicantResponse applicants_add(applicant)

Create Applicant

Create Applicant

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import ats_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.create_applicant_response import CreateApplicantResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.applicant import Applicant
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
    api_instance = ats_api.AtsApi(api_client)
    applicant = Applicant(
        name="Elon Musk",
        first_name="Elon",
        last_name="Musk",
        middle_name="D.",
        initials="EM",
        birthday=dateutil_parser('Sat Aug 12 00:00:00 UTC 2000').date(),
        cover_letter="I submit this application to express my sincere interest in the API developer position. In the previous role, I was responsible for leadership and ...",
        photo_url="https://unavatar.io/elon-musk",
        headline="PepsiCo, Inc, Central Perk",
        title="CEO",
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
        websites=[
            ApplicantWebsites(
                id="12345",
                url="http://example.com",
                type="primary",
            ),
        ],
        social_links=[
            ApplicantSocialLinks(
                id="12345",
                url="https://www.twitter.com/apideck",
                type="twitter",
            ),
        ],
        stage_id="12345",
        recruiter_id="12345",
        coordinator_id="12345",
        application_ids=["a0d636c6-43b3-4bde-8c70-85b707d992f4","a98lfd96-43b3-4bde-8c70-85b707d992e6"],
        applications=["a0d636c6-43b3-4bde-8c70-85b707d992f4","a98lfd96-43b3-4bde-8c70-85b707d992e6"],
        followers=["a0d636c6-43b3-4bde-8c70-85b707d992f4","a98lfd96-43b3-4bde-8c70-85b707d992e6"],
        sources=["Job site"],
        confidential=False,
        anonymized=True,
        tags=Tags(["New"]),
        archived=False,
        owner_id="54321",
        record_url="https://app.intercom.io/contacts/12345",
        deleted=True,
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
    ) # Applicant | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Applicant
        api_response = api_instance.applicants_add(applicant)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->applicants_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Applicant
        api_response = api_instance.applicants_add(applicant, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->applicants_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant** | [**Applicant**](Applicant.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateApplicantResponse**](CreateApplicantResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Applicants |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **applicants_all**
> GetApplicantsResponse applicants_all()

List Applicants

List Applicants

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import ats_api
from apideck.model.applicants_filter import ApplicantsFilter
from apideck.model.pass_through_query import PassThroughQuery
from apideck.model.get_applicants_response import GetApplicantsResponse
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
    api_instance = ats_api.AtsApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    limit = 20 # int | Number of results to return. Minimum 1, Maximum 200, Default 20 (optional) if omitted the server will use the default value of 20
    filter = ApplicantsFilter(
        job_id="1234",
    ) # ApplicantsFilter | Apply filters (optional)
    pass_through = PassThroughQuery() # PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads (optional)
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Applicants
        api_response = api_instance.applicants_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, filter=filter, pass_through=pass_through, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->applicants_all: %s\n" % e)
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
 **filter** | **ApplicantsFilter**| Apply filters | [optional]
 **pass_through** | **PassThroughQuery**| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional]
 **fields** | **str, none_type**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional]

### Return type

[**GetApplicantsResponse**](GetApplicantsResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Applicants |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **applicants_delete**
> DeleteApplicantResponse applicants_delete(id)

Delete Applicant

Delete Applicant

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import ats_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.delete_applicant_response import DeleteApplicantResponse
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
    api_instance = ats_api.AtsApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete Applicant
        api_response = api_instance.applicants_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->applicants_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Applicant
        api_response = api_instance.applicants_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->applicants_delete: %s\n" % e)
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

[**DeleteApplicantResponse**](DeleteApplicantResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Applicants |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **applicants_one**
> GetApplicantResponse applicants_one(id)

Get Applicant

Get Applicant

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import ats_api
from apideck.model.get_applicant_response import GetApplicantResponse
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
    api_instance = ats_api.AtsApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Applicant
        api_response = api_instance.applicants_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->applicants_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Applicant
        api_response = api_instance.applicants_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->applicants_one: %s\n" % e)
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

[**GetApplicantResponse**](GetApplicantResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Applicants |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **applicants_update**
> UpdateApplicantResponse applicants_update(id, applicant)

Update Applicant

Update Applicant

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import ats_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.applicant import Applicant
from apideck.model.update_applicant_response import UpdateApplicantResponse
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
    api_instance = ats_api.AtsApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    applicant = Applicant(
        name="Elon Musk",
        first_name="Elon",
        last_name="Musk",
        middle_name="D.",
        initials="EM",
        birthday=dateutil_parser('Sat Aug 12 00:00:00 UTC 2000').date(),
        cover_letter="I submit this application to express my sincere interest in the API developer position. In the previous role, I was responsible for leadership and ...",
        photo_url="https://unavatar.io/elon-musk",
        headline="PepsiCo, Inc, Central Perk",
        title="CEO",
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
        websites=[
            ApplicantWebsites(
                id="12345",
                url="http://example.com",
                type="primary",
            ),
        ],
        social_links=[
            ApplicantSocialLinks(
                id="12345",
                url="https://www.twitter.com/apideck",
                type="twitter",
            ),
        ],
        stage_id="12345",
        recruiter_id="12345",
        coordinator_id="12345",
        application_ids=["a0d636c6-43b3-4bde-8c70-85b707d992f4","a98lfd96-43b3-4bde-8c70-85b707d992e6"],
        applications=["a0d636c6-43b3-4bde-8c70-85b707d992f4","a98lfd96-43b3-4bde-8c70-85b707d992e6"],
        followers=["a0d636c6-43b3-4bde-8c70-85b707d992f4","a98lfd96-43b3-4bde-8c70-85b707d992e6"],
        sources=["Job site"],
        confidential=False,
        anonymized=True,
        tags=Tags(["New"]),
        archived=False,
        owner_id="54321",
        record_url="https://app.intercom.io/contacts/12345",
        deleted=True,
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
    ) # Applicant | 
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update Applicant
        api_response = api_instance.applicants_update(id, applicant)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->applicants_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Applicant
        api_response = api_instance.applicants_update(id, applicant, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->applicants_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **applicant** | [**Applicant**](Applicant.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateApplicantResponse**](UpdateApplicantResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Applicants |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **applications_add**
> CreateApplicationResponse applications_add(application)

Create Application

Create Application

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import ats_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.create_application_response import CreateApplicationResponse
from apideck.model.application import Application
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
    api_instance = ats_api.AtsApi(api_client)
    application = Application(
        applicant_id="12345",
        job_id="12345",
        status="open",
        stage=ApplicationStage(
            id="12345",
            name="12345",
        ),
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
    ) # Application | 
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Application
        api_response = api_instance.applications_add(application)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->applications_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Application
        api_response = api_instance.applications_add(application, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->applications_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | [**Application**](Application.md)|  |
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]

### Return type

[**CreateApplicationResponse**](CreateApplicationResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Applications |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **applications_all**
> GetApplicationsResponse applications_all()

List Applications

List Applications

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import ats_api
from apideck.model.get_applications_response import GetApplicationsResponse
from apideck.model.pass_through_query import PassThroughQuery
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
    api_instance = ats_api.AtsApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    cursor = "cursor_example" # str, none_type | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
    pass_through = PassThroughQuery() # PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads (optional)
    limit = 20 # int | Number of results to return. Minimum 1, Maximum 200, Default 20 (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Applications
        api_response = api_instance.applications_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, pass_through=pass_through, limit=limit)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->applications_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **cursor** | **str, none_type**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional]
 **pass_through** | **PassThroughQuery**| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional]
 **limit** | **int**| Number of results to return. Minimum 1, Maximum 200, Default 20 | [optional] if omitted the server will use the default value of 20

### Return type

[**GetApplicationsResponse**](GetApplicationsResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Applications |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **applications_delete**
> DeleteApplicationResponse applications_delete(id)

Delete Application

Delete Application

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import ats_api
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.delete_application_response import DeleteApplicationResponse
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
    api_instance = ats_api.AtsApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete Application
        api_response = api_instance.applications_delete(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->applications_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Application
        api_response = api_instance.applications_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->applications_delete: %s\n" % e)
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

[**DeleteApplicationResponse**](DeleteApplicationResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Applications |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **applications_one**
> GetApplicationResponse applications_one(id)

Get Application

Get Application

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import ats_api
from apideck.model.get_application_response import GetApplicationResponse
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
    api_instance = ats_api.AtsApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get Application
        api_response = api_instance.applications_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->applications_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Application
        api_response = api_instance.applications_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->applications_one: %s\n" % e)
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

[**GetApplicationResponse**](GetApplicationResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Applications |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **applications_update**
> UpdateApplicationResponse applications_update(id, application)

Update Application

Update Application

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import ats_api
from apideck.model.update_application_response import UpdateApplicationResponse
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.application import Application
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
    api_instance = ats_api.AtsApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    application = Application(
        applicant_id="12345",
        job_id="12345",
        status="open",
        stage=ApplicationStage(
            id="12345",
            name="12345",
        ),
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
    ) # Application | 
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update Application
        api_response = api_instance.applications_update(id, application)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->applications_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Application
        api_response = api_instance.applications_update(id, application, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->applications_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the record you are acting upon. |
 **application** | [**Application**](Application.md)|  |
 **consumer_id** | **str**| ID of the consumer which you want to get or push data from | [optional]
 **app_id** | **str**| The ID of your Unify application | [optional]
 **service_id** | **str**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional]
 **raw** | **bool**| Include raw response. Mostly used for debugging purposes | [optional] if omitted the server will use the default value of False

### Return type

[**UpdateApplicationResponse**](UpdateApplicationResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Applications |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **jobs_all**
> GetJobsResponse jobs_all()

List Jobs

List Jobs

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import ats_api
from apideck.model.pass_through_query import PassThroughQuery
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.get_jobs_response import GetJobsResponse
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
    api_instance = ats_api.AtsApi(api_client)
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
        # List Jobs
        api_response = api_instance.jobs_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, pass_through=pass_through, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->jobs_all: %s\n" % e)
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

[**GetJobsResponse**](GetJobsResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Jobs |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **jobs_one**
> GetJobResponse jobs_one(id)

Get Job

Get Job

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import ats_api
from apideck.model.get_job_response import GetJobResponse
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
    api_instance = ats_api.AtsApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
    app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
    service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) if omitted the server will use the default value of False
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Job
        api_response = api_instance.jobs_one(id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->jobs_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Job
        api_response = api_instance.jobs_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AtsApi->jobs_one: %s\n" % e)
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

[**GetJobResponse**](GetJobResponse.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Jobs |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**404** | The specified resource was not found |  -  |
**422** | Unprocessable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

