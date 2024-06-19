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
**custom_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | When custom mappings are configured on the resource, the result is included here. | [optional] [readonly] 
**row_version** | **str, none_type** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**pass_through** | [**PassThroughBody**](PassThroughBody.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


