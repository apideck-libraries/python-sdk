# Payment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier representing the entity | [readonly] 
**total_amount** | **float** | Amount of payment | 
**transaction_date** | **datetime** | Date transaction was entered - YYYY:MM::DDThh:mm:ss.sTZD | 
**downstream_id** | **str, none_type** | The third-party API ID of original entity | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**currency_rate** | **float, none_type** | Currency Exchange Rate at the time entity was recorded/generated. | [optional] 
**reference** | **str, none_type** | Optional payment reference message ie: Debit remittance detail. | [optional] 
**payment_method** | **str, none_type** | Payment method name | [optional] 
**payment_method_reference** | **str, none_type** | Optional reference message returned by payment method on processing | [optional] 
**payment_method_id** | **str, none_type** | Unique identifier for the payment method. | [optional] 
**accounts_receivable_account_type** | **str, none_type** | Type of accounts receivable account. | [optional] 
**accounts_receivable_account_id** | **str, none_type** | Unique identifier for the account to allocate payment to. | [optional] 
**account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**customer** | [**LinkedCustomer**](LinkedCustomer.md) |  | [optional] 
**supplier** | [**LinkedSupplier**](LinkedSupplier.md) |  | [optional] 
**company_id** | **str, none_type** | The company or subsidiary id the transaction belongs to | [optional] 
**reconciled** | **bool** | Payment has been reconciled | [optional] 
**status** | **str** | Status of payment | [optional] 
**type** | **str** | Type of payment | [optional] 
**allocations** | [**[Allocation]**](Allocation.md) |  | [optional] 
**note** | **str, none_type** | Optional note to be associated with the payment. | [optional] 
**number** | **str, none_type** | Payment number. | [optional] 
**tracking_categories** | [**LinkedTrackingCategories**](LinkedTrackingCategories.md) |  | [optional] 
**custom_fields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**row_version** | **str, none_type** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**display_id** | **str, none_type** | Payment id to be displayed. | [optional] 
**custom_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | When custom mappings are configured on the resource, the result is included here. | [optional] [readonly] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**pass_through** | [**PassThroughBody**](PassThroughBody.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


