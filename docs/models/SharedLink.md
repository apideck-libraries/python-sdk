# SharedLink


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **str, none_type** | The ID of the file or folder to link. | 
**url** | **str, none_type** | The URL that can be used to view the file. | [optional] [readonly] 
**download_url** | **str, none_type** | The URL that can be used to download the file. | [optional] 
**target** | [**SharedLinkTarget**](SharedLinkTarget.md) |  | [optional] 
**scope** | **str, none_type** | The scope of the shared link. | [optional] 
**password_protected** | **bool, none_type** | Indicated if the shared link is password protected. | [optional] [readonly] 
**password** | **str, none_type** | Optional password for the shared link. | [optional] 
**expires_at** | **datetime, none_type** |  | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**pass_through** | [**PassThroughBody**](PassThroughBody.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


