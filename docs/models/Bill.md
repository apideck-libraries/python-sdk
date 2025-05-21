# Bill


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**downstream_id** | **str, none_type** | The third-party API ID of original entity | [optional] [readonly] 
**bill_number** | **str, none_type** | Reference to supplier bill number | [optional] 
**supplier** | [**LinkedSupplier**](LinkedSupplier.md) |  | [optional] 
**company_id** | **str, none_type** | The company or subsidiary id the transaction belongs to | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**currency_rate** | **float, none_type** | Currency Exchange Rate at the time entity was recorded/generated. | [optional] 
**tax_inclusive** | **bool, none_type** | Amounts are including tax | [optional] 
**bill_date** | **date, none_type** | Date bill was issued - YYYY-MM-DD. | [optional] 
**due_date** | **date, none_type** | The due date is the date on which a payment is scheduled to be received - YYYY-MM-DD. | [optional] 
**paid_date** | **date, none_type** | The paid date is the date on which a payment was sent to the supplier - YYYY-MM-DD. | [optional] 
**po_number** | **str, none_type** | A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order. | [optional] 
**reference** | **str, none_type** | Optional bill reference. | [optional] 
**line_items** | [**[BillLineItem]**](BillLineItem.md) |  | [optional] 
**terms** | **str, none_type** | Terms of payment. | [optional] 
**balance** | **float, none_type** | Balance of bill due. | [optional] 
**deposit** | **float, none_type** | Amount of deposit made to this bill. | [optional] 
**sub_total** | **float, none_type** | Sub-total amount, normally before tax. | [optional] 
**total_tax** | **float, none_type** | Total tax amount applied to this bill. | [optional] 
**total** | **float, none_type** | Total amount of bill, including tax. | [optional] 
**tax_code** | **str, none_type** | Applicable tax id/code override if tax is not supplied on a line item basis. | [optional] 
**notes** | **str, none_type** |  | [optional] 
**status** | **str, none_type** | Invoice status | [optional] 
**ledger_account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**payment_method** | **str, none_type** | Payment method used for the transaction, such as cash, credit card, bank transfer, or check | [optional] 
**channel** | **str, none_type** | The channel through which the transaction is processed. | [optional] 
**language** | **str, none_type** | language code according to ISO 639-1. For the United States - EN | [optional] 
**accounting_by_row** | **bool, none_type** | Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row. | [optional] 
**bank_account** | [**BankAccount**](BankAccount.md) |  | [optional] 
**discount_percentage** | **float, none_type** | Discount percentage applied to this transaction. | [optional] 
**source_document_url** | **str, none_type** | URL link to a source document - shown as &#39;Go to [appName]&#39; in the downstream app. Currently only supported for Xero. | [optional] 
**tracking_categories** | [**LinkedTrackingCategories**](LinkedTrackingCategories.md) |  | [optional] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**row_version** | **str, none_type** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**custom_fields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**custom_mappings** | [**CustomMappings**](CustomMappings.md) |  | [optional] 
**pass_through** | [**PassThroughBody**](PassThroughBody.md) |  | [optional] 
**accounting_period** | **str, none_type** | Accounting period | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


