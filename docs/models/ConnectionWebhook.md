# ConnectionWebhook


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unified_api** | [**UnifiedApiId**](UnifiedApiId.md) |  | 
**status** | **str** | The status of the webhook. | 
**delivery_url** | **str** | The delivery url of the webhook endpoint. | 
**execute_base_url** | **str** | The Unify Base URL events from connectors will be sent to after service id is appended. | [readonly] 
**events** | **[str]** | The list of subscribed events for this webhook. [&#x60;*&#x60;] indicates that all events are enabled. | 
**id** | **str** |  | [optional] [readonly] 
**description** | **str, none_type** |  | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


