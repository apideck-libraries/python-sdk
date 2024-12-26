# AgedDebtors


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_generated_at** | **datetime** | The exact date and time the report was generated. | [optional] 
**report_as_of_date** | **date** | The cutoff date for transactions included in the report. | [optional] 
**period_count** | **int** | Number of aging periods shown in the report. | [optional]  if omitted the server will use the default value of 4
**period_length** | **int** | Length of each aging period in days. | [optional]  if omitted the server will use the default value of 30
**outstanding_balances** | [**[OutstandingBalanceByCustomer]**](OutstandingBalanceByCustomer.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


