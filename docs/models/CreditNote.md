# CreditNote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier representing the entity | [readonly] 
**total_amount** | **float** | Amount of transaction | 
**number** | **str, none_type** | Credit note number. | [optional] 
**customer** | [**LinkedCustomer**](LinkedCustomer.md) |  | [optional] 
**company_id** | **str, none_type** | The company or subsidiary id the transaction belongs to | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**currency_rate** | **float, none_type** | Currency Exchange Rate at the time entity was recorded/generated. | [optional] 
**tax_inclusive** | **bool, none_type** | Amounts are including tax | [optional] 
**sub_total** | **float, none_type** | Sub-total amount, normally before tax. | [optional] 
**total_tax** | **float, none_type** | Total tax amount applied to this invoice. | [optional] 
**tax_code** | **str, none_type** | Applicable tax id/code override if tax is not supplied on a line item basis. | [optional] 
**balance** | **float, none_type** | The balance reflecting any payments made against the transaction. | [optional] 
**remaining_credit** | **float, none_type** | Indicates the total credit amount still available to apply towards the payment. | [optional] 
**status** | **str** | Status of credit notes | [optional] 
**reference** | **str, none_type** | Optional reference message ie: Debit remittance detail. | [optional] 
**date_issued** | **datetime** | Date credit note issued - YYYY:MM::DDThh:mm:ss.sTZD | [optional] 
**date_paid** | **datetime, none_type** | Date credit note paid - YYYY:MM::DDThh:mm:ss.sTZD | [optional] 
**type** | **str** | Type of payment | [optional] 
**account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**line_items** | [**[InvoiceLineItem]**](InvoiceLineItem.md) |  | [optional] 
**allocations** | [**[Allocation]**](Allocation.md) |  | [optional] 
**note** | **str, none_type** | Optional note to be associated with the credit note. | [optional] 
**terms** | **str, none_type** | Optional terms to be associated with the credit note. | [optional] 
**billing_address** | [**Address**](Address.md) |  | [optional] 
**shipping_address** | [**Address**](Address.md) |  | [optional] 
**tracking_categories** | [**LinkedTrackingCategories**](LinkedTrackingCategories.md) |  | [optional] 
**custom_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | When custom mappings are configured on the resource, the result is included here. | [optional] [readonly] 
**custom_fields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**row_version** | **str, none_type** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**pass_through** | [**PassThroughBody**](PassThroughBody.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


