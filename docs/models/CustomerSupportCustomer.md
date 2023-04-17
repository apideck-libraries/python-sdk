# CustomerSupportCustomer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**company_name** | **str, none_type** | The name of the company. | [optional] 
**first_name** | **str, none_type** | The first name of the person. | [optional] 
**last_name** | **str, none_type** | The last name of the person. | [optional] 
**individual** | **bool, none_type** |  | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**notes** | **str, none_type** |  | [optional] 
**phone_numbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**emails** | [**[Email]**](Email.md) |  | [optional] 
**tax_number** | **str, none_type** |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**bank_accounts** | [**BankAccount**](BankAccount.md) |  | [optional] 
**status** | **str, none_type** | Customer status | [optional] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime** | The date and time when the object was created. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


