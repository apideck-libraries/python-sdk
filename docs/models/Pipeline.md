# Pipeline


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Pipeline. | 
**id** | **str** | The unique identifier of the Pipeline. | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**archived** | **bool** | Whether the Pipeline is archived or not. | [optional] 
**active** | **bool** | Whether the Pipeline is active or not. | [optional] 
**display_order** | **int, none_type** | The order in which the Pipeline is displayed in the UI. | [optional] 
**win_probability_enabled** | **bool** | Whether the Pipeline has win probability enabled or not. | [optional] 
**stages** | [**[PipelineStages]**](PipelineStages.md) | The Pipeline Stages. | [optional] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


