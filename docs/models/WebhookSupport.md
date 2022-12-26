# WebhookSupport

How webhooks are supported for the connector. Sometimes the connector natively supports webhooks, other times Apideck virtualizes them based on polling.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Mode of the webhook support. | [optional] 
**subscription_level** | **str** | Received events are scoped to connection or across integration. | [optional] 
**managed_via** | **str** | How the subscription is managed in the downstream. | [optional] 
**virtual_webhooks** | [**VirtualWebhooks**](VirtualWebhooks.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


