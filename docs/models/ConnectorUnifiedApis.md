# ConnectorUnifiedApis


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**UnifiedApiId**](UnifiedApiId.md) |  | [optional] 
**name** | **str** | Name of the API. | [optional] 
**oauth_scopes** | [**[ConnectorOauthScopes1]**](ConnectorOauthScopes1.md) |  | [optional] 
**supported_resources** | [**[LinkedConnectorResource]**](LinkedConnectorResource.md) | List of resources that are supported on the connector. | [optional] 
**downstream_unsupported_resources** | **[str]** | List of resources that are not supported on the downstream. | [optional] 
**supported_events** | [**[ConnectorEvent]**](ConnectorEvent.md) | List of events that are supported on the connector for this Unified API. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


