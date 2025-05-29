# JournalEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**title** | **str, none_type** | Journal entry title | [optional] 
**currency_rate** | **float, none_type** | Currency Exchange Rate at the time entity was recorded/generated. | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**company_id** | **str, none_type** | The company or subsidiary id the transaction belongs to | [optional] 
**line_items** | [**[JournalEntryLineItem]**](JournalEntryLineItem.md) | Requires a minimum of 2 line items that sum to 0 | [optional] 
**status** | **str, none_type** | Journal entry status | [optional] 
**memo** | **str, none_type** | Reference for the journal entry. | [optional] 
**posted_at** | **datetime** | This is the date on which the journal entry was added. This can be different from the creation date and can also be backdated. | [optional] 
**journal_symbol** | **str, none_type** | Journal symbol of the entry. For example IND for indirect costs | [optional] 
**tax_type** | **str, none_type** | The specific category of tax associated with a transaction like sales or purchase | [optional] 
**tax_code** | **str, none_type** | Applicable tax id/code override if tax is not supplied on a line item basis. | [optional] 
**number** | **str, none_type** | Journal entry number. | [optional] 
**tracking_categories** | [**LinkedTrackingCategories**](LinkedTrackingCategories.md) |  | [optional] 
**accounting_period** | **str, none_type** | Accounting period | [optional] 
**custom_mappings** | [**CustomMappings**](CustomMappings.md) |  | [optional] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**row_version** | **str, none_type** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**custom_fields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**pass_through** | [**PassThroughBody**](PassThroughBody.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


