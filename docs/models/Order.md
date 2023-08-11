# Order


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** |  | 
**location_id** | **str** |  | 
**id** | **str** | A unique identifier for an object. | [optional] [readonly] 
**idempotency_key** | [**IdempotencyKey**](IdempotencyKey.md) |  | [optional] 
**order_number** | **str** |  | [optional] 
**order_date** | **date, none_type** |  | [optional] 
**closed_date** | **date, none_type** |  | [optional] 
**reference_id** | **str, none_type** | An optional user-defined reference ID that associates this record with another entity in an external system. For example, a customer ID from an external customer management system. | [optional] 
**status** | **str** | Order status. Clover specific: If no value is set, the status defaults to hidden, which indicates a hidden order. A hidden order is not displayed in user interfaces and can only be retrieved by its id. When creating an order via the REST API the value must be manually set to &#39;open&#39;. More info [https://docs.clover.com/reference/orderupdateorder]() | [optional] 
**payment_status** | **str** | Is this order paid or not? | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**title** | **str** |  | [optional] 
**note** | **str** | A note with information about this order, may be printed on the order receipt and displayed in apps | [optional] 
**customer_id** | **str** |  | [optional] 
**employee_id** | **str** |  | [optional] 
**order_type_id** | **str** |  | [optional] 
**table** | **str** |  | [optional] 
**seat** | **str** |  | [optional] 
**total_amount** | **int, none_type** |  | [optional] 
**total_tip** | **int, none_type** |  | [optional] 
**total_tax** | **int, none_type** |  | [optional] 
**total_discount** | **int, none_type** |  | [optional] 
**total_refund** | **int, none_type** |  | [optional] 
**total_service_charge** | **int, none_type** |  | [optional] 
**refunded** | **bool** |  | [optional] 
**customers** | [**[OrderCustomers]**](OrderCustomers.md) |  | [optional] 
**fulfillments** | [**[OrderFulfillments]**](OrderFulfillments.md) |  | [optional] 
**line_items** | [**[OrderLineItems]**](OrderLineItems.md) |  | [optional] 
**payments** | [**[OrderPayments]**](OrderPayments.md) |  | [optional] 
**service_charges** | [**ServiceCharges**](ServiceCharges.md) |  | [optional] 
**refunds** | [**[OrderRefunds]**](OrderRefunds.md) |  | [optional] 
**taxes** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**discounts** | [**[OrderDiscounts]**](OrderDiscounts.md) |  | [optional] 
**tenders** | [**[OrderTenders]**](OrderTenders.md) |  | [optional] 
**source** | **str, none_type** | Source of order. Indicates the way that the order was placed. | [optional] [readonly] 
**voided** | **bool** |  | [optional] 
**voided_at** | **datetime** |  | [optional] [readonly] 
**version** | **str, none_type** |  | [optional] 
**updated_by** | **str, none_type** | The user who last updated the object. | [optional] [readonly] 
**created_by** | **str, none_type** | The user who created the object. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | The date and time when the object was last updated. | [optional] [readonly] 
**created_at** | **datetime, none_type** | The date and time when the object was created. | [optional] [readonly] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


