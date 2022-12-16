# OrderTenders


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**percentage** | **float** |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**total_amount** | **int, none_type** |  | [optional] 
**total_tip** | **int, none_type** |  | [optional] 
**total_processing_fee** | **int, none_type** |  | [optional] 
**total_tax** | **int, none_type** |  | [optional] 
**total_discount** | **int, none_type** |  | [optional] 
**total_refund** | **int, none_type** |  | [optional] 
**total_service_charge** | **int, none_type** |  | [optional] 
**buyer_tendered_cash_amount** | **int, none_type** | The amount (in cents) of cash tendered by the buyer. Only applicable when the tender type is cash. | [optional] 
**change_back_cash_amount** | **int, none_type** | The amount (in cents) of cash returned to the buyer. Only applicable when the tender type is cash. | [optional] 
**card** | [**PaymentCard**](PaymentCard.md) |  | [optional] 
**card_status** | **str, none_type** | The status of the card. Only applicable when the tender type is card. | [optional] 
**card_entry_method** | **str, none_type** | The entry method of the card. Only applicable when the tender type is card. | [optional] 
**payment_id** | **str** |  | [optional] [readonly] 
**location_id** | **str** |  | [optional] [readonly] 
**transaction_id** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


