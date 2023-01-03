# InvoiceItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the item. | [optional] [readonly] 
**name** | **str, none_type** | Item name | [optional] 
**description** | **str, none_type** | A short description of the item | [optional] 
**code** | **str, none_type** | User defined item code | [optional] 
**sold** | **bool, none_type** | Item will be available on sales transactions | [optional] 
**purchased** | **bool, none_type** | Item is available for purchase transactions | [optional] 
**tracked** | **bool, none_type** | Item is inventoried | [optional] 
**inventory_date** | **date, none_type** | The date of opening balance if inventory item is tracked - YYYY-MM-DD. | [optional] 
**type** | **str, none_type** | Item type | [optional] 
**sales_details** | [**InvoiceItemSalesDetails**](InvoiceItemSalesDetails.md) |  | [optional] 
**purchase_details** | [**InvoiceItemSalesDetails**](InvoiceItemSalesDetails.md) |  | [optional] 
**quantity** | **float, none_type** |  | [optional] 
**unit_price** | **float, none_type** |  | [optional] 
**asset_account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**income_account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**expense_account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**active** | **bool, none_type** |  | [optional] 
**row_version** | **str, none_type** |  | [optional] 
**updated_by** | **str, none_type** |  | [optional] [readonly] 
**created_by** | **str, none_type** |  | [optional] [readonly] 
**updated_at** | **datetime, none_type** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


