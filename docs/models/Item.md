# Item


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | **str** |  | [optional] 
**idempotency_key** | [**IdempotencyKey**](IdempotencyKey.md) |  | [optional] 
**description** | **str** |  | [optional] 
**abbreviation** | **str** |  | [optional] 
**product_type** | **str** |  | [optional] 
**price_amount** | **float** |  | [optional] 
**pricing_type** | **str** |  | [optional] 
**price_currency** | [**Currency**](Currency.md) |  | [optional] 
**cost** | **float** |  | [optional] 
**tax_ids** | **[str]** | A list of Tax IDs for the product. | [optional] 
**absent_at_location_ids** | **[str]** | A list of locations where the object is not present, even if present_at_all_locations is true. This can include locations that are deactivated. | [optional] 
**present_at_all_locations** | **bool** |  | [optional] 
**available_for_pickup** | **bool** |  | [optional] 
**available_online** | **bool** |  | [optional] 
**sku** | **str** | SKU of the item | [optional] 
**code** | **str** | Product code, e.g. UPC or EAN | [optional] 
**categories** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**options** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | List of options pertaining to this item&#39;s attribute variation | [optional] 
**variations** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**modifier_groups** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**available** | **bool, none_type** |  | [optional] 
**hidden** | **bool, none_type** |  | [optional] 
**version** | **str, none_type** |  | [optional] [readonly] 
**deleted** | **bool, none_type** |  | [optional] 
**updated_by** | **str, none_type** |  | [optional] [readonly] 
**created_by** | **str, none_type** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


