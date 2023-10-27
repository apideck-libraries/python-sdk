# EcommerceProduct


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [readonly] 
**name** | **str, none_type** | The name of the product as it should be displayed to customers. | [optional] 
**description** | **str, none_type** | A detailed description of the product. | [optional] 
**status** | **str, none_type** | The current status of the product (active or archived). | [optional] 
**price** | **str, none_type** | The price of the product. | [optional] 
**sku** | **str, none_type** | The stock keeping unit of the product. | [optional] 
**inventory_quantity** | **str, none_type** | The quantity of the product in stock. | [optional] 
**images** | [**[EcommerceProductImages], none_type**](EcommerceProductImages.md) | An array of image URLs for the product. | [optional] 
**weight** | **str, none_type** | The weight of the product. | [optional] 
**weight_unit** | **str, none_type** | The unit of measurement for the weight of the product. | [optional] 
**options** | [**[EcommerceProductOptions]**](EcommerceProductOptions.md) | An array of options for the product. | [optional] 
**variants** | [**[EcommerceProductVariants]**](EcommerceProductVariants.md) |  | [optional] 
**tags** | **[str, none_type]** | An array of tags for the product, used for organization and searching. | [optional] 
**categories** | [**[EcommerceProductCategories]**](EcommerceProductCategories.md) | An array of categories for the product, used for organization and searching. | [optional] 
**custom_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | When custom mappings are configured on the resource, the result is included here. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


