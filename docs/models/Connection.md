# Connection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the connection. | [optional] [readonly] 
**service_id** | **str** | The ID of the service this connection belongs to. | [optional] [readonly] 
**name** | **str** | The name of the connection | [optional] [readonly] 
**tag_line** | **str** |  | [optional] [readonly] 
**unified_api** | **str** | The unified API category where the connection belongs to. | [optional] [readonly] 
**state** | [**ConnectionState**](ConnectionState.md) |  | [optional] 
**integration_state** | [**IntegrationState**](IntegrationState.md) |  | [optional] 
**auth_type** | [**AuthType**](AuthType.md) |  | [optional] 
**oauth_grant_type** | [**OAuthGrantType**](OAuthGrantType.md) |  | [optional] 
**status** | **str** | Status of the connection. | [optional] [readonly] 
**enabled** | **bool** | Whether the connection is enabled or not. You can enable or disable a connection using the Update Connection API. | [optional] 
**website** | **str** | The website URL of the connection | [optional] [readonly] 
**icon** | **str** | A visual icon of the connection, that will be shown in the Vault | [optional] [readonly] 
**logo** | **str** | The logo of the connection, that will be shown in the Vault | [optional] [readonly] 
**authorize_url** | **str, none_type** | The OAuth redirect URI. Redirect your users to this URI to let them authorize your app in the connector&#39;s UI. Before you can use this URI, you must add &#x60;redirect_uri&#x60; as a query parameter. Your users will be redirected to this &#x60;redirect_uri&#x60; after they granted access to your app in the connector&#39;s UI. | [optional] [readonly] 
**revoke_url** | **str, none_type** | The OAuth revoke URI. Redirect your users to this URI to revoke this connection. Before you can use this URI, you must add &#x60;redirect_uri&#x60; as a query parameter. Your users will be redirected to this &#x60;redirect_uri&#x60; after they granted access to your app in the connector&#39;s UI. | [optional] [readonly] 
**settings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Connection settings. Values will persist to &#x60;form_fields&#x60; with corresponding id | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Attach your own consumer specific metadata | [optional] 
**form_fields** | [**[FormField]**](FormField.md) | The settings that are wanted to create a connection. | [optional] [readonly] 
**configuration** | [**[ConnectionConfiguration]**](ConnectionConfiguration.md) |  | [optional] 
**configurable_resources** | **[str]** |  | [optional] [readonly] 
**resource_schema_support** | **[str]** |  | [optional] [readonly] 
**resource_settings_support** | **[str]** |  | [optional] [readonly] 
**settings_required_for_authorization** | **[str]** | List of settings that are required to be configured on integration before authorization can occur | [optional] [readonly] 
**subscriptions** | [**[WebhookSubscription]**](WebhookSubscription.md) |  | [optional] [readonly] 
**has_guide** | **bool** | Whether the connector has a guide available in the developer docs or not (https://docs.apideck.com/connectors/{service_id}/docs/consumer+connection). | [optional] [readonly] 
**created_at** | **float** |  | [optional] [readonly] 
**updated_at** | **float, none_type** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


