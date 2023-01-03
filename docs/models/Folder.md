# Folder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the folder | 
**parent_folders** | [**[LinkedFolder]**](LinkedFolder.md) | The parent folders of the file, starting from the root | 
**id** | **str** |  | [optional] [readonly] 
**description** | **str** | Optional description of the folder | [optional] 
**path** | **str** | The full path of the folder (includes the folder name) | [optional] [readonly] 
**size** | **int** | The size of the folder in bytes | [optional] [readonly] 
**owner** | [**Owner**](Owner.md) |  | [optional] 
**parent_folders_complete** | **bool** | Whether the list of parent folder is complete. Some connectors only return the direct parent of a folder | [optional] [readonly] 
**updated_by** | **str, none_type** |  | [optional] [readonly] 
**created_by** | **str, none_type** |  | [optional] [readonly] 
**updated_at** | **datetime, none_type** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


