# PosBankAccountAchDetails

ACH-specific details about `BANK_ACCOUNT` type payments with the `transfer_type` of `ACH`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routing_number** | **str** | The routing number for the bank account. | [optional] 
**account_number_suffix** | **str** | The last few digits of the bank account number. | [optional] 
**account_type** | **str** | The type of the bank account performing the transfer. The account type can be &#x60;CHECKING&#x60;, &#x60;SAVINGS&#x60;, or &#x60;UNKNOWN&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


