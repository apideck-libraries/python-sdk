# Job


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**slug** | **str, none_type** |  | [optional] 
**title** | **str, none_type** | The job title of the person. | [optional] 
**sequence** | **int** | Sequence in relation to other jobs. | [optional] 
**visibility** | **str** | The visibility of the job | [optional] 
**status** | [**JobStatus**](JobStatus.md) |  | [optional] 
**code** | **str** | The code of the job. | [optional] 
**language** | **str, none_type** | language code according to ISO 639-1. For the United States - EN | [optional] 
**employment_terms** | **str, none_type** |  | [optional] 
**experience** | **str** | Level of experience required for the job role. | [optional] 
**location** | **str, none_type** | Specifies the location for the job posting. | [optional] 
**remote** | **bool, none_type** | Specifies whether the posting is for a remote job. | [optional] 
**requisition_id** | **str** | A job&#39;s Requisition ID (Req ID) allows your organization to identify and track a job based on alphanumeric naming conventions unique to your company&#39;s internal processes. | [optional] 
**department** | [**Department**](Department.md) |  | [optional] 
**branch** | [**Branch**](Branch.md) |  | [optional] 
**recruiters** | **[str], none_type** | The recruiter is generally someone who is tasked to help the hiring manager find and screen qualified applicant | [optional] 
**hiring_managers** | **[str]** |  | [optional] 
**followers** | **[str], none_type** |  | [optional] 
**description** | **str, none_type** | A description of the object. | [optional] 
**description_html** | **str, none_type** | The job description in HTML format | [optional] 
**blocks** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**closing** | **str, none_type** |  | [optional] 
**closing_html** | **str, none_type** | The closing section of the job description in HTML format | [optional] 
**closing_date** | **date, none_type** |  | [optional] 
**salary** | [**JobSalary**](JobSalary.md) |  | [optional] 
**url** | **str, none_type** | URL of the job description | [optional] 
**job_portal_url** | **str, none_type** | URL of the job portal | [optional] 
**record_url** | **str, none_type** |  | [optional] 
**links** | [**[JobLinks]**](JobLinks.md) |  | [optional] 
**confidential** | **bool** |  | [optional] 
**available_to_employees** | **bool** | Specifies whether an employee of the organization can apply for the job. | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**custom_fields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**deleted** | **bool, none_type** | Flag to indicate if the object is deleted. | [optional] 
**owner_id** | **str, none_type** |  | [optional] 
**published_at** | **datetime, none_type** |  | [optional] [readonly] 
**custom_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | When custom mappings are configured on the resource, the result is included here. | [optional] [readonly] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


