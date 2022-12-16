# Connector


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the connector. | [optional] [readonly] 
**name** | **str** | Name of the connector. | [optional] 
**status** | [**ConnectorStatus**](ConnectorStatus.md) |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**icon_url** | **str** | Link to a small square icon for the connector. | [optional] 
**logo_url** | **str** | Link to the full logo for the connector. | [optional] 
**website_url** | **str** | Link to the connector&#39;s website. | [optional] 
**signup_url** | **str** | Link to the connector&#39;s signup page. | [optional] 
**free_trial_available** | **bool** | Set to &#x60;true&#x60; when the connector offers a free trial. Use &#x60;signup_url&#x60; to sign up for a free trial | [optional] 
**auth_type** | **str** | Type of authorization used by the connector | [optional] [readonly] 
**auth_only** | **bool** | Indicates whether a connector only supports authentication. In this case the connector is not mapped to a Unified API, but can be used with the Proxy API | [optional] [readonly] 
**blind_mapped** | **bool** | Set to &#x60;true&#x60; when connector was implemented from downstream docs only and without API access. This state indicates that integration will require Apideck support, and access to downstream API to validate mapping quality. | [optional] [readonly] 
**oauth_grant_type** | **str** | OAuth grant type used by the connector. More info: https://oauth.net/2/grant-types | [optional] [readonly] 
**oauth_credentials_source** | **str** | Location of the OAuth client credentials. For most connectors the OAuth client credentials are stored on integration and managed by the application owner. For others they are stored on connection and managed by the consumer in Vault. | [optional] [readonly] 
**oauth_scopes** | [**[ConnectorOauthScopes]**](ConnectorOauthScopes.md) | List of OAuth Scopes available for this connector. | [optional] 
**custom_scopes** | **bool** | Set to &#x60;true&#x60; when connector allows the definition of custom scopes. | [optional] [readonly] 
**has_sandbox_credentials** | **bool** | Indicates whether Apideck Sandbox OAuth credentials are available. | [optional] 
**settings** | [**[ConnectorSetting]**](ConnectorSetting.md) |  | [optional] 
**service_id** | **str** | Service provider identifier | [optional] 
**unified_apis** | [**[ConnectorUnifiedApis]**](ConnectorUnifiedApis.md) | List of Unified APIs that feature this connector. | [optional] 
**supported_resources** | [**[LinkedConnectorResource]**](LinkedConnectorResource.md) | List of resources that are supported on the connector. | [optional] 
**configurable_resources** | **[str]** | List of resources that have settings that can be configured. | [optional] 
**supported_events** | [**[ConnectorEvent]**](ConnectorEvent.md) | List of events that are supported on the connector across all Unified APIs. | [optional] 
**webhook_support** | [**[WebhookSupport]**](WebhookSupport.md) | How webhooks are supported for the connector. Sometimes the connector natively supports webhooks, other times Apideck virtualizes them based on polling. | [optional] 
**docs** | [**[ConnectorDoc]**](ConnectorDoc.md) |  | [optional] 
**tls_support** | [**ConnectorTlsSupport**](ConnectorTlsSupport.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


