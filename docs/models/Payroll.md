# Payroll


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | A unique identifier for an object. | [readonly] 
**processed** | **bool, none_type** | Whether or not the payroll has been successfully processed. Note that processed payrolls cannot be updated. | 
**check_date** | **str, none_type** | The date on which employees will be paid for the payroll. | 
**start_date** | **str, none_type** | The start date, inclusive, of the pay period. | 
**end_date** | **str, none_type** | The end date, inclusive, of the pay period. | 
**company_id** | **str, none_type** | The unique identifier of the company. | [optional] 
**processed_date** | **str, none_type** | The date the payroll was processed. | [optional] 
**totals** | **PayrollTotals** |  | [optional] 
**compensations** | [**[Compensation]**](Compensation.md) | An array of compensations for the payroll. | [optional] 
**custom_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | When custom mappings are configured on the resource, the result is included here. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


