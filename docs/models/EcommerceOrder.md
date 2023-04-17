# EcommerceOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [readonly] 
**order_number** | **str** | Order number, if any. | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**discounts** | [**[EcommerceDiscount]**](EcommerceDiscount.md) |  | [optional] 
**sub_total** | **str** | Sub-total amount, normally before tax. | [optional] 
**shipping_cost** | **str** | Shipping cost, if any. | [optional] 
**total_discount** | **str** | Total discount, if any. | [optional] 
**total_tax** | **str** | Total tax, if any. | [optional] 
**total_amount** | **str** | Total amount due. | [optional] 
**status** | [**EcommerceOrderStatus**](EcommerceOrderStatus.md) |  | [optional] 
**payment_status** | **str** | Current payment status of the order. | [optional] 
**fulfillment_status** | **str** | Current fulfillment status of the order. | [optional] 
**payment_method** | **str** | Payment method used for this order. | [optional] 
**customer** | [**LinkedEcommerceCustomer**](LinkedEcommerceCustomer.md) |  | [optional] 
**billing_address** | [**EcommerceAddress**](EcommerceAddress.md) |  | [optional] 
**shipping_address** | [**EcommerceAddress**](EcommerceAddress.md) |  | [optional] 
**tracking** | [**[TrackingItem]**](TrackingItem.md) |  | [optional] 
**line_items** | [**[EcommerceOrderLineItem]**](EcommerceOrderLineItem.md) |  | [optional] 
**note** | **str** | Note for the order. | [optional] 
**created_at** | **datetime** | The date and time when the object was created. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


