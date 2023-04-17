# ConnectorEvent

Unify event that is supported on the connector. Events are delivered via Webhooks.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | Unify event type | [optional] 
**event_source** | **str** | Unify event source | [optional] 
**downstream_event_type** | **str** | Downstream event type | [optional] 
**resources** | **[str]** |  | [optional] 
**entity_type** | **str** | Unify entity type | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


