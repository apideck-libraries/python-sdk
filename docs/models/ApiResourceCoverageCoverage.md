# ApiResourceCoverageCoverage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**downstream_id** | **str** | ID of the resource in the Connector&#39;s API (downstream) | [optional] 
**downstream_name** | **str** | Name of the resource in the Connector&#39;s API (downstream) | [optional] 
**pagination_supported** | **bool** | Indicates if pagination (cursor and limit parameters) is supported on the list endpoint of the resource. | [optional] 
**pagination** | [**PaginationCoverage**](PaginationCoverage.md) |  | [optional] 
**supported_operations** | **[str]** | List of supported operations on the resource. | [optional] 
**supported_filters** | **[str]** | Supported filters on the list endpoint of the resource. | [optional] 
**supported_sort_by** | **[str]** | Supported sorting properties on the list endpoint of the resource. | [optional] 
**supported_fields** | [**[SupportedProperty]**](SupportedProperty.md) | Supported fields on the detail endpoint. | [optional] 
**supported_list_fields** | [**[SupportedProperty]**](SupportedProperty.md) | Supported fields on the list endpoint. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


