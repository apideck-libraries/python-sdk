# UploadSession


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**success** | **bool** | Indicates if the upload session was completed successfully. | [optional] [readonly] 
**part_size** | **float** | Size in bytes of each part of the file that you will upload. Uploaded parts need to be this size for the upload to be successful. | [optional] [readonly] 
**parallel_upload_supported** | **bool** | Indicates if parts of the file can uploaded in parallel. | [optional] [readonly] 
**uploaded_byte_range** | **str** | The range of bytes that was successfully uploaded. | [optional] [readonly] 
**expires_at** | **datetime** |  | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


