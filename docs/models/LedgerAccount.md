# LedgerAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**display_id** | **str** | The human readable display ID used when displaying the account | [optional] 
**nominal_code** | **str, none_type** | The nominal code of the ledger account. | [optional] 
**code** | **str, none_type** | The code assigned to the account. | [optional] 
**classification** | **str, none_type** | The classification of account. | [optional] 
**type** | **str** | The type of account. | [optional] 
**sub_type** | **str, none_type** | The sub type of account. | [optional] 
**name** | **str, none_type** | The name of the account. | [optional] 
**fully_qualified_name** | **str, none_type** | The fully qualified name of the account. | [optional] 
**description** | **str, none_type** | The description of the account. | [optional] 
**opening_balance** | **float, none_type** | The opening balance of the account. | [optional] 
**current_balance** | **float, none_type** | The current balance of the account. | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**tax_type** | **str, none_type** | The tax type of the account. | [optional] 
**tax_rate** | [**LinkedTaxRate**](LinkedTaxRate.md) |  | [optional] 
**level** | **float, none_type** |  | [optional] 
**active** | **bool, none_type** | Whether the account is active or not. | [optional] 
**status** | **str, none_type** | The status of the account. | [optional] 
**header** | **bool, none_type** | Whether the account is a header or not. | [optional] 
**bank_account** | [**BankAccount**](BankAccount.md) |  | [optional] 
**categories** | [**[LedgerAccountCategories]**](LedgerAccountCategories.md) | The categories of the account. | [optional] [readonly] 
**parent_account** | [**LedgerAccountParentAccount**](LedgerAccountParentAccount.md) |  | [optional] 
**sub_account** | **bool, none_type** | Whether the account is a sub account or not. | [optional] 
**sub_accounts** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | The sub accounts of the account. | [optional] [readonly] 
**last_reconciliation_date** | **date, none_type** | Reconciliation Date means the last calendar day of each Reconciliation Period. | [optional] 
**custom_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | When custom mappings are configured on the resource, the result is included here. | [optional] [readonly] 
**row_version** | **str, none_type** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


