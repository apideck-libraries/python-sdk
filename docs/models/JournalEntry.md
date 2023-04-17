# JournalEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**title** | **str, none_type** | Journal entry title | [optional] 
**currency_rate** | **float, none_type** | Currency Exchange Rate at the time entity was recorded/generated. | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**line_items** | [**[JournalEntryLineItem]**](JournalEntryLineItem.md) | Requires a minimum of 2 line items that sum to 0 | [optional] 
**memo** | **str, none_type** | Reference for the journal entry. | [optional] 
**posted_at** | **datetime** | This is the date on which the journal entry was added. This can be different from the creation date and can also be backdated. | [optional] 
**journal_symbol** | **str, none_type** | Journal symbol of the entry. For example IND for indirect costs | [optional] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime** | The date and time when the object was created. | [optional] [readonly] 
**row_version** | **str, none_type** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


