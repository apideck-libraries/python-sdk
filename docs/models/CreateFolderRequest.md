# CreateFolderRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the folder. | 
**parent_folder_id** | **str** | The parent folder to create the new file within. This can be an ID or a path depending on the downstream folder. Please see the connector section below to see downstream specific gotchas. | 
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**description** | **str** | Optional description of the folder. | [optional] 
**drive_id** | **str** | ID of the drive to create the folder in. | [optional] 
**pass_through** | [**PassThroughBody**](PassThroughBody.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


