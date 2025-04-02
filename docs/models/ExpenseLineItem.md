# ExpenseLineItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_amount** | **float, none_type** | The total amount of the expense line item. | 
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**tracking_categories** | [**LinkedTrackingCategories**](LinkedTrackingCategories.md) |  | [optional] 
**account_id** | **str** | The unique identifier for the ledger account. | [optional] 
**customer_id** | **str** | The ID of the customer this expense item is linked to. | [optional] 
**department_id** | **str, none_type** | The ID of the department | [optional] 
**location_id** | **str, none_type** | The ID of the location | [optional] 
**subsidiary_id** | **str, none_type** | The ID of the subsidiary | [optional] 
**tax_rate** | [**LinkedTaxRate**](LinkedTaxRate.md) |  | [optional] 
**description** | **str, none_type** | The expense line item description | [optional] 
**billable** | **bool** | Boolean that indicates if the line item is billable or not. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


