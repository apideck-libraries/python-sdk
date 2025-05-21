# EcommerceOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [readonly] 
**order_number** | **str, none_type** | Order number, if any. | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**discounts** | [**[EcommerceDiscount]**](EcommerceDiscount.md) |  | [optional] 
**sub_total** | **str, none_type** | Sub-total amount, normally before tax. | [optional] 
**shipping_cost** | **str, none_type** | Shipping cost, if any. | [optional] 
**coupon_discount** | **str, none_type** | Coupon discount, if any. | [optional] 
**total_discount** | **str, none_type** | Total discount, if any. | [optional] 
**total_tax** | **str, none_type** | Total tax, if any. | [optional] 
**total_amount** | **str, none_type** | Total amount due. | [optional] 
**refunded_amount** | **str, none_type** | Refunded amount, if any. | [optional] 
**status** | [**EcommerceOrderStatus**](EcommerceOrderStatus.md) |  | [optional] 
**payment_status** | **str, none_type** | Current payment status of the order. | [optional] 
**fulfillment_status** | **str, none_type** | Current fulfillment status of the order. | [optional] 
**payment_method** | **str, none_type** | Payment method used for this order. | [optional] 
**customer** | [**LinkedEcommerceCustomer**](LinkedEcommerceCustomer.md) |  | [optional] 
**billing_address** | [**EcommerceAddress**](EcommerceAddress.md) |  | [optional] 
**shipping_address** | [**EcommerceAddress**](EcommerceAddress.md) |  | [optional] 
**tracking** | [**[TrackingItem]**](TrackingItem.md) |  | [optional] 
**line_items** | [**[EcommerceOrderLineItem]**](EcommerceOrderLineItem.md) |  | [optional] 
**note** | **str, none_type** | Note for the order. | [optional] 
**custom_mappings** | [**CustomMappings**](CustomMappings.md) |  | [optional] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


