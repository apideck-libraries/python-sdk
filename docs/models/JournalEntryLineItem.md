# JournalEntryLineItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Debit entries are considered positive, and credit entries are considered negative. | 
**ledger_account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | 
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**description** | **str, none_type** | User defined description | [optional] 
**tax_amount** | **float, none_type** | Tax amount | [optional] 
**sub_total** | **float, none_type** | Sub-total amount, normally before tax. | [optional] 
**total_amount** | **float, none_type** | Debit entries are considered positive, and credit entries are considered negative. | [optional] 
**tax_rate** | [**LinkedTaxRate**](LinkedTaxRate.md) |  | [optional] 
**tracking_category** | [**DeprecatedLinkedTrackingCategory**](DeprecatedLinkedTrackingCategory.md) |  | [optional] 
**tracking_categories** | [**LinkedTrackingCategories**](LinkedTrackingCategories.md) |  | [optional] 
**customer** | [**LinkedCustomer**](LinkedCustomer.md) |  | [optional] 
**supplier** | [**LinkedSupplier**](LinkedSupplier.md) |  | [optional] 
**department_id** | **str, none_type** | The ID of the department | [optional] 
**location_id** | **str, none_type** | The ID of the location | [optional] 
**line_number** | **int, none_type** | Line number of the resource | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


