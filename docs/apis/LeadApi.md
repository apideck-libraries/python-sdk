# apideck.LeadApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**leads_add**](LeadApi.md#leads_add) | **POST** /lead/leads | Create lead
[**leads_all**](LeadApi.md#leads_all) | **GET** /lead/leads | List leads
[**leads_delete**](LeadApi.md#leads_delete) | **DELETE** /lead/leads/{id} | Delete lead
[**leads_one**](LeadApi.md#leads_one) | **GET** /lead/leads/{id} | Get lead
[**leads_update**](LeadApi.md#leads_update) | **PATCH** /lead/leads/{id} | Update lead


# **leads_add**
> CreateLeadResponse leads_add(lead)

Create lead

Create lead

### Example

* Api Key Authentication (apiKey):

```python
import time
import apideck
from apideck.api import lead_api
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
    api_instance = lead_api.LeadApi(api_client)
    lead = Lead(
        name="Elon Musk",
        company_name="Spacex",
        owner_id="54321",
        company_id="2",
        contact_id="2",
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
                url="https://www.twitter.com/apideck-io",
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
        print("Exception when calling LeadApi->leads_add: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create lead
        api_response = api_instance.leads_add(lead, raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling LeadApi->leads_add: %s\n" % e)
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
from apideck.api import lead_api
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
    api_instance = lead_api.LeadApi(api_client)
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
    fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List leads
        api_response = api_instance.leads_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, cursor=cursor, limit=limit, filter=filter, sort=sort, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling LeadApi->leads_all: %s\n" % e)
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
from apideck.api import lead_api
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
    api_instance = lead_api.LeadApi(api_client)
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
        print("Exception when calling LeadApi->leads_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete lead
        api_response = api_instance.leads_delete(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling LeadApi->leads_delete: %s\n" % e)
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
from apideck.api import lead_api
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
    api_instance = lead_api.LeadApi(api_client)
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
        print("Exception when calling LeadApi->leads_one: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get lead
        api_response = api_instance.leads_one(id, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling LeadApi->leads_one: %s\n" % e)
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
from apideck.api import lead_api
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
    api_instance = lead_api.LeadApi(api_client)
    id = "id_example" # str | ID of the record you are acting upon.
    lead = Lead(
        name="Elon Musk",
        company_name="Spacex",
        owner_id="54321",
        company_id="2",
        contact_id="2",
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
                url="https://www.twitter.com/apideck-io",
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
        print("Exception when calling LeadApi->leads_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update lead
        api_response = api_instance.leads_update(id, lead, consumer_id=consumer_id, app_id=app_id, service_id=service_id, raw=raw)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling LeadApi->leads_update: %s\n" % e)
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

