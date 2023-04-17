# Consumer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer_id** | **str** | Unique consumer identifier. You can freely choose a consumer ID yourself. Most of the time, this is an ID of your internal data model that represents a user or account in your system (for example account:12345). If the consumer doesn&#39;t exist yet, Vault will upsert a consumer based on your ID. | 
**application_id** | **str** | ID of your Apideck Application | [optional] [readonly] 
**metadata** | [**ConsumerMetadata**](ConsumerMetadata.md) |  | [optional] 
**connections** | [**[ConsumerConnection]**](ConsumerConnection.md) |  | [optional] [readonly] 
**services** | **[str]** |  | [optional] [readonly] 
**aggregated_request_count** | **float** |  | [optional] [readonly] 
**request_counts** | [**RequestCountAllocation**](RequestCountAllocation.md) |  | [optional] 
**created** | **str** |  | [optional] [readonly] 
**modified** | **str** |  | [optional] [readonly] 
**request_count_updated** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


