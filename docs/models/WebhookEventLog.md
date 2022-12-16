# WebhookEventLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status_code** | **int** | HTTP Status code that was returned. | [optional] 
**success** | **bool** | Whether or not the request was successful. | [optional] 
**application_id** | **str** | ID of your Apideck Application | [optional] 
**consumer_id** | **str** | Consumer identifier | [optional] 
**unified_api** | [**UnifiedApiId**](UnifiedApiId.md) |  | [optional] 
**service** | [**WebhookEventLogService**](WebhookEventLogService.md) |  | [optional] 
**endpoint** | **str** | The URL of the webhook endpoint. | [optional] 
**event_type** | **str** | Name of source event that webhook is subscribed to. | [optional] 
**execution_attempt** | **float** | Number of attempts webhook endpoint was called before a success was returned or eventually failed | [optional] 
**http_method** | **str** | HTTP Method of request to endpoint. | [optional] 
**timestamp** | **str** | ISO Date and time when the request was made. | [optional] 
**entity_type** | **str** | Name of the Entity described by the attributes delivered within payload | [optional] 
**request_body** | **str** | The JSON stringified payload that was delivered to the webhook endpoint. | [optional] 
**response_body** | **str** | The JSON stringified response that was returned from the webhook endpoint. | [optional] 
**retry_scheduled** | **bool** | If the request has not hit the max retry limit and will be retried. | [optional] 
**attempts** | [**[WebhookEventLogAttempts]**](WebhookEventLogAttempts.md) | record of each attempt to call webhook endpoint | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


