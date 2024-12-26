# BalanceByPeriod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date, none_type** | The starting date of the period. If not provided, it represents the oldest period, where all transactions due before the specified &#x60;end_date&#x60; are included. | [optional] 
**end_date** | **date, none_type** | The ending date of the period. If not provided, it represents an open-ended period starting from the &#x60;start_date&#x60;, typically capturing future-dated transactions that are not yet aged. | [optional] 
**total_amount** | **float** | Total amount of the period. | [optional] 
**balances_by_transaction** | [**[BalanceByTransaction]**](BalanceByTransaction.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


