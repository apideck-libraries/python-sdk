# Folder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the folder | 
**parent_folders** | [**[LinkedFolder]**](LinkedFolder.md) | The parent folders of the file, starting from the root | 
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**description** | **str, none_type** | Optional description of the folder | [optional] 
**path** | **str, none_type** | The full path of the folder (includes the folder name) | [optional] [readonly] 
**size** | **int, none_type** | The size of the folder in bytes | [optional] [readonly] 
**owner** | [**Owner**](Owner.md) |  | [optional] 
**parent_folders_complete** | **bool** | Whether the list of parent folder is complete. Some connectors only return the direct parent of a folder | [optional] [readonly] 
**custom_mappings** | [**CustomMappings**](CustomMappings.md) |  | [optional] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


