# ProfitAndLoss


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_name** | **str** | The name of the report | 
**currency** | [**Currency**](Currency.md) |  | 
**income** | [**Income**](Income.md) |  | 
**expenses** | [**Expenses**](Expenses.md) |  | 
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**start_date** | **str** | The start date of the report | [optional] 
**end_date** | **str** | The end date of the report | [optional] 
**cost_of_goods_sold** | [**CostOfGoodsSold**](CostOfGoodsSold.md) |  | [optional] 
**other_income** | [**OtherIncome**](OtherIncome.md) |  | [optional] 
**other_expenses** | [**OtherExpenses**](OtherExpenses.md) |  | [optional] 
**uncategorized_accounts** | [**UncategorizedAccounts**](UncategorizedAccounts.md) |  | [optional] 
**gross_profit** | [**ProfitAndLossIndicator**](ProfitAndLossIndicator.md) |  | [optional] 
**net_operating_income** | [**ProfitAndLossIndicator**](ProfitAndLossIndicator.md) |  | [optional] 
**net_income** | [**ProfitAndLossIndicator**](ProfitAndLossIndicator.md) |  | [optional] 
**custom_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | When custom mappings are configured on the resource, the result is included here. | [optional] [readonly] 
**customer** | **str** | The customer id | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


