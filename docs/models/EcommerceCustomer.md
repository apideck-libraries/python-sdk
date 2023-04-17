# EcommerceCustomer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for an object. | [readonly] 
**name** | **str** | Full name of the customer | [optional] 
**first_name** | **str** | First name of the customer | [optional] 
**last_name** | **str** | Last name of the customer | [optional] 
**company_name** | **str** | Company name of the customer | [optional] 
**status** | **str** | The current status of the customer | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**emails** | [**[Email]**](Email.md) | An array of email addresses for the customer. | [optional] 
**phone_numbers** | [**[PhoneNumber]**](PhoneNumber.md) | An array of phone numbers for the customer. | [optional] 
**addresses** | [**[EcommerceCustomerAddresses]**](EcommerceCustomerAddresses.md) | An array of addresses for the customer. | [optional] 
**orders** | [**[LinkedEcommerceOrder]**](LinkedEcommerceOrder.md) |  | [optional] 
**created_at** | **datetime** | The date and time when the object was created. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


