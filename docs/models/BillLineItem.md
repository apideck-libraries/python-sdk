# BillLineItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**row_id** | **str** | Row ID | [optional] 
**code** | **str, none_type** | User defined item code | [optional] 
**line_number** | **int, none_type** | Line number in the invoice | [optional] 
**description** | **str, none_type** | User defined description | [optional] 
**type** | **str, none_type** | Bill Line Item type | [optional] 
**tax_amount** | **float, none_type** | Tax amount | [optional] 
**total_amount** | **float, none_type** | Total amount of the line item | [optional] 
**quantity** | **float, none_type** |  | [optional] 
**unit_price** | **float, none_type** |  | [optional] 
**unit_of_measure** | **str, none_type** | Description of the unit type the item is sold as, ie: kg, hour. | [optional] 
**discount_percentage** | **float, none_type** | Discount percentage applied to the line item when supported downstream. | [optional] 
**discount_amount** | **float, none_type** | Discount amount applied to the line item when supported downstream. | [optional] 
**location_id** | **str, none_type** | Location id | [optional] 
**department_id** | **str, none_type** | Department id | [optional] 
**item** | [**LinkedInvoiceItem**](LinkedInvoiceItem.md) |  | [optional] 
**tax_rate** | [**LinkedTaxRate**](LinkedTaxRate.md) |  | [optional] 
**ledger_account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**tracking_categories** | [**LinkedTrackingCategories**](LinkedTrackingCategories.md) |  | [optional] 
**row_version** | **str, none_type** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


