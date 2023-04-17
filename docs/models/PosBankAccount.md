# PosBankAccount

Card details for this payment. This field is currently not available. Reach out to our team for more info.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_name** | **str** | The name of the bank associated with the bank account. | [optional] 
**transfer_type** | **str** | The type of the bank transfer. The type can be &#x60;ACH&#x60; or &#x60;UNKNOWN&#x60;. | [optional] 
**account_ownership_type** | **str** | The ownership type of the bank account performing the transfer. The type can be &#x60;INDIVIDUAL&#x60;, &#x60;COMPANY&#x60;, or &#x60;UNKNOWN&#x60;. | [optional] 
**fingerprint** | **str** | Uniquely identifies the bank account for this seller and can be used to determine if payments are from the same bank account. | [optional] 
**country** | **str, none_type** | Country code according to ISO 3166-1 alpha-2. | [optional] 
**statement_description** | **str** | The statement description as sent to the bank. | [optional] 
**ach_details** | [**PosBankAccountAchDetails**](PosBankAccountAchDetails.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


