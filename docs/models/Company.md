# Company


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | **str** |  | [optional] [readonly] 
**interaction_count** | **int, none_type** |  | [optional] [readonly] 
**owner_id** | **str** |  | [optional] 
**image** | **str, none_type** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**vat_number** | **str, none_type** | VAT number | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**status** | **str, none_type** |  | [optional] 
**fax** | **str, none_type** |  | [optional] 
**annual_revenue** | **str, none_type** | Annual revenue | [optional] 
**number_of_employees** | **str, none_type** | Number of employees | [optional] 
**industry** | **str, none_type** | Industry | [optional] 
**ownership** | **str, none_type** | Ownership | [optional] 
**sales_tax_number** | **str, none_type** |  | [optional] 
**payee_number** | **str, none_type** |  | [optional] 
**abn_or_tfn** | **str, none_type** | An ABN is necessary for operating a business, while a TFN (Tax File Number) is required for any person working in Australia. | [optional] 
**abn_branch** | **str, none_type** | An ABN Branch (also known as a GST Branch) is used if part of your business needs to account for GST separately from its parent entity. | [optional] 
**acn** | **str, none_type** | The Australian Company Number (ACN) is a nine digit number with the last digit being a check digit calculated using a modified modulus 10 calculation. ASIC has adopted a convention of always printing and displaying the ACN in the format XXX XXX XXX; three blocks of three characters, each block separated by a blank. | [optional] 
**first_name** | **str, none_type** | The first name of the person. | [optional] 
**last_name** | **str, none_type** | The last name of the person. | [optional] 
**parent_id** | **str** | Parent ID | [optional] [readonly] 
**bank_accounts** | [**[BankAccount]**](BankAccount.md) |  | [optional] 
**websites** | [**[Website]**](Website.md) |  | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**social_links** | [**[SocialLink]**](SocialLink.md) |  | [optional] 
**phone_numbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**emails** | [**[Email]**](Email.md) |  | [optional] 
**row_type** | [**CompanyRowType**](CompanyRowType.md) |  | [optional] 
**custom_fields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**read_only** | **bool, none_type** |  | [optional] 
**last_activity_at** | **datetime, none_type** |  | [optional] [readonly] 
**deleted** | **bool** |  | [optional] [readonly] 
**salutation** | **str, none_type** | A formal salutation for the person. For example, &#39;Mr&#39;, &#39;Mrs&#39; | [optional] 
**birthday** | **date, none_type** | The date of birth of the person. | [optional] 
**updated_by** | **str, none_type** |  | [optional] [readonly] 
**created_by** | **str, none_type** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


