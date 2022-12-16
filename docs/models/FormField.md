# FormField


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the form field. | [optional] 
**label** | **str** | The label of the field | [optional] 
**placeholder** | **str, none_type** | The placeholder for the form field | [optional] 
**description** | **str, none_type** | The description of the form field | [optional] 
**type** | **str** |  | [optional] 
**required** | **bool** | Indicates if the form field is required, which means it must be filled in before the form can be submitted | [optional] 
**custom_field** | **bool** |  | [optional] 
**allow_custom_values** | **bool** | Only applicable to select fields. Allow the user to add a custom value though the option select if the desired value is not in the option select list. | [optional]  if omitted the server will use the default value of False
**disabled** | **bool, none_type** | Indicates if the form field is displayed in a “read-only” mode. | [optional] 
**hidden** | **bool, none_type** | Indicates if the form field is not displayed but the value that is being stored on the connection. | [optional] 
**sensitive** | **bool, none_type** | Indicates if the form field contains sensitive data, which will display the value as a masked input. | [optional] 
**options** | [**[FormFieldOption]**](FormFieldOption.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


