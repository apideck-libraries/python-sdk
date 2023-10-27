# Opportunity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title or name of the opportunity. | 
**primary_contact_id** | **str, none_type** | The unique identifier of the primary contact associated with the opportunity. | 
**id** | **str** | A unique identifier for the opportunity. | [optional] [readonly] 
**description** | **str, none_type** | A description of the opportunity. | [optional] 
**type** | **str, none_type** | The type of the opportunity | [optional] 
**monetary_amount** | **float, none_type** | The monetary value associated with the opportunity | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**win_probability** | **float, none_type** | The probability of winning the opportunity, expressed as a percentage. | [optional] 
**expected_revenue** | **float, none_type** | The expected revenue from the opportunity | [optional] [readonly] 
**close_date** | **date, none_type** | The actual closing date for the opportunity. If close_date is null, the opportunity is not closed yet. | [optional] 
**loss_reason_id** | **str, none_type** | The unique identifier of the reason why the opportunity was lost. | [optional] 
**loss_reason** | **str, none_type** | The reason why the opportunity was lost. | [optional] 
**won_reason_id** | **str, none_type** | The unique identifier of the reason why the opportunity was won. | [optional] 
**won_reason** | **str, none_type** | The reason why the opportunity was won. | [optional] 
**pipeline_id** | **str, none_type** | The unique identifier of the pipeline associated with the opportunity | [optional] 
**pipeline_stage_id** | **str, none_type** | The unique identifier of the stage in the pipeline associated with the opportunity. | [optional] 
**source_id** | **str, none_type** | The unique identifier of the source of the opportunity. | [optional] 
**lead_id** | **str, none_type** | The unique identifier of the lead associated with the opportunity. | [optional] 
**lead_source** | **str, none_type** | The source of the lead associated with the opportunity. | [optional] 
**contact_id** | **str, none_type** | The unique identifier of the contact associated with the opportunity. | [optional] 
**contact_ids** | **[str]** | An array of unique identifiers of all contacts associated with the opportunity. | [optional] 
**company_id** | **str, none_type** | The unique identifier of the company associated with the opportunity. | [optional] 
**company_name** | **str, none_type** | The name of the company associated with the opportunity. | [optional] 
**owner_id** | **str, none_type** | The unique identifier of the user who owns the opportunity. | [optional] 
**priority** | **str, none_type** | The priority level of the opportunity. | [optional] 
**status** | **str, none_type** | The current status of the opportunity. | [optional] 
**status_id** | **str, none_type** | The unique identifier of the current status of the opportunity. | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**interaction_count** | **float, none_type** | The number of interactions with the opportunity. | [optional] [readonly] 
**custom_fields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**stage_last_changed_at** | **datetime, none_type** | The date and time when the stage of the opportunity was last changed. | [optional] 
**last_activity_at** | **str, none_type** | The date and time of the last activity associated with the opportunity. | [optional] [readonly] 
**deleted** | **bool** | Indicates whether the opportunity has been deleted. | [optional] [readonly] 
**date_stage_changed** | **datetime, none_type** | The date and time when the stage of the opportunity was last changed. | [optional] [readonly] 
**date_last_contacted** | **datetime, none_type** | The date and time when the opportunity was last contacted. | [optional] [readonly] 
**date_lead_created** | **datetime, none_type** | The date and time when the lead associated with the opportunity was created. | [optional] [readonly] 
**custom_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | When custom mappings are configured on the resource, the result is included here. | [optional] [readonly] 
**updated_by** | **str, none_type** | The unique identifier of the user who last updated the opportunity. | [optional] [readonly] 
**created_by** | **str, none_type** | The unique identifier of the user who created the opportunity. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the opportunity was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the opportunity was created. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


