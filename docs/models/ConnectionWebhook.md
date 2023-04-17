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
**description** | **str, none_type** | A description of the object. | [optional] 
**disabled_reason** | **str** | Indicates if the webhook has has been disabled as it reached its retry limit or if account is over the usage allocated by it&#39;s plan. | [optional] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime** | The date and time when the object was created. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


