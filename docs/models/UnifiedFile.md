# UnifiedFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [readonly] 
**name** | **str, none_type** | The name of the file | 
**type** | [**FileType**](FileType.md) |  | 
**downstream_id** | **str, none_type** | The third-party API ID of original entity | [optional] [readonly] 
**description** | **str, none_type** | Optional description of the file | [optional] 
**path** | **str, none_type** | The full path of the file or folder (includes the file name) | [optional] 
**mime_type** | **str, none_type** | The MIME type of the file. | [optional] 
**downloadable** | **bool** | Whether the current user can download this file | [optional] 
**size** | **int, none_type** | The size of the file in bytes | [optional] 
**owner** | [**Owner**](Owner.md) |  | [optional] 
**parent_folders** | [**[LinkedFolder]**](LinkedFolder.md) | The parent folders of the file, starting from the root | [optional] 
**parent_folders_complete** | **bool** | Whether the list of parent folders is complete. Some connectors only return the direct parent of a file | [optional] 
**permissions** | [**UnifiedFilePermissions**](UnifiedFilePermissions.md) |  | [optional] 
**exportable** | **bool** | Whether the current file is exportable to other file formats. This property is relevant for proprietary file formats such as Google Docs or Dropbox Paper. | [optional] 
**export_formats** | **[str], none_type** | The available file formats when exporting this file. | [optional] 
**custom_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | When custom mappings are configured on the resource, the result is included here. | [optional] [readonly] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


