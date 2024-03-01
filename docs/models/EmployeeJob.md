# EmployeeJob


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | A unique identifier for an object. | [optional] [readonly] 
**employee_id** | **str, none_type** | A unique identifier for an object. | [optional] [readonly] 
**title** | **str, none_type** | The job title of the person. | [optional] 
**role** | **str, none_type** | The position and responsibilities of the person within the organization. | [optional] 
**start_date** | **date, none_type** | The date on which the employee starts working in their current job role. | [optional] 
**end_date** | **date, none_type** | The date on which the employee leaves or is expected to leave their current job role. | [optional] 
**compensation_rate** | **float, none_type** | The rate of pay for the employee in their current job role. | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**payment_unit** | [**PaymentUnit**](PaymentUnit.md) |  | [optional] 
**hired_at** | **date, none_type** | The date on which the employee was hired by the organization | [optional] 
**is_primary** | **bool, none_type** | Indicates whether this the employee&#39;s primary job. | [optional] 
**is_manager** | **bool, none_type** | Indicates whether this the employee has a manager role. | [optional] 
**location** | [**Address**](Address.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


