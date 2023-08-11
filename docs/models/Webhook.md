# Webhook


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unified_api** | [**UnifiedApiId**](UnifiedApiId.md) |  | 
**status** | [**Status**](Status.md) |  | 
**delivery_url** | [**DeliveryUrl**](DeliveryUrl.md) |  | 
**execute_base_url** | [**ExecuteBaseUrl**](ExecuteBaseUrl.md) |  | 
**events** | [**[WebhookEventType]**](WebhookEventType.md) | The list of subscribed events for this webhook. [&#x60;*&#x60;] indicates that all events are enabled. | 
**id** | **str** |  | [optional] [readonly] 
**description** | **str, none_type** | A description of the object. | [optional] 
**disabled_reason** | **str** | Indicates if the webhook has has been disabled as it reached its retry limit or if account is over the usage allocated by it&#39;s plan. | [optional] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


