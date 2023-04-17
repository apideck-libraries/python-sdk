# PaymentCard

A card's non-confidential details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**bin** | **str, none_type** | The first six digits of the card number, known as the Bank Identification Number (BIN). | [optional] 
**card_brand** | **str, none_type** | The first six digits of the card number, known as the Bank Identification Number (BIN). | [optional] 
**card_type** | **str, none_type** |  | [optional] 
**prepaid_type** | **str, none_type** |  | [optional] 
**cardholder_name** | **str, none_type** |  | [optional] 
**customer_id** | **str, none_type** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**exp_month** | **int, none_type** | The expiration month of the associated card as an integer between 1 and 12. | [optional] 
**exp_year** | **int, none_type** | The four-digit year of the card&#39;s expiration date. | [optional] 
**fingerprint** | **str, none_type** |  | [optional] 
**last_4** | **str, none_type** |  | [optional] 
**enabled** | **bool, none_type** | Indicates whether or not a card can be used for payments. | [optional] 
**billing_address** | [**Address**](Address.md) |  | [optional] 
**reference_id** | **str, none_type** | An optional user-defined reference ID that associates this record with another entity in an external system. For example, a customer ID from an external customer management system. | [optional] 
**version** | **str, none_type** |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


