# TaxRate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | ID assigned to identify this tax rate. | [optional] 
**name** | **str** | Name assigned to identify this tax rate. | [optional] 
**code** | **str, none_type** | Tax code assigned to identify this tax rate. | [optional] 
**description** | **str, none_type** | Description of tax rate | [optional] 
**effective_tax_rate** | **float, none_type** | Effective tax rate | [optional] 
**total_tax_rate** | **float, none_type** | Not compounded sum of the components of a tax rate | [optional] 
**tax_payable_account_id** | **str, none_type** | Unique identifier for the account for tax collected. | [optional] 
**tax_remitted_account_id** | **str, none_type** | Unique identifier for the account for tax remitted. | [optional] 
**components** | **[bool, date, datetime, dict, float, int, list, str, none_type], none_type** |  | [optional] 
**type** | **str, none_type** | Tax type used to indicate the source of tax collected or paid | [optional] 
**report_tax_type** | **str, none_type** | Report Tax type to aggregate tax collected or paid for reporting purposes | [optional] 
**original_tax_rate_id** | **str, none_type** | ID of the original tax rate from which the new tax rate is derived. Helps to understand the relationship between corresponding tax rate entities. | [optional] 
**status** | **str, none_type** | Tax rate status | [optional] 
**row_version** | **str, none_type** |  | [optional] 
**updated_by** | **str, none_type** |  | [optional] [readonly] 
**created_by** | **str, none_type** |  | [optional] [readonly] 
**updated_at** | **datetime, none_type** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


