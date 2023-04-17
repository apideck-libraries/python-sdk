# EcommerceProduct


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [readonly] 
**name** | **str** | The name of the product as it should be displayed to customers. | [optional] 
**description** | **str** | A detailed description of the product. | [optional] 
**status** | **str** | The current status of the product (active or archived). | [optional] 
**price** | **str** | The price of the product. | [optional] 
**sku** | **str** | The stock keeping unit of the product. | [optional] 
**inventory_quantity** | **str** | The quantity of the product in stock. | [optional] 
**images** | [**[EcommerceProductImages]**](EcommerceProductImages.md) | An array of image URLs for the product. | [optional] 
**weight** | **str** | The weight of the product. | [optional] 
**weight_unit** | **str** | The unit of measurement for the weight of the product. | [optional] 
**options** | [**[EcommerceProductOptions]**](EcommerceProductOptions.md) | An array of options for the product. | [optional] 
**variants** | [**[EcommerceProductVariants]**](EcommerceProductVariants.md) |  | [optional] 
**tags** | **[str]** | An array of tags for the product, used for organization and searching. | [optional] 
**categories** | [**[EcommerceProductCategories]**](EcommerceProductCategories.md) | An array of categories for the product, used for organization and searching. | [optional] 
**created_at** | **datetime** | The date and time when the object was created. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


