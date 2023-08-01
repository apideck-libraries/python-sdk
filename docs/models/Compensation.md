# Compensation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** | A unique identifier for an object. | [readonly] 
**net_pay** | **float, none_type** | The employee&#39;s net pay. Only available when payroll has been processed | [optional] 
**gross_pay** | **float, none_type** | The employee&#39;s gross pay. Only available when payroll has been processed | [optional] 
**taxes** | [**[Tax], none_type**](Tax.md) | An array of employer and employee taxes for the pay period. | [optional] 
**deductions** | [**[Deduction], none_type**](Deduction.md) | An array of employee deductions for the pay period. | [optional] 
**benefits** | [**[Benefit], none_type**](Benefit.md) | An array of employee benefits for the pay period. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


