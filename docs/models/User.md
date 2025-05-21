# User


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | [**[Email]**](Email.md) |  | 
**id** | **str** | The unique identifier for the user | [optional] [readonly] 
**parent_id** | **str, none_type** | The parent user id | [optional] 
**username** | **str, none_type** | The username of the user | [optional] 
**first_name** | **str, none_type** | The first name of the person. | [optional] 
**last_name** | **str, none_type** | The last name of the person. | [optional] 
**title** | **str, none_type** | The job title of the person. | [optional] 
**division** | **str, none_type** | The division the person is currently in. Usually a collection of departments or teams or regions. | [optional] 
**department** | **str, none_type** | The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field. | [optional] 
**company_name** | **str, none_type** | The name of the company. | [optional] 
**employee_number** | **str, none_type** | An Employee Number, Employee ID or Employee Code, is a unique number that has been assigned to each individual staff member within a company. | [optional] 
**description** | **str, none_type** | A description of the object. | [optional] 
**image** | **str, none_type** | The URL of the user&#39;s avatar | [optional] 
**language** | **str, none_type** | language code according to ISO 639-1. For the United States - EN | [optional] 
**status** | **str, none_type** | The status of the user | [optional] 
**password** | **str, none_type** | The password of the user | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**phone_numbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**custom_mappings** | [**CustomMappings**](CustomMappings.md) |  | [optional] 
**updated_at** | **str, none_type** | The date and time when the user was last updated. | [optional] [readonly] 
**created_at** | **str, none_type** | The date and time when the user was created. | [optional] [readonly] 
**pass_through** | [**PassThroughBody**](PassThroughBody.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


