# WebhookEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Unique reference to this request event | [optional] 
**unified_api** | **str** | Name of Apideck Unified API | [optional] 
**service_id** | **str** | Service provider identifier | [optional] 
**consumer_id** | **str** | Unique consumer identifier. You can freely choose a consumer ID yourself. Most of the time, this is an ID of your internal data model that represents a user or account in your system (for example account:12345). If the consumer doesn&#39;t exist yet, Vault will upsert a consumer based on your ID. | [optional] 
**entity_id** | **str** | The service provider&#39;s ID of the entity that triggered this event | [optional] 
**entity_type** | **str** | The type entity that triggered this event | [optional] 
**entity_url** | **str** | The url to retrieve entity detail. | [optional] 
**execution_attempt** | **float** | The current count this request event has been attempted | [optional] 
**occurred_at** | **str** | ISO Datetime for when the original event occurred | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


