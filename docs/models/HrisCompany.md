# HrisCompany


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_name** | **str, none_type** |  | 
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**display_name** | **str, none_type** |  | [optional] 
**subdomain** | **str, none_type** |  | [optional] 
**status** | **str** |  | [optional] 
**company_number** | **str, none_type** | An Company Number, Company ID or Company Code, is a unique number that has been assigned to each company. | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**phone_numbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**emails** | [**[Email]**](Email.md) |  | [optional] 
**websites** | [**[Website]**](Website.md) |  | [optional] 
**debtor_id** | **str, none_type** |  | [optional] 
**custom_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | When custom mappings are configured on the resource, the result is included here. | [optional] [readonly] 
**deleted** | **bool** |  | [optional] [readonly] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**pass_through** | [**PassThroughBody**](PassThroughBody.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


