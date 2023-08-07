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
**taxable** | **bool, none_type** | If true, transactions for this item are taxable | [optional] 
**inventory_date** | **date, none_type** | The date of opening balance if inventory item is tracked - YYYY-MM-DD. | [optional] 
**type** | **str, none_type** | Item type | [optional] 
**sales_details** | [**InvoiceItemSalesDetails**](InvoiceItemSalesDetails.md) |  | [optional] 
**purchase_details** | [**InvoiceItemSalesDetails**](InvoiceItemSalesDetails.md) |  | [optional] 
**quantity** | **float, none_type** |  | [optional] 
**unit_price** | **float, none_type** |  | [optional] 
**asset_account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**income_account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**expense_account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**tracking_category** | [**LinkedTrackingCategory**](LinkedTrackingCategory.md) |  | [optional] 
**active** | **bool, none_type** |  | [optional] 
**row_version** | **str, none_type** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime** | The date and time when the object was created. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


