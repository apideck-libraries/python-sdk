# Ticket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [readonly] 
**parent_id** | **str** | The ticket&#39;s parent ID | [optional] 
**collection_id** | **str** | The ticket&#39;s collection ID | [optional] [readonly] 
**type** | **str** | The ticket&#39;s type | [optional] 
**subject** | **str** | Subject of the ticket | [optional] 
**description** | **str** | The ticket&#39;s description. HTML version of description is mapped if supported by the third-party platform | [optional] 
**status** | **str, none_type** | The current status of the ticket. Possible values include: open, in_progress, closed, or - in cases where there is no clear mapping - the original value passed through. | [optional] 
**priority** | **str** | Priority of the ticket | [optional] 
**assignees** | [**[Assignee]**](Assignee.md) |  | [optional] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime** | The date and time when the object was created. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**due_date** | **datetime, none_type** | Due date of the ticket | [optional] 
**completed_at** | **datetime, none_type** | When the ticket was completed | [optional] [readonly] 
**tags** | [**[CollectionTag]**](CollectionTag.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

