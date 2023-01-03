# Bill


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**downstream_id** | **str, none_type** | The third-party API ID of original entity | [optional] [readonly] 
**supplier** | [**LinkedSupplier**](LinkedSupplier.md) |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**currency_rate** | **float, none_type** | Currency Exchange Rate at the time entity was recorded/generated. | [optional] 
**tax_inclusive** | **bool, none_type** | Amounts are including tax | [optional] 
**bill_date** | **date** | Date bill was issued - YYYY-MM-DD. | [optional] 
**due_date** | **date** | The due date is the date on which a payment is scheduled to be received by the supplier - YYYY-MM-DD. | [optional] 
**paid_date** | **date, none_type** | The paid date is the date on which a payment was sent to the supplier - YYYY-MM-DD. | [optional] 
**po_number** | **str, none_type** | A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order. | [optional] 
**reference** | **str, none_type** | Optional invoice reference. | [optional] 
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
**bill_number** | **str, none_type** |  | [optional] 
**updated_by** | **str, none_type** |  | [optional] [readonly] 
**created_by** | **str, none_type** |  | [optional] [readonly] 
**updated_at** | **datetime, none_type** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**row_version** | **str, none_type** |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


