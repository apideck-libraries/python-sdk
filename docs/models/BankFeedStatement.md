# BankFeedStatement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [readonly] 
**bank_feed_account_id** | **str** | The ID of the bank feed account this statement belongs to. | [optional] 
**status** | **str** | The current status of the bank feed statement. | [optional] 
**start_date** | **datetime** | Start date of the bank feed statement. | [optional] 
**end_date** | **datetime** | End date of the bank feed statement. | [optional] 
**start_balance** | **float** | Balance amount at the start of the period. | [optional] 
**start_balance_credit_or_debit** | [**CreditOrDebit**](CreditOrDebit.md) |  | [optional] 
**end_balance** | **float** | Balance amount at the end of the period. | [optional] 
**end_balance_credit_or_debit** | [**CreditOrDebit**](CreditOrDebit.md) |  | [optional] 
**transactions** | [**[BankFeedStatementTransactions]**](BankFeedStatementTransactions.md) | List of transactions in the bank feed statement. | [optional] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


