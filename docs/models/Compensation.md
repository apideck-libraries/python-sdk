# Compensation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** |  | [readonly] 
**net_pay** | **float** | The employee&#39;s net pay. Only available when payroll has been processed | [optional] 
**gross_pay** | **float** | The employee&#39;s gross pay. Only available when payroll has been processed | [optional] 
**taxes** | [**[Tax]**](Tax.md) | An array of employer and employee taxes for the pay period. | [optional] 
**deductions** | [**[Deduction]**](Deduction.md) | An array of employee deductions for the pay period. | [optional] 
**benefits** | [**[Benefit]**](Benefit.md) | An array of employee benefits for the pay period. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


