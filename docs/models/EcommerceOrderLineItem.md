# EcommerceOrderLineItem

A single line item of an ecommerce order, representing a product or variant with associated options, quantity, and pricing information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | The name of the product or variant associated with the line item. | 
**quantity** | **str, none_type** | The quantity of the product or variant associated with the line item. | 
**id** | **str, none_type** | A unique identifier for an object. | [optional] [readonly] 
**product_id** | **str, none_type** | A unique identifier for the product associated with the line item. | [optional] 
**variant_id** | **str, none_type** | A unique identifier for the variant of the product associated with the line item, if applicable. | [optional] 
**sku** | **str, none_type** | The SKU of the product or variant associated with the line item. | [optional] 
**description** | **str, none_type** | The description of the product or variant associated with the line item. | [optional] 
**options** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**unit_price** | **str, none_type** | The unit price of the product or variant associated with the line item. | [optional] 
**tax_rate** | **str, none_type** | The tax rate applied to the product or variant associated with the line item. | [optional] 
**tax_amount** | **str, none_type** | The total tax amount applied to the product or variant associated with the line item. | [optional] 
**is_refunded** | **bool, none_type** | Whether the line item has been refunded. | [optional] 
**refunded_amount** | **str, none_type** | The amount of the line item that has been refunded. | [optional] 
**refunded_quantity** | **str, none_type** | The quantity of the line item that has been refunded. | [optional] 
**sub_total** | **str, none_type** | The sub total for the product(s) or variant associated with the line item, excluding taxes and discounts. | [optional] 
**total_amount** | **str, none_type** | The total amount for the product(s) or variant associated with the line item, including taxes and discounts. | [optional] 
**discounts** | [**[EcommerceDiscount]**](EcommerceDiscount.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


