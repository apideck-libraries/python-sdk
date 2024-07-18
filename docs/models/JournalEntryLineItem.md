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
**department_id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**location_id** | **str** | A unique identifier for an object. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


