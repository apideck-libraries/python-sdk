# BalanceSheetReports


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **str** | The start date of the report | 
**assets** | [**BalanceSheetAssetsAccount**](BalanceSheetAssetsAccount.md) |  | 
**liabilities** | [**BalanceSheetLiabilitiesAccount**](BalanceSheetLiabilitiesAccount.md) |  | 
**equity** | [**BalanceSheetEquityAccount**](BalanceSheetEquityAccount.md) |  | 
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**report_name** | **str** | The name of the report | [optional] 
**start_date** | **str** | The start date of the report | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**net_assets** | **float** | The net assets of the balance sheet | [optional] 
**custom_mappings** | [**CustomMappings**](CustomMappings.md) |  | [optional] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**uncategorized_items** | [**BalanceSheetUncategorizedItemsAccount**](BalanceSheetUncategorizedItemsAccount.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


