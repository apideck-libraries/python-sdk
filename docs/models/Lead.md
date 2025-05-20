# Lead


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Full name of the lead. | 
**id** | **str** | Unique identifier for the contact. | [optional] [readonly] 
**company_name** | **str, none_type** | The name of the company the lead is associated with. | [optional] 
**owner_id** | **str, none_type** | The owner of the lead. | [optional] 
**owner_name** | **str, none_type** | The name of the owner of the lead. | [optional] 
**company_id** | **str, none_type** | The company the lead is associated with. | [optional] 
**lead_id** | **str, none_type** | The identifier of the lead. | [optional] 
**lead_source** | **str, none_type** | The source of the lead. | [optional] 
**first_name** | **str, none_type** | The first name of the lead. | [optional] 
**last_name** | **str, none_type** | The last name of the lead. | [optional] 
**description** | **str, none_type** | The description of the lead. | [optional] 
**prefix** | **str, none_type** | The prefix of the lead. | [optional] 
**title** | **str, none_type** | The job title of the lead. | [optional] 
**language** | **str, none_type** | language code according to ISO 639-1. For the United States - EN | [optional] 
**status** | **str, none_type** |  | [optional] 
**monetary_amount** | **float, none_type** | The monetary amount of the lead. | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**fax** | **str, none_type** | The fax number of the lead. | [optional] 
**websites** | [**[Website]**](Website.md) |  | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**social_links** | [**[SocialLink]**](SocialLink.md) |  | [optional] 
**phone_numbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**emails** | [**[Email]**](Email.md) |  | [optional] 
**custom_fields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**custom_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | When custom mappings are configured on the resource, the result is included here. | [optional] [readonly] 
**updated_at** | **str, none_type** | Date updated in ISO 8601 format | [optional] [readonly] 
**created_at** | **str, none_type** | Date created in ISO 8601 format | [optional] [readonly] 
**pass_through** | [**PassThroughBody**](PassThroughBody.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


