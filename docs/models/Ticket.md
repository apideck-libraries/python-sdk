# Ticket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [readonly] 
**parent_id** | **str, none_type** | The ticket&#39;s parent ID | [optional] 
**collection_id** | **str, none_type** | The ticket&#39;s collection ID | [optional] [readonly] 
**type** | **str, none_type** | The ticket&#39;s type | [optional] 
**subject** | **str, none_type** | Subject of the ticket | [optional] 
**description** | **str, none_type** | The ticket&#39;s description. HTML version of description is mapped if supported by the third-party platform | [optional] 
**status** | **str, none_type** | The current status of the ticket. Possible values include: open, in_progress, closed, or - in cases where there is no clear mapping - the original value passed through. | [optional] 
**priority** | **str, none_type** | Priority of the ticket | [optional] 
**assignees** | [**[Assignee]**](Assignee.md) |  | [optional] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**due_date** | **datetime, none_type** | Due date of the ticket | [optional] 
**completed_at** | **datetime, none_type** | When the ticket was completed | [optional] [readonly] 
**tags** | [**[CollectionTag]**](CollectionTag.md) |  | [optional] 
**custom_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | When custom mappings are configured on the resource, the result is included here. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


