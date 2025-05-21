# Company


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Name of the company | 
**id** | **str** | Unique identifier for the company | [optional] [readonly] 
**interaction_count** | **int, none_type** | Number of interactions | [optional] [readonly] 
**owner_id** | **str, none_type** | Owner ID | [optional] 
**image** | **str, none_type** | The Image URL of the company | [optional] 
**description** | **str, none_type** | A description of the company | [optional] 
**vat_number** | **str, none_type** | The VAT number of the company | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**status** | **str, none_type** | The status of the company | [optional] 
**fax** | **str, none_type** | The fax number of the company | [optional] 
**annual_revenue** | **str, none_type** | The annual revenue of the company | [optional] 
**number_of_employees** | **str, none_type** | Number of employees | [optional] 
**industry** | **str, none_type** | The industry represents the type of business the company is in. | [optional] 
**ownership** | **str, none_type** | The ownership indicates the type of ownership of the company. | [optional] 
**sales_tax_number** | **str, none_type** | A sales tax number is a unique number that identifies a company for tax purposes. | [optional] 
**payee_number** | **str, none_type** | A payee number is a unique number that identifies a payee for tax purposes. | [optional] 
**abn_or_tfn** | **str, none_type** | An ABN is necessary for operating a business, while a TFN (Tax File Number) is required for any person working in Australia. | [optional] 
**abn_branch** | **str, none_type** | An ABN Branch (also known as a GST Branch) is used if part of your business needs to account for GST separately from its parent entity. | [optional] 
**acn** | **str, none_type** | The Australian Company Number (ACN) is a nine digit number with the last digit being a check digit calculated using a modified modulus 10 calculation. ASIC has adopted a convention of always printing and displaying the ACN in the format XXX XXX XXX; three blocks of three characters, each block separated by a blank. | [optional] 
**first_name** | **str, none_type** | The first name of the person. | [optional] 
**last_name** | **str, none_type** | The last name of the person. | [optional] 
**parent_id** | **str, none_type** | Parent ID | [optional] [readonly] 
**bank_accounts** | [**[BankAccount]**](BankAccount.md) |  | [optional] 
**websites** | [**[Website]**](Website.md) |  | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**social_links** | [**[SocialLink]**](SocialLink.md) |  | [optional] 
**phone_numbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**emails** | [**[Email]**](Email.md) |  | [optional] 
**row_type** | [**CompanyRowType**](CompanyRowType.md) |  | [optional] 
**custom_fields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**read_only** | **bool, none_type** | Whether the company is read-only or not | [optional] 
**last_activity_at** | **datetime, none_type** | Last activity date | [optional] [readonly] 
**deleted** | **bool** | Whether the company is deleted or not | [optional] [readonly] 
**salutation** | **str, none_type** | A formal salutation for the person. For example, &#39;Mr&#39;, &#39;Mrs&#39; | [optional] 
**birthday** | **date, none_type** | The date of birth of the person. | [optional] 
**custom_mappings** | [**CustomMappings**](CustomMappings.md) |  | [optional] 
**updated_by** | **str, none_type** | Updated by user ID | [optional] [readonly] 
**created_by** | **str, none_type** | Created by user ID | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Last updated date | [optional] [readonly] 
**created_at** | **datetime, none_type** | Creation date | [optional] [readonly] 
**pass_through** | [**PassThroughBody**](PassThroughBody.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


