# TimeOffRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**employee_id** | **str** | ID of the employee | [optional] 
**policy_id** | **str** | ID of the policy | [optional] 
**status** | **str** | The status of the time off request. | [optional] 
**description** | **str** | Description of the time off request. | [optional] 
**start_date** | **str** | The start date of the time off request. | [optional] 
**end_date** | **str** | The end date of the time off request. | [optional] 
**request_date** | **str** | The date the request was made. | [optional] 
**request_type** | **str** | The type of request | [optional] 
**approval_date** | **str** | The date the request was approved | [optional] 
**units** | **str** | The unit of time off requested. Possible values include: &#x60;hours&#x60;, &#x60;days&#x60;, or &#x60;other&#x60;. | [optional] 
**amount** | **float** | The amount of time off requested. | [optional] 
**notes** | [**TimeOffRequestNotes**](TimeOffRequestNotes.md) |  | [optional] 
**updated_by** | **str, none_type** |  | [optional] [readonly] 
**created_by** | **str, none_type** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


