# SessionSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unified_apis** | [**[UnifiedApiId]**](UnifiedApiId.md) | Provide the IDs of the Unified APIs you want to be visible. Leaving it empty or omiting this field will show all Unified APIs. | [optional] 
**hide_resource_settings** | **bool** |  | [optional]  if omitted the server will use the default value of False
**sandbox_mode** | **bool** | Configure [Vault](/apis/vault/reference#section/Get-Started) to show a banner informing the logged in user is in a test environment. | [optional]  if omitted the server will use the default value of False
**isolation_mode** | **bool** | Configure [Vault](/apis/vault/reference#section/Get-Started) to run in isolation mode, meaning it only shows the connection settings and hides the navigation items. | [optional]  if omitted the server will use the default value of False
**session_length** | **str** | The duration of time the session is valid for (maximum 1 week). | [optional]  if omitted the server will use the default value of "1h"
**show_logs** | **bool** | Configure [Vault](/apis/vault/reference#section/Get-Started) to show the logs page. Defaults to &#x60;true&#x60;. | [optional]  if omitted the server will use the default value of True
**show_suggestions** | **bool** | Configure [Vault](/apis/vault/reference#section/Get-Started) to show the suggestions page. Defaults to &#x60;false&#x60;. | [optional]  if omitted the server will use the default value of False
**show_sidebar** | **bool** | Configure [Vault](/apis/vault/reference#section/Get-Started) to show the sidebar. Defaults to &#x60;true&#x60;. | [optional]  if omitted the server will use the default value of True
**auto_redirect** | **bool** | Automatically redirect to redirect uri after the connection has been configured as callable. Defaults to &#x60;false&#x60;. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


