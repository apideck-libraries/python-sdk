# CompanyInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**company_name** | **str, none_type** | The name of the company. | [optional] 
**status** | **str** | Based on the status some functionality is enabled or disabled. | [optional] 
**legal_name** | **str** | The legal name of the company | [optional] 
**country** | **str, none_type** | country code according to ISO 3166-1 alpha-2. | [optional] 
**sales_tax_number** | **str, none_type** |  | [optional] 
**automated_sales_tax** | **bool** | Whether sales tax is calculated automatically for the company | [optional] 
**sales_tax_enabled** | **bool** | Whether sales tax is enabled for the company | [optional] 
**default_sales_tax** | [**LinkedTaxRate**](LinkedTaxRate.md) |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**language** | **str, none_type** | language code according to ISO 639-1. For the United States - EN | [optional] 
**fiscal_year_start_month** | **str** | The start month of fiscal year. | [optional] 
**company_start_date** | **date** | Date when company file was created | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**phone_numbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**emails** | [**[Email]**](Email.md) |  | [optional] 
**row_version** | **str, none_type** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


