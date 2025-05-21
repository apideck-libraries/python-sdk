# BankFeedAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [readonly] 
**bank_account_type** | **str** | Type of the bank account. | [optional] 
**source_account_id** | **str** | The source account&#39;s unique identifier. | [optional] 
**target_account_id** | **str** | The target account&#39;s unique identifier in the accounting connector. | [optional] 
**target_account_name** | **str** | Name associated with the target account. | [optional] 
**target_account_number** | **str** | Account number of the destination bank account. | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**feed_status** | **str** | Current status of the bank feed. | [optional] 
**country** | **str, none_type** | Country code according to ISO 3166-1 alpha-2. | [optional] 
**custom_fields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**custom_mappings** | [**CustomMappings**](CustomMappings.md) |  | [optional] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


