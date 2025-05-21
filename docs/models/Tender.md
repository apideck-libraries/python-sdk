# Tender


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**key** | **str, none_type** |  | [optional] 
**label** | **str, none_type** |  | [optional] 
**active** | **bool, none_type** |  | [optional] 
**hidden** | **bool, none_type** |  | [optional] 
**editable** | **bool, none_type** |  | [optional] 
**opens_cash_drawer** | **bool** | If this tender opens the cash drawer | [optional]  if omitted the server will use the default value of True
**allows_tipping** | **bool** | Allow tipping on payment from tender | [optional]  if omitted the server will use the default value of True
**custom_mappings** | [**CustomMappings**](CustomMappings.md) |  | [optional] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**pass_through** | [**PassThroughBody**](PassThroughBody.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


