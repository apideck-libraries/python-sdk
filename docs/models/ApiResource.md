# ApiResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the resource, typically a lowercased version of name. | [optional] 
**name** | **str** | Name of the resource (plural) | [optional] 
**status** | [**ResourceStatus**](ResourceStatus.md) |  | [optional] 
**linked_resources** | [**[ApiResourceLinkedResources]**](ApiResourceLinkedResources.md) | List of linked resources. | [optional] 
**schema** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | JSON Schema of the resource in our Unified API | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


