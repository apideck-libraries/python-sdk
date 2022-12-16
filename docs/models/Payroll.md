# Payroll


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**processed** | **bool** | Whether or not the payroll has been successfully processed. Note that processed payrolls cannot be updated. | 
**check_date** | **str** | The date on which employees will be paid for the payroll. | 
**start_date** | **str** | The start date, inclusive, of the pay period. | 
**end_date** | **str** | The end date, inclusive, of the pay period. | 
**company_id** | **str, none_type** |  | [optional] 
**processed_date** | **str, none_type** | The date the payroll was processed. | [optional] 
**totals** | **PayrollTotals** |  | [optional] 
**compensations** | [**[Compensation]**](Compensation.md) | An array of compensations for the payroll. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


