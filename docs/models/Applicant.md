# Applicant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**name** | **str** | The name of an applicant. | [optional] 
**first_name** | **str, none_type** | The first name of the person. | [optional] 
**last_name** | **str, none_type** | The last name of the person. | [optional] 
**middle_name** | **str, none_type** | Middle name of the person. | [optional] 
**initials** | **str, none_type** | The initials of the person, usually derived from their first, middle, and last names. | [optional] 
**birthday** | **date, none_type** | The date of birth of the person. | [optional] 
**cover_letter** | **str** |  | [optional] 
**job_url** | **str, none_type** |  | [optional] [readonly] 
**photo_url** | **str, none_type** | The URL of the photo of a person. | [optional] 
**headline** | **str** | Typically a list of previous companies where the contact has worked or schools that the contact has attended | [optional] 
**title** | **str, none_type** | The job title of the person. | [optional] 
**emails** | [**[Email]**](Email.md) |  | [optional] 
**custom_fields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**phone_numbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**websites** | [**[ApplicantWebsites]**](ApplicantWebsites.md) |  | [optional] 
**social_links** | [**[ApplicantSocialLinks]**](ApplicantSocialLinks.md) |  | [optional] 
**stage_id** | **str** |  | [optional] 
**recruiter_id** | **str** |  | [optional] 
**coordinator_id** | **str** |  | [optional] 
**application_ids** | **[str], none_type** |  | [optional] 
**applications** | **[str], none_type** |  | [optional] 
**followers** | **[str], none_type** |  | [optional] 
**sources** | **[str], none_type** |  | [optional] 
**source_id** | **str** |  | [optional] [readonly] 
**confidential** | **bool** |  | [optional] 
**anonymized** | **bool** |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**archived** | **bool, none_type** |  | [optional] 
**last_interaction_at** | **datetime, none_type** |  | [optional] [readonly] 
**owner_id** | **str, none_type** |  | [optional] 
**sourced_by** | **str, none_type** |  | [optional] [readonly] 
**cv_url** | **str** |  | [optional] [readonly] 
**record_url** | **str, none_type** |  | [optional] 
**rejected_at** | **datetime, none_type** |  | [optional] [readonly] 
**custom_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | When custom mappings are configured on the resource, the result is included here. | [optional] [readonly] 
**deleted** | **bool, none_type** | Flag to indicate if the object is deleted. | [optional] 
**deleted_by** | **str, none_type** | The user who deleted the object. | [optional] [readonly] 
**deleted_at** | **datetime, none_type** | The time at which the object was deleted. | [optional] [readonly] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


