# Customer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [readonly] 
**downstream_id** | **str, none_type** | The third-party API ID of original entity | [optional] [readonly] 
**display_id** | **str, none_type** | Display ID | [optional] 
**display_name** | **str, none_type** | Display name | [optional] 
**company_name** | **str, none_type** | The name of the company. | [optional] 
**title** | **str, none_type** | The job title of the person. | [optional] 
**first_name** | **str, none_type** | The first name of the person. | [optional] 
**middle_name** | **str, none_type** | Middle name of the person. | [optional] 
**last_name** | **str, none_type** | The last name of the person. | [optional] 
**suffix** | **str, none_type** |  | [optional] 
**individual** | **bool, none_type** | Is this an individual or business customer | [optional] 
**project** | **bool, none_type** | If true, indicates this is a Project. | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**phone_numbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**emails** | [**[Email]**](Email.md) |  | [optional] 
**websites** | [**[Website]**](Website.md) |  | [optional] 
**bank_accounts** | [**[BankAccount]**](BankAccount.md) |  | [optional] 
**notes** | **str, none_type** | Some notes about this customer | [optional] 
**tax_rate** | [**LinkedTaxRate**](LinkedTaxRate.md) |  | [optional] 
**tax_number** | **str, none_type** |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**parent** | [**LinkedParentCustomer**](LinkedParentCustomer.md) |  | [optional] 
**status** | **str, none_type** | Customer status | [optional] 
**payment_method** | **str, none_type** | Payment method used for the transaction, such as cash, credit card, bank transfer, or check | [optional] 
**channel** | **str, none_type** | The channel through which the transaction is processed. | [optional] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**row_version** | **str, none_type** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


