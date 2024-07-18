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
**memo** | **str, none_type** | Reference for the journal entry. | [optional] 
**posted_at** | **datetime** | This is the date on which the journal entry was added. This can be different from the creation date and can also be backdated. | [optional] 
**journal_symbol** | **str, none_type** | Journal symbol of the entry. For example IND for indirect costs | [optional] 
**tax_type** | **str, none_type** | The specific category of tax associated with a transaction like sales or purchase | [optional] 
**tax_code** | **str, none_type** | Applicable tax id/code override if tax is not supplied on a line item basis. | [optional] 
**number** | **str, none_type** | Journal entry number. | [optional] 
**tracking_categories** | [**LinkedTrackingCategories**](LinkedTrackingCategories.md) |  | [optional] 
**custom_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | When custom mappings are configured on the resource, the result is included here. | [optional] [readonly] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**row_version** | **str, none_type** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**pass_through** | [**PassThroughBody**](PassThroughBody.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


