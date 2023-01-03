# Payment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_amount** | **float** | Amount of payment | 
**transaction_date** | **datetime** | Date transaction was entered - YYYY:MM::DDThh:mm:ss.sTZD | 
**id** | **str** | Unique identifier representing the entity | [optional] [readonly] 
**downstream_id** | **str, none_type** | The third-party API ID of original entity | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**currency_rate** | **float, none_type** | Currency Exchange Rate at the time entity was recorded/generated. | [optional] 
**reference** | **str, none_type** | Optional payment reference message ie: Debit remittance detail. | [optional] 
**payment_method** | **str, none_type** | Payment method | [optional] 
**payment_method_reference** | **str, none_type** | Optional reference message returned by payment method on processing | [optional] 
**accounts_receivable_account_type** | **str, none_type** | Type of accounts receivable account. | [optional] 
**accounts_receivable_account_id** | **str, none_type** | Unique identifier for the account to allocate payment to. | [optional] 
**account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**customer** | [**LinkedCustomer**](LinkedCustomer.md) |  | [optional] 
**supplier** | [**LinkedSupplier**](LinkedSupplier.md) |  | [optional] 
**reconciled** | **bool** | Payment has been reconciled | [optional] 
**status** | **str** | Status of payment | [optional] 
**type** | **str** | Type of payment | [optional] 
**allocations** | [**[PaymentAllocations]**](PaymentAllocations.md) |  | [optional] 
**note** | **str, none_type** | Optional note to be associated with the payment. | [optional] 
**row_version** | **str, none_type** |  | [optional] 
**display_id** | **str, none_type** | Payment id to be displayed. | [optional] 
**updated_by** | **str, none_type** |  | [optional] [readonly] 
**created_by** | **str, none_type** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime, none_type** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


