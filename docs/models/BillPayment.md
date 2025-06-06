# BillPayment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [readonly] 
**total_amount** | **float, none_type** | The total amount of the transaction or record | 
**transaction_date** | **datetime, none_type** | The date of the transaction - YYYY:MM::DDThh:mm:ss.sTZD | 
**downstream_id** | **str, none_type** | The third-party API ID of original entity | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**currency_rate** | **float, none_type** | Currency Exchange Rate at the time entity was recorded/generated. | [optional] 
**reference** | **str, none_type** | Optional transaction reference message ie: Debit remittance detail. | [optional] 
**payment_method** | **str, none_type** | Payment method used for the transaction, such as cash, credit card, bank transfer, or check | [optional] 
**payment_method_reference** | **str, none_type** | Optional reference message returned by payment method on processing | [optional] 
**payment_method_id** | **str, none_type** | A unique identifier for an object. | [optional] 
**account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**supplier** | [**LinkedSupplier**](LinkedSupplier.md) |  | [optional] 
**company_id** | **str, none_type** | The company or subsidiary id the transaction belongs to | [optional] 
**reconciled** | **bool, none_type** | Indicates if the transaction has been reconciled. | [optional] 
**status** | [**PaymentStatus**](PaymentStatus.md) |  | [optional] 
**type** | **str** | Type of payment | [optional] 
**allocations** | [**[BillPaymentAllocations]**](BillPaymentAllocations.md) |  | [optional] 
**note** | **str, none_type** | Note associated with the transaction | [optional] 
**number** | **str, none_type** | Number associated with the transaction | [optional] 
**tracking_categories** | [**LinkedTrackingCategories**](LinkedTrackingCategories.md) |  | [optional] 
**custom_fields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**row_version** | **str, none_type** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**display_id** | **str, none_type** | Id to be displayed. | [optional] 
**custom_mappings** | [**CustomMappings**](CustomMappings.md) |  | [optional] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**pass_through** | [**PassThroughBody**](PassThroughBody.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


