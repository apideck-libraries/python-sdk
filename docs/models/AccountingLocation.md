# AccountingLocation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**parent_id** | **str, none_type** | A unique identifier for an object. | [optional] 
**company_name** | **str, none_type** | The name of the company. | [optional] 
**display_name** | **str, none_type** | The display name of the location. | [optional] 
**status** | **str** | Based on the status some functionality is enabled or disabled. | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**subsidiaries** | [**[SubsidiaryReference]**](SubsidiaryReference.md) |  | [optional] 
**custom_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | When custom mappings are configured on the resource, the result is included here. | [optional] [readonly] 
**row_version** | **str, none_type** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

