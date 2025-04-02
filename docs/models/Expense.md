# Expense


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_date** | **datetime, none_type** | The date of the transaction - YYYY:MM::DDThh:mm:ss.sTZD | 
**account_id** | **str** | The unique identifier for the ledger account that this expense should be credited to.  | 
**line_items** | [**[ExpenseLineItem]**](ExpenseLineItem.md) | Expense line items linked to this expense. | 
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**number** | **str, none_type** | Number. | [optional] 
**customer_id** | **str** | The ID of the customer this entity is linked to. Used for expenses that should be marked as billable to customers. | [optional] 
**supplier_id** | **str** | The ID of the supplier this entity is linked to. | [optional] 
**company_id** | **str, none_type** | The company or subsidiary id the transaction belongs to | [optional] 
**department_id** | **str, none_type** | The ID of the department | [optional] 
**payment_type** | **str, none_type** | The type of payment for the expense. | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**currency_rate** | **float, none_type** | Currency Exchange Rate at the time entity was recorded/generated. | [optional] 
**type** | **str, none_type** | The type of expense. | [optional] 
**memo** | **str, none_type** | The memo of the expense. | [optional] 
**tax_rate** | [**LinkedTaxRate**](LinkedTaxRate.md) |  | [optional] 
**total_amount** | **float, none_type** | The total amount of the expense line item. | [optional] 
**custom_fields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**custom_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | When custom mappings are configured on the resource, the result is included here. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**row_version** | **str, none_type** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**pass_through** | [**PassThroughBody**](PassThroughBody.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


