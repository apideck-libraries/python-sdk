# UnifiedFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**name** | **str** | The name of the file | 
**type** | [**FileType**](FileType.md) |  | 
**downstream_id** | **str, none_type** | The third-party API ID of original entity | [optional] [readonly] 
**description** | **str** | Optional description of the file | [optional] 
**path** | **str** | The full path of the file or folder (includes the file name) | [optional] 
**mime_type** | **str** | The MIME type of the file. | [optional] 
**downloadable** | **bool** | Whether the current user can download this file | [optional] 
**size** | **int** | The size of the file in bytes | [optional] 
**owner** | [**Owner**](Owner.md) |  | [optional] 
**parent_folders** | [**[LinkedFolder]**](LinkedFolder.md) | The parent folders of the file, starting from the root | [optional] 
**parent_folders_complete** | **bool** | Whether the list of parent folder is complete. Some connectors only return the direct parent of a file | [optional] 
**updated_by** | **str, none_type** |  | [optional] [readonly] 
**created_by** | **str, none_type** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


