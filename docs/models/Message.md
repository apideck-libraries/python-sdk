# Message


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **str** | The phone number that initiated the message. | 
**to** | **str** | The phone number that received the message. | 
**body** | **str** | The message text. | 
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**subject** | **str** |  | [optional] 
**type** | **str** | Set to sms for SMS messages and mms for MMS messages. | [optional] 
**number_of_units** | **int** | The number of units that make up the complete message. Messages can be split up due to the constraints of the message size. | [optional] [readonly] 
**number_of_media_files** | **int** | The number of media files associated with the message. | [optional] [readonly] 
**direction** | **str** | The direction of the message. | [optional] [readonly] 
**status** | **str** | Status of the delivery of the message. | [optional] [readonly] 
**scheduled_at** | **datetime** | The scheduled date and time of the message. | [optional] 
**sent_at** | **datetime** | The date and time that the message was sent | [optional] [readonly] 
**webhook_url** | **str** | Define a webhook to receive delivery notifications. | [optional] 
**reference** | **str** | A client reference. | [optional] 
**price** | [**Price**](Price.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**messaging_service_id** | **str** | The ID of the Messaging Service used with the message. In case of Plivo this links to the Powerpack ID. | [optional] 
**custom_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | When custom mappings are configured on the resource, the result is included here. | [optional] [readonly] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 
**pass_through** | [**PassThroughBody**](PassThroughBody.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


