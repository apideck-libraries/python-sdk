# AccountingDepartment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**parent_id** | **str, none_type** | A unique identifier for an object. | [optional] 
**name** | **str, none_type** | The name of the department. | [optional] 
**status** | **str** | Based on the status some functionality is enabled or disabled. | [optional] 
**subsidiaries** | [**[SubsidiaryReference]**](SubsidiaryReference.md) |  | [optional] 
**code** | **str** | The code of the department. | [optional] 
**custom_mappings** | [**CustomMappings**](CustomMappings.md) |  | [optional] 
**row_version** | **str, none_type** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**pass_through** | [**PassThroughBody**](PassThroughBody.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


