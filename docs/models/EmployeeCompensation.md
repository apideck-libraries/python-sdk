# EmployeeCompensation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | A unique identifier for an object. | [optional] [readonly] 
**job_id** | **str, none_type** | The ID of the job to which the compensation belongs. | [optional] [readonly] 
**rate** | **float, none_type** | The amount paid per payment unit. | [optional] 
**payment_unit** | [**PaymentUnit**](PaymentUnit.md) |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**flsa_status** | **str, none_type** | The FLSA status for this compensation. | [optional] 
**effective_date** | **str, none_type** | The date on which a change to an employee&#39;s compensation takes effect. | [optional] 
**payment_frequency** | [**PaymentFrequency**](PaymentFrequency.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


