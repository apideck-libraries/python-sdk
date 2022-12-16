# SharedLink


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **str** | The ID of the file or folder to link. | 
**url** | **str** | The URL that can be used to view the file. | [optional] [readonly] 
**download_url** | **str** | The URL that can be used to download the file. | [optional] 
**target** | [**SharedLinkTarget**](SharedLinkTarget.md) |  | [optional] 
**scope** | **str** | The scope of the shared link. | [optional] 
**password_protected** | **bool** | Indicated if the shared link is password protected. | [optional] [readonly] 
**password** | **str, none_type** | Optional password for the shared link. | [optional] 
**expires_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


