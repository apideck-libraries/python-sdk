# BankFeedStatementTransactions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posted_date** | **datetime** | The date of the transaction - YYYY:MM::DDThh:mm:ss.sTZD | 
**amount** | **float** | The amount of the transaction. | 
**credit_or_debit** | [**CreditOrDebit**](CreditOrDebit.md) |  | 
**source_transaction_id** | **str** | The ID of the source transaction. | 
**description** | **str** | A description of the transaction. | [optional] 
**counterparty** | **str** | The counterparty of the transaction. | [optional] 
**reference** | **str** | The reference of the transaction. | [optional] 
**transaction_type** | **str** | Type of transaction. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


