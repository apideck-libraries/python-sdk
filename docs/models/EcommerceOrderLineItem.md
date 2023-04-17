# EcommerceOrderLineItem

A single line item of an ecommerce order, representing a product or variant with associated options, quantity, and pricing information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the product or variant associated with the line item. | 
**quantity** | **str** | The quantity of the product or variant associated with the line item. | 
**total_amount** | **str** | The total amount for the product(s) or variant associated with the line item, including taxes and discounts. | 
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**product_id** | **str** | A unique identifier for the product associated with the line item. | [optional] 
**variant_id** | **str** | A unique identifier for the variant of the product associated with the line item, if applicable. | [optional] 
**sku** | **str** | The SKU of the product or variant associated with the line item. | [optional] 
**description** | **str** | The description of the product or variant associated with the line item. | [optional] 
**options** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**unit_price** | **str** | The unit price of the product or variant associated with the line item. | [optional] 
**tax_rate** | **str** | The tax rate applied to the product or variant associated with the line item. | [optional] 
**tax_amount** | **str** | The total tax amount applied to the product or variant associated with the line item. | [optional] 
**discounts** | [**[EcommerceDiscount]**](EcommerceDiscount.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


