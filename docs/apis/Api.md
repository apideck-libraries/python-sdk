# Api


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the API. | [optional] [readonly] 
**type** | **str** | Indicates whether the API is a Unified API. If unified_api is false, the API is a Platform API. | [optional] 
**name** | **str** | Name of the API. | [optional] 
**description** | **str, none_type** | Description of the API. | [optional] 
**status** | [**ApiStatus**](ApiStatus.md) |  | [optional] 
**spec_url** | **str** | Link to the latest OpenAPI specification of the API. | [optional] 
**api_reference_url** | **str** | Link to the API reference of the API. | [optional] 
**postman_collection_id** | **str, none_type** | ID of the Postman collection of the API. | [optional] 
**categories** | **[str]** | List of categories the API belongs to. | [optional] 
**resources** | [**[ApiResources]**](ApiResources.md) | List of resources supported in this API. | [optional] 
**events** | **[str]** | List of event types this API supports. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


