# CreditNote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_amount** | **float** | Amount of transaction | 
**id** | **str** | Unique identifier representing the entity | [optional] [readonly] 
**number** | **str, none_type** | Credit note number. | [optional] 
**customer** | [**LinkedCustomer**](LinkedCustomer.md) |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**currency_rate** | **float, none_type** | Currency Exchange Rate at the time entity was recorded/generated. | [optional] 
**tax_inclusive** | **bool, none_type** | Amounts are including tax | [optional] 
**sub_total** | **float, none_type** | Sub-total amount, normally before tax. | [optional] 
**total_tax** | **float, none_type** | Total tax amount applied to this invoice. | [optional] 
**tax_code** | **str, none_type** | Applicable tax id/code override if tax is not supplied on a line item basis. | [optional] 
**balance** | **float, none_type** | The balance reflecting any payments made against the transaction. | [optional] 
**remaining_credit** | **float, none_type** | Indicates the total credit amount still available to apply towards the payment. | [optional] 
**status** | **str** | Status of payment | [optional] 
**reference** | **str, none_type** | Optional reference message ie: Debit remittance detail. | [optional] 
**date_issued** | **datetime** | Date credit note issued - YYYY:MM::DDThh:mm:ss.sTZD | [optional] 
**date_paid** | **datetime, none_type** | Date credit note paid - YYYY:MM::DDThh:mm:ss.sTZD | [optional] 
**type** | **str** | Type of payment | [optional] 
**account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**line_items** | [**[InvoiceLineItem]**](InvoiceLineItem.md) |  | [optional] 
**allocations** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**note** | **str, none_type** | Optional note to be associated with the credit note. | [optional] 
**row_version** | **str, none_type** |  | [optional] 
**updated_by** | **str, none_type** |  | [optional] [readonly] 
**created_by** | **str, none_type** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


