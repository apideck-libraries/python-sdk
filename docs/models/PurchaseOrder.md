# PurchaseOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**downstream_id** | **str, none_type** | The third-party API ID of original entity | [optional] [readonly] 
**po_number** | **str, none_type** | A PO Number uniquely identifies a purchase order and is generally defined by the buyer. | [optional] 
**reference** | **str, none_type** | Optional purchase order reference. | [optional] 
**supplier** | [**LinkedSupplier**](LinkedSupplier.md) |  | [optional] 
**status** | **str, none_type** |  | [optional] 
**issued_date** | **date, none_type** | Date purchase order was issued - YYYY-MM-DD. | [optional] 
**delivery_date** | **date, none_type** | The date on which the purchase order is to be delivered - YYYY-MM-DD. | [optional] 
**expected_arrival_date** | **date, none_type** | The date on which the order is expected to arrive - YYYY-MM-DD. | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**currency_rate** | **float, none_type** | Currency Exchange Rate at the time entity was recorded/generated. | [optional] 
**sub_total** | **float, none_type** | Sub-total amount, normally before tax. | [optional] 
**total_tax** | **float, none_type** | Total tax amount applied to this invoice. | [optional] 
**total** | **float, none_type** | Total amount of invoice, including tax. | [optional] 
**tax_inclusive** | **bool, none_type** | Amounts are including tax | [optional] 
**line_items** | [**[InvoiceLineItem]**](InvoiceLineItem.md) |  | [optional] 
**shipping_address** | [**Address**](Address.md) |  | [optional] 
**ledger_account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**template_id** | **str, none_type** | Optional purchase order template | [optional] 
**discount_percentage** | **float, none_type** | Discount percentage applied to this transaction. | [optional] 
**bank_account** | [**BankAccount**](BankAccount.md) |  | [optional] 
**accounting_by_row** | **bool, none_type** | Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row. | [optional] 
**due_date** | **date** | The due date is the date on which a payment is scheduled to be received - YYYY-MM-DD. | [optional] 
**payment_method** | **str, none_type** | Payment method used for the transaction, such as cash, credit card, bank transfer, or check | [optional] 
**tax_code** | **str, none_type** | Applicable tax id/code override if tax is not supplied on a line item basis. | [optional] 
**channel** | **str, none_type** | The channel through which the transaction is processed. | [optional] 
**row_version** | **str, none_type** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


