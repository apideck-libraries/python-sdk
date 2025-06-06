# Apideck Python SDK

> ⚠️ **DEPRECATION NOTICE**: This SDK is deprecated and will be archived on May 31, 2025. Please transition to the [new SDK](https://github.com/apideck-libraries/sdk-python) before this date. After May 31, 2025, this repository will be archived and will no longer receive any updates. To support you during this transition please refer to our [migration guide](https://developers.apideck.com/guides/sdk-migration).

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Installation](#installation--usage)
- [Getting started](#getting-started)
- [Example](#example)
- [Support](#support)
- [License](#license)

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

```sh
pip install apideck
```

or you can install directly using:

```sh
pip install git+https://github.com/apideck-libraries/python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/apideck-libraries/python-sdk.git`)

Then import the package:
```python
import apideck
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import apideck
```

## Getting started

The module supports all Apideck API endpoints. For complete information about the API, head
to the [docs][2].

## Example

Retrieving a list of all contacts and updating the first record with a new address.

```python
import apideck
from apideck.api import crm_api
from apideck.model.contacts_sort import ContactsSort
from apideck.model.sort_direction import SortDirection
from pprint import pprint

configuration = apideck.Configuration()

configuration.api_key['apiKey'] = '<insert-api-key-here>'
configuration.api_key_prefix['apiKey'] = 'Bearer'

with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = crm_api.CrmApi(api_client)
    raw = False
    consumer_id = '<insert-consumer-id-here>'
    app_id = '<insert-application-id-here>'
    service_id = '<insert-service-id-here>'
    limit = 20

    sort = ContactsSort(
        by="name",
        direction=SortDirection("asc"),
    ) 
    

    try:
        # List contacts
        api_response = api_instance.contacts_all(raw=raw, consumer_id=consumer_id, app_id=app_id, service_id=service_id, limit=limit, sort=sort)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling CrmApi->contacts_all: %s\n" % e)
```

## Apideck Unified Apis

The following Apis are currently available:

### AccountingApi

Read the full documentation of the AccountingApi [here](./docs/apis/AccountingApi.md).

### AtsApi

Read the full documentation of the AtsApi [here](./docs/apis/AtsApi.md).

### ConnectorApi

Read the full documentation of the ConnectorApi [here](./docs/apis/ConnectorApi.md).

### CrmApi

Read the full documentation of the CrmApi [here](./docs/apis/CrmApi.md).

### EcommerceApi

Read the full documentation of the EcommerceApi [here](./docs/apis/EcommerceApi.md).

### FileStorageApi

Read the full documentation of the FileStorageApi [here](./docs/apis/FileStorageApi.md).

### HrisApi

Read the full documentation of the HrisApi [here](./docs/apis/HrisApi.md).

### IssueTrackingApi

Read the full documentation of the IssueTrackingApi [here](./docs/apis/IssueTrackingApi.md).

### LeadApi

Read the full documentation of the LeadApi [here](./docs/apis/LeadApi.md).

### PosApi

Read the full documentation of the PosApi [here](./docs/apis/PosApi.md).

### SmsApi

Read the full documentation of the SmsApi [here](./docs/apis/SmsApi.md).

### VaultApi

Read the full documentation of the VaultApi [here](./docs/apis/VaultApi.md).

### WebhookApi

Read the full documentation of the WebhookApi [here](./docs/apis/WebhookApi.md).


### Utils

#### uploadFile

A utility for uploading files using the File Storage API. `uploadFile` will automatically use upload sessions for files larger than 4MB. Smaller files will be uploaded with a simple upload call.

**Example Usage**


## Support

Open an [issue][3]!

## License

[Apache-2.0][4]

[1]: https://apideck.com
[2]: https://developers.apideck.com/
[3]: https://github.com/apideck-libraries/python-sdk/issues/new
[4]: https://github.com/apideck-libraries/python-sdk/blob/main/LICENSE


```python

import time
import apideck
from pprint import pprint
from apideck.api import accounting_api
from apideck.model.accounting_department import AccountingDepartment
from apideck.model.accounting_departments_filter import AccountingDepartmentsFilter
from apideck.model.accounting_location import AccountingLocation
from apideck.model.accounting_locations_filter import AccountingLocationsFilter
from apideck.model.aged_report_filter import AgedReportFilter
from apideck.model.attachment_reference_type import AttachmentReferenceType
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.balance_sheet_filter import BalanceSheetFilter
from apideck.model.bank_feed_account import BankFeedAccount
from apideck.model.bank_feed_statement import BankFeedStatement
from apideck.model.bill import Bill
from apideck.model.bill_payment import BillPayment
from apideck.model.bills_filter import BillsFilter
from apideck.model.bills_sort import BillsSort
from apideck.model.create_accounting_department_response import CreateAccountingDepartmentResponse
from apideck.model.create_accounting_location_response import CreateAccountingLocationResponse
from apideck.model.create_bank_feed_account_response import CreateBankFeedAccountResponse
from apideck.model.create_bank_feed_statement_response import CreateBankFeedStatementResponse
from apideck.model.create_bill_payment_response import CreateBillPaymentResponse
from apideck.model.create_bill_response import CreateBillResponse
from apideck.model.create_credit_note_response import CreateCreditNoteResponse
from apideck.model.create_customer_response import CreateCustomerResponse
from apideck.model.create_expense_response import CreateExpenseResponse
from apideck.model.create_invoice_item_response import CreateInvoiceItemResponse
from apideck.model.create_invoice_response import CreateInvoiceResponse
from apideck.model.create_journal_entry_response import CreateJournalEntryResponse
from apideck.model.create_ledger_account_response import CreateLedgerAccountResponse
from apideck.model.create_payment_response import CreatePaymentResponse
from apideck.model.create_purchase_order_response import CreatePurchaseOrderResponse
from apideck.model.create_subsidiary_response import CreateSubsidiaryResponse
from apideck.model.create_supplier_response import CreateSupplierResponse
from apideck.model.create_tax_rate_response import CreateTaxRateResponse
from apideck.model.create_tracking_category_response import CreateTrackingCategoryResponse
from apideck.model.credit_note import CreditNote
from apideck.model.credit_notes_filter import CreditNotesFilter
from apideck.model.credit_notes_sort import CreditNotesSort
from apideck.model.customer import Customer
from apideck.model.customers_filter import CustomersFilter
from apideck.model.customers_sort import CustomersSort
from apideck.model.delete_accounting_department_response import DeleteAccountingDepartmentResponse
from apideck.model.delete_accounting_location_response import DeleteAccountingLocationResponse
from apideck.model.delete_attachment_response import DeleteAttachmentResponse
from apideck.model.delete_bank_feed_account_response import DeleteBankFeedAccountResponse
from apideck.model.delete_bank_feed_statement_response import DeleteBankFeedStatementResponse
from apideck.model.delete_bill_payment_response import DeleteBillPaymentResponse
from apideck.model.delete_bill_response import DeleteBillResponse
from apideck.model.delete_credit_note_response import DeleteCreditNoteResponse
from apideck.model.delete_customer_response import DeleteCustomerResponse
from apideck.model.delete_expense_response import DeleteExpenseResponse
from apideck.model.delete_invoice_response import DeleteInvoiceResponse
from apideck.model.delete_journal_entry_response import DeleteJournalEntryResponse
from apideck.model.delete_ledger_account_response import DeleteLedgerAccountResponse
from apideck.model.delete_payment_response import DeletePaymentResponse
from apideck.model.delete_purchase_order_response import DeletePurchaseOrderResponse
from apideck.model.delete_subsidiary_response import DeleteSubsidiaryResponse
from apideck.model.delete_supplier_response import DeleteSupplierResponse
from apideck.model.delete_tax_rate_response import DeleteTaxRateResponse
from apideck.model.delete_tracking_category_response import DeleteTrackingCategoryResponse
from apideck.model.expense import Expense
from apideck.model.get_accounting_department_response import GetAccountingDepartmentResponse
from apideck.model.get_accounting_departments_response import GetAccountingDepartmentsResponse
from apideck.model.get_accounting_location_response import GetAccountingLocationResponse
from apideck.model.get_accounting_locations_response import GetAccountingLocationsResponse
from apideck.model.get_aged_creditors_response import GetAgedCreditorsResponse
from apideck.model.get_aged_debtors_response import GetAgedDebtorsResponse
from apideck.model.get_attachment_response import GetAttachmentResponse
from apideck.model.get_attachments_response import GetAttachmentsResponse
from apideck.model.get_balance_sheet_response import GetBalanceSheetResponse
from apideck.model.get_bank_feed_account_response import GetBankFeedAccountResponse
from apideck.model.get_bank_feed_accounts_response import GetBankFeedAccountsResponse
from apideck.model.get_bank_feed_statement_response import GetBankFeedStatementResponse
from apideck.model.get_bank_feed_statements_response import GetBankFeedStatementsResponse
from apideck.model.get_bill_payment_response import GetBillPaymentResponse
from apideck.model.get_bill_payments_response import GetBillPaymentsResponse
from apideck.model.get_bill_response import GetBillResponse
from apideck.model.get_bills_response import GetBillsResponse
from apideck.model.get_company_info_response import GetCompanyInfoResponse
from apideck.model.get_credit_note_response import GetCreditNoteResponse
from apideck.model.get_credit_notes_response import GetCreditNotesResponse
from apideck.model.get_customer_response import GetCustomerResponse
from apideck.model.get_customers_response import GetCustomersResponse
from apideck.model.get_expense_response import GetExpenseResponse
from apideck.model.get_expenses_response import GetExpensesResponse
from apideck.model.get_invoice_item_response import GetInvoiceItemResponse
from apideck.model.get_invoice_items_response import GetInvoiceItemsResponse
from apideck.model.get_invoice_response import GetInvoiceResponse
from apideck.model.get_invoices_response import GetInvoicesResponse
from apideck.model.get_journal_entries_response import GetJournalEntriesResponse
from apideck.model.get_journal_entry_response import GetJournalEntryResponse
from apideck.model.get_ledger_account_response import GetLedgerAccountResponse
from apideck.model.get_ledger_accounts_response import GetLedgerAccountsResponse
from apideck.model.get_payment_response import GetPaymentResponse
from apideck.model.get_payments_response import GetPaymentsResponse
from apideck.model.get_profit_and_loss_response import GetProfitAndLossResponse
from apideck.model.get_purchase_order_response import GetPurchaseOrderResponse
from apideck.model.get_purchase_orders_response import GetPurchaseOrdersResponse
from apideck.model.get_subsidiaries_response import GetSubsidiariesResponse
from apideck.model.get_subsidiary_response import GetSubsidiaryResponse
from apideck.model.get_supplier_response import GetSupplierResponse
from apideck.model.get_suppliers_response import GetSuppliersResponse
from apideck.model.get_tax_rate_response import GetTaxRateResponse
from apideck.model.get_tax_rates_response import GetTaxRatesResponse
from apideck.model.get_tracking_categories_response import GetTrackingCategoriesResponse
from apideck.model.get_tracking_category_response import GetTrackingCategoryResponse
from apideck.model.invoice import Invoice
from apideck.model.invoice_item import InvoiceItem
from apideck.model.invoice_item_filter import InvoiceItemFilter
from apideck.model.invoice_items_filter import InvoiceItemsFilter
from apideck.model.invoice_items_sort import InvoiceItemsSort
from apideck.model.invoices_filter import InvoicesFilter
from apideck.model.invoices_sort import InvoicesSort
from apideck.model.journal_entries_filter import JournalEntriesFilter
from apideck.model.journal_entries_sort import JournalEntriesSort
from apideck.model.journal_entry import JournalEntry
from apideck.model.ledger_account import LedgerAccount
from apideck.model.ledger_accounts_filter import LedgerAccountsFilter
from apideck.model.ledger_accounts_sort import LedgerAccountsSort
from apideck.model.not_found_response import NotFoundResponse
from apideck.model.pass_through_query import PassThroughQuery
from apideck.model.payment import Payment
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.payments_filter import PaymentsFilter
from apideck.model.payments_sort import PaymentsSort
from apideck.model.profit_and_loss_filter import ProfitAndLossFilter
from apideck.model.purchase_order import PurchaseOrder
from apideck.model.purchase_orders_filter import PurchaseOrdersFilter
from apideck.model.purchase_orders_sort import PurchaseOrdersSort
from apideck.model.subsidiary import Subsidiary
from apideck.model.supplier import Supplier
from apideck.model.suppliers_filter import SuppliersFilter
from apideck.model.suppliers_sort import SuppliersSort
from apideck.model.tax_rate import TaxRate
from apideck.model.tax_rates_filter import TaxRatesFilter
from apideck.model.tracking_category import TrackingCategory
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.update_accounting_department_response import UpdateAccountingDepartmentResponse
from apideck.model.update_accounting_location_response import UpdateAccountingLocationResponse
from apideck.model.update_bank_feed_account_response import UpdateBankFeedAccountResponse
from apideck.model.update_bank_feed_statement_response import UpdateBankFeedStatementResponse
from apideck.model.update_bill_payment_response import UpdateBillPaymentResponse
from apideck.model.update_bill_response import UpdateBillResponse
from apideck.model.update_credit_note_response import UpdateCreditNoteResponse
from apideck.model.update_customer_response import UpdateCustomerResponse
from apideck.model.update_expense_response import UpdateExpenseResponse
from apideck.model.update_invoice_items_response import UpdateInvoiceItemsResponse
from apideck.model.update_invoice_response import UpdateInvoiceResponse
from apideck.model.update_journal_entry_response import UpdateJournalEntryResponse
from apideck.model.update_ledger_account_response import UpdateLedgerAccountResponse
from apideck.model.update_payment_response import UpdatePaymentResponse
from apideck.model.update_purchase_order_response import UpdatePurchaseOrderResponse
from apideck.model.update_subsidiary_response import UpdateSubsidiaryResponse
from apideck.model.update_supplier_response import UpdateSupplierResponse
from apideck.model.update_tax_rate_response import UpdateTaxRateResponse
from apideck.model.update_tracking_category_response import UpdateTrackingCategoryResponse
# Defining the host is optional and defaults to https://unify.apideck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = apideck.Configuration(
    host = "https://unify.apideck.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'


# Enter a context with an instance of the API client
with apideck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounting_api.AccountingApi(api_client)
    raw = False # bool | Include raw response. Mostly used for debugging purposes (optional) (default to False)
x_apideck_consumer_id = "test-consumer" # str | ID of the consumer which you want to get or push data from (optional)
x_apideck_app_id = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX" # str | The ID of your Unify application (optional)
x_apideck_service_id = "salesforce" # str | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (optional)
filter = AgedReportFilter(
        customer_id="123abc",
        supplier_id="123abc",
        report_as_of_date="2024-01-01",
        period_count=3,
        period_length=30,
    ) # AgedReportFilter | Apply filters (optional)
pass_through = PassThroughQuery() # PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads (optional)
fields = "id,updated_at" # str, none_type | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded. (optional)

    try:
        # Get Aged Creditors
        api_response = api_instance.aged_creditors_one(raw=raw, x_apideck_consumer_id=x_apideck_consumer_id, x_apideck_app_id=x_apideck_app_id, x_apideck_service_id=x_apideck_service_id, filter=filter, pass_through=pass_through, fields=fields)
        pprint(api_response)
    except apideck.ApiException as e:
        print("Exception when calling AccountingApi->aged_creditors_one: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to _https://unify.apideck.com_

| Class                                                             | Method                                                                         | HTTP request                | Description |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------ | --------------------------- | ----------- |
| _AccountingApi_ | [**aged_creditors_one**](docs/apis/AccountingApi.md#aged_creditors_one) | **GET** /accounting/aged-creditors | Get Aged Creditors |

_AccountingApi_ | [**aged_debtors_one**](docs/apis/AccountingApi.md#aged_debtors_one) | **GET** /accounting/aged-debtors | Get Aged Debtors |

_AccountingApi_ | [**attachments_all**](docs/apis/AccountingApi.md#attachments_all) | **GET** /accounting/attachments/{reference_type}/{reference_id} | List Attachments |

_AccountingApi_ | [**attachments_delete**](docs/apis/AccountingApi.md#attachments_delete) | **DELETE** /accounting/attachments/{reference_type}/{reference_id}/{id} | Delete Attachment |

_AccountingApi_ | [**attachments_download**](docs/apis/AccountingApi.md#attachments_download) | **GET** /accounting/attachments/{reference_type}/{reference_id}/{id}/download | Download Attachment |

_AccountingApi_ | [**attachments_one**](docs/apis/AccountingApi.md#attachments_one) | **GET** /accounting/attachments/{reference_type}/{reference_id}/{id} | Get Attachment |

_AccountingApi_ | [**balance_sheet_one**](docs/apis/AccountingApi.md#balance_sheet_one) | **GET** /accounting/balance-sheet | Get BalanceSheet |

_AccountingApi_ | [**bank_feed_accounts_add**](docs/apis/AccountingApi.md#bank_feed_accounts_add) | **POST** /accounting/bank-feed-accounts | Create Bank Feed Account |

_AccountingApi_ | [**bank_feed_accounts_all**](docs/apis/AccountingApi.md#bank_feed_accounts_all) | **GET** /accounting/bank-feed-accounts | List Bank Feed Accounts |

_AccountingApi_ | [**bank_feed_accounts_delete**](docs/apis/AccountingApi.md#bank_feed_accounts_delete) | **DELETE** /accounting/bank-feed-accounts/{id} | Delete Bank Feed Account |

_AccountingApi_ | [**bank_feed_accounts_one**](docs/apis/AccountingApi.md#bank_feed_accounts_one) | **GET** /accounting/bank-feed-accounts/{id} | Get Bank Feed Account |

_AccountingApi_ | [**bank_feed_accounts_update**](docs/apis/AccountingApi.md#bank_feed_accounts_update) | **PATCH** /accounting/bank-feed-accounts/{id} | Update Bank Feed Account |

_AccountingApi_ | [**bank_feed_statements_add**](docs/apis/AccountingApi.md#bank_feed_statements_add) | **POST** /accounting/bank-feed-statements | Create Bank Feed Statement |

_AccountingApi_ | [**bank_feed_statements_all**](docs/apis/AccountingApi.md#bank_feed_statements_all) | **GET** /accounting/bank-feed-statements | List Bank Feed Statements |

_AccountingApi_ | [**bank_feed_statements_delete**](docs/apis/AccountingApi.md#bank_feed_statements_delete) | **DELETE** /accounting/bank-feed-statements/{id} | Delete Bank Feed Statement |

_AccountingApi_ | [**bank_feed_statements_one**](docs/apis/AccountingApi.md#bank_feed_statements_one) | **GET** /accounting/bank-feed-statements/{id} | Get Bank Feed Statement |

_AccountingApi_ | [**bank_feed_statements_update**](docs/apis/AccountingApi.md#bank_feed_statements_update) | **PATCH** /accounting/bank-feed-statements/{id} | Update Bank Feed Statement |

_AccountingApi_ | [**bill_payments_add**](docs/apis/AccountingApi.md#bill_payments_add) | **POST** /accounting/bill-payments | Create Bill Payment |

_AccountingApi_ | [**bill_payments_all**](docs/apis/AccountingApi.md#bill_payments_all) | **GET** /accounting/bill-payments | List Bill Payments |

_AccountingApi_ | [**bill_payments_delete**](docs/apis/AccountingApi.md#bill_payments_delete) | **DELETE** /accounting/bill-payments/{id} | Delete Bill Payment |

_AccountingApi_ | [**bill_payments_one**](docs/apis/AccountingApi.md#bill_payments_one) | **GET** /accounting/bill-payments/{id} | Get Bill Payment |

_AccountingApi_ | [**bill_payments_update**](docs/apis/AccountingApi.md#bill_payments_update) | **PATCH** /accounting/bill-payments/{id} | Update Bill Payment |

_AccountingApi_ | [**bills_add**](docs/apis/AccountingApi.md#bills_add) | **POST** /accounting/bills | Create Bill |

_AccountingApi_ | [**bills_all**](docs/apis/AccountingApi.md#bills_all) | **GET** /accounting/bills | List Bills |

_AccountingApi_ | [**bills_delete**](docs/apis/AccountingApi.md#bills_delete) | **DELETE** /accounting/bills/{id} | Delete Bill |

_AccountingApi_ | [**bills_one**](docs/apis/AccountingApi.md#bills_one) | **GET** /accounting/bills/{id} | Get Bill |

_AccountingApi_ | [**bills_update**](docs/apis/AccountingApi.md#bills_update) | **PATCH** /accounting/bills/{id} | Update Bill |

_AccountingApi_ | [**company_info_one**](docs/apis/AccountingApi.md#company_info_one) | **GET** /accounting/company-info | Get company info |

_AccountingApi_ | [**credit_notes_add**](docs/apis/AccountingApi.md#credit_notes_add) | **POST** /accounting/credit-notes | Create Credit Note |

_AccountingApi_ | [**credit_notes_all**](docs/apis/AccountingApi.md#credit_notes_all) | **GET** /accounting/credit-notes | List Credit Notes |

_AccountingApi_ | [**credit_notes_delete**](docs/apis/AccountingApi.md#credit_notes_delete) | **DELETE** /accounting/credit-notes/{id} | Delete Credit Note |

_AccountingApi_ | [**credit_notes_one**](docs/apis/AccountingApi.md#credit_notes_one) | **GET** /accounting/credit-notes/{id} | Get Credit Note |

_AccountingApi_ | [**credit_notes_update**](docs/apis/AccountingApi.md#credit_notes_update) | **PATCH** /accounting/credit-notes/{id} | Update Credit Note |

_AccountingApi_ | [**customers_add**](docs/apis/AccountingApi.md#customers_add) | **POST** /accounting/customers | Create Customer |

_AccountingApi_ | [**customers_all**](docs/apis/AccountingApi.md#customers_all) | **GET** /accounting/customers | List Customers |

_AccountingApi_ | [**customers_delete**](docs/apis/AccountingApi.md#customers_delete) | **DELETE** /accounting/customers/{id} | Delete Customer |

_AccountingApi_ | [**customers_one**](docs/apis/AccountingApi.md#customers_one) | **GET** /accounting/customers/{id} | Get Customer |

_AccountingApi_ | [**customers_update**](docs/apis/AccountingApi.md#customers_update) | **PATCH** /accounting/customers/{id} | Update Customer |

_AccountingApi_ | [**departments_add**](docs/apis/AccountingApi.md#departments_add) | **POST** /accounting/departments | Create Department |

_AccountingApi_ | [**departments_all**](docs/apis/AccountingApi.md#departments_all) | **GET** /accounting/departments | List Departments |

_AccountingApi_ | [**departments_delete**](docs/apis/AccountingApi.md#departments_delete) | **DELETE** /accounting/departments/{id} | Delete Department |

_AccountingApi_ | [**departments_one**](docs/apis/AccountingApi.md#departments_one) | **GET** /accounting/departments/{id} | Get Department |

_AccountingApi_ | [**departments_update**](docs/apis/AccountingApi.md#departments_update) | **PATCH** /accounting/departments/{id} | Update Department |

_AccountingApi_ | [**expenses_add**](docs/apis/AccountingApi.md#expenses_add) | **POST** /accounting/expenses | Create Expense |

_AccountingApi_ | [**expenses_all**](docs/apis/AccountingApi.md#expenses_all) | **GET** /accounting/expenses | List Expenses |

_AccountingApi_ | [**expenses_delete**](docs/apis/AccountingApi.md#expenses_delete) | **DELETE** /accounting/expenses/{id} | Delete Expense |

_AccountingApi_ | [**expenses_one**](docs/apis/AccountingApi.md#expenses_one) | **GET** /accounting/expenses/{id} | Get Expense |

_AccountingApi_ | [**expenses_update**](docs/apis/AccountingApi.md#expenses_update) | **PATCH** /accounting/expenses/{id} | Update Expense |

_AccountingApi_ | [**invoice_items_add**](docs/apis/AccountingApi.md#invoice_items_add) | **POST** /accounting/invoice-items | Create Invoice Item |

_AccountingApi_ | [**invoice_items_all**](docs/apis/AccountingApi.md#invoice_items_all) | **GET** /accounting/invoice-items | List Invoice Items |

_AccountingApi_ | [**invoice_items_delete**](docs/apis/AccountingApi.md#invoice_items_delete) | **DELETE** /accounting/invoice-items/{id} | Delete Invoice Item |

_AccountingApi_ | [**invoice_items_one**](docs/apis/AccountingApi.md#invoice_items_one) | **GET** /accounting/invoice-items/{id} | Get Invoice Item |

_AccountingApi_ | [**invoice_items_update**](docs/apis/AccountingApi.md#invoice_items_update) | **PATCH** /accounting/invoice-items/{id} | Update Invoice Item |

_AccountingApi_ | [**invoices_add**](docs/apis/AccountingApi.md#invoices_add) | **POST** /accounting/invoices | Create Invoice |

_AccountingApi_ | [**invoices_all**](docs/apis/AccountingApi.md#invoices_all) | **GET** /accounting/invoices | List Invoices |

_AccountingApi_ | [**invoices_delete**](docs/apis/AccountingApi.md#invoices_delete) | **DELETE** /accounting/invoices/{id} | Delete Invoice |

_AccountingApi_ | [**invoices_one**](docs/apis/AccountingApi.md#invoices_one) | **GET** /accounting/invoices/{id} | Get Invoice |

_AccountingApi_ | [**invoices_update**](docs/apis/AccountingApi.md#invoices_update) | **PATCH** /accounting/invoices/{id} | Update Invoice |

_AccountingApi_ | [**journal_entries_add**](docs/apis/AccountingApi.md#journal_entries_add) | **POST** /accounting/journal-entries | Create Journal Entry |

_AccountingApi_ | [**journal_entries_all**](docs/apis/AccountingApi.md#journal_entries_all) | **GET** /accounting/journal-entries | List Journal Entries |

_AccountingApi_ | [**journal_entries_delete**](docs/apis/AccountingApi.md#journal_entries_delete) | **DELETE** /accounting/journal-entries/{id} | Delete Journal Entry |

_AccountingApi_ | [**journal_entries_one**](docs/apis/AccountingApi.md#journal_entries_one) | **GET** /accounting/journal-entries/{id} | Get Journal Entry |

_AccountingApi_ | [**journal_entries_update**](docs/apis/AccountingApi.md#journal_entries_update) | **PATCH** /accounting/journal-entries/{id} | Update Journal Entry |

_AccountingApi_ | [**ledger_accounts_add**](docs/apis/AccountingApi.md#ledger_accounts_add) | **POST** /accounting/ledger-accounts | Create Ledger Account |

_AccountingApi_ | [**ledger_accounts_all**](docs/apis/AccountingApi.md#ledger_accounts_all) | **GET** /accounting/ledger-accounts | List Ledger Accounts |

_AccountingApi_ | [**ledger_accounts_delete**](docs/apis/AccountingApi.md#ledger_accounts_delete) | **DELETE** /accounting/ledger-accounts/{id} | Delete Ledger Account |

_AccountingApi_ | [**ledger_accounts_one**](docs/apis/AccountingApi.md#ledger_accounts_one) | **GET** /accounting/ledger-accounts/{id} | Get Ledger Account |

_AccountingApi_ | [**ledger_accounts_update**](docs/apis/AccountingApi.md#ledger_accounts_update) | **PATCH** /accounting/ledger-accounts/{id} | Update Ledger Account |

_AccountingApi_ | [**locations_add**](docs/apis/AccountingApi.md#locations_add) | **POST** /accounting/locations | Create Location |

_AccountingApi_ | [**locations_all**](docs/apis/AccountingApi.md#locations_all) | **GET** /accounting/locations | List Locations |

_AccountingApi_ | [**locations_delete**](docs/apis/AccountingApi.md#locations_delete) | **DELETE** /accounting/locations/{id} | Delete Location |

_AccountingApi_ | [**locations_one**](docs/apis/AccountingApi.md#locations_one) | **GET** /accounting/locations/{id} | Get Location |

_AccountingApi_ | [**locations_update**](docs/apis/AccountingApi.md#locations_update) | **PATCH** /accounting/locations/{id} | Update Location |

_AccountingApi_ | [**payments_add**](docs/apis/AccountingApi.md#payments_add) | **POST** /accounting/payments | Create Payment |

_AccountingApi_ | [**payments_all**](docs/apis/AccountingApi.md#payments_all) | **GET** /accounting/payments | List Payments |

_AccountingApi_ | [**payments_delete**](docs/apis/AccountingApi.md#payments_delete) | **DELETE** /accounting/payments/{id} | Delete Payment |

_AccountingApi_ | [**payments_one**](docs/apis/AccountingApi.md#payments_one) | **GET** /accounting/payments/{id} | Get Payment |

_AccountingApi_ | [**payments_update**](docs/apis/AccountingApi.md#payments_update) | **PATCH** /accounting/payments/{id} | Update Payment |

_AccountingApi_ | [**profit_and_loss_one**](docs/apis/AccountingApi.md#profit_and_loss_one) | **GET** /accounting/profit-and-loss | Get Profit and Loss |

_AccountingApi_ | [**purchase_orders_add**](docs/apis/AccountingApi.md#purchase_orders_add) | **POST** /accounting/purchase-orders | Create Purchase Order |

_AccountingApi_ | [**purchase_orders_all**](docs/apis/AccountingApi.md#purchase_orders_all) | **GET** /accounting/purchase-orders | List Purchase Orders |

_AccountingApi_ | [**purchase_orders_delete**](docs/apis/AccountingApi.md#purchase_orders_delete) | **DELETE** /accounting/purchase-orders/{id} | Delete Purchase Order |

_AccountingApi_ | [**purchase_orders_one**](docs/apis/AccountingApi.md#purchase_orders_one) | **GET** /accounting/purchase-orders/{id} | Get Purchase Order |

_AccountingApi_ | [**purchase_orders_update**](docs/apis/AccountingApi.md#purchase_orders_update) | **PATCH** /accounting/purchase-orders/{id} | Update Purchase Order |

_AccountingApi_ | [**subsidiaries_add**](docs/apis/AccountingApi.md#subsidiaries_add) | **POST** /accounting/subsidiaries | Create Subsidiary |

_AccountingApi_ | [**subsidiaries_all**](docs/apis/AccountingApi.md#subsidiaries_all) | **GET** /accounting/subsidiaries | List Subsidiaries |

_AccountingApi_ | [**subsidiaries_delete**](docs/apis/AccountingApi.md#subsidiaries_delete) | **DELETE** /accounting/subsidiaries/{id} | Delete Subsidiary |

_AccountingApi_ | [**subsidiaries_one**](docs/apis/AccountingApi.md#subsidiaries_one) | **GET** /accounting/subsidiaries/{id} | Get Subsidiary |

_AccountingApi_ | [**subsidiaries_update**](docs/apis/AccountingApi.md#subsidiaries_update) | **PATCH** /accounting/subsidiaries/{id} | Update Subsidiary |

_AccountingApi_ | [**suppliers_add**](docs/apis/AccountingApi.md#suppliers_add) | **POST** /accounting/suppliers | Create Supplier |

_AccountingApi_ | [**suppliers_all**](docs/apis/AccountingApi.md#suppliers_all) | **GET** /accounting/suppliers | List Suppliers |

_AccountingApi_ | [**suppliers_delete**](docs/apis/AccountingApi.md#suppliers_delete) | **DELETE** /accounting/suppliers/{id} | Delete Supplier |

_AccountingApi_ | [**suppliers_one**](docs/apis/AccountingApi.md#suppliers_one) | **GET** /accounting/suppliers/{id} | Get Supplier |

_AccountingApi_ | [**suppliers_update**](docs/apis/AccountingApi.md#suppliers_update) | **PATCH** /accounting/suppliers/{id} | Update Supplier |

_AccountingApi_ | [**tax_rates_add**](docs/apis/AccountingApi.md#tax_rates_add) | **POST** /accounting/tax-rates | Create Tax Rate |

_AccountingApi_ | [**tax_rates_all**](docs/apis/AccountingApi.md#tax_rates_all) | **GET** /accounting/tax-rates | List Tax Rates |

_AccountingApi_ | [**tax_rates_delete**](docs/apis/AccountingApi.md#tax_rates_delete) | **DELETE** /accounting/tax-rates/{id} | Delete Tax Rate |

_AccountingApi_ | [**tax_rates_one**](docs/apis/AccountingApi.md#tax_rates_one) | **GET** /accounting/tax-rates/{id} | Get Tax Rate |

_AccountingApi_ | [**tax_rates_update**](docs/apis/AccountingApi.md#tax_rates_update) | **PATCH** /accounting/tax-rates/{id} | Update Tax Rate |

_AccountingApi_ | [**tracking_categories_add**](docs/apis/AccountingApi.md#tracking_categories_add) | **POST** /accounting/tracking-categories | Create Tracking Category |

_AccountingApi_ | [**tracking_categories_all**](docs/apis/AccountingApi.md#tracking_categories_all) | **GET** /accounting/tracking-categories | List Tracking Categories |

_AccountingApi_ | [**tracking_categories_delete**](docs/apis/AccountingApi.md#tracking_categories_delete) | **DELETE** /accounting/tracking-categories/{id} | Delete Tracking Category |

_AccountingApi_ | [**tracking_categories_one**](docs/apis/AccountingApi.md#tracking_categories_one) | **GET** /accounting/tracking-categories/{id} | Get Tracking Category |

_AccountingApi_ | [**tracking_categories_update**](docs/apis/AccountingApi.md#tracking_categories_update) | **PATCH** /accounting/tracking-categories/{id} | Update Tracking Category |

_AtsApi_ | [**applicants_add**](docs/apis/AtsApi.md#applicants_add) | **POST** /ats/applicants | Create Applicant |

_AtsApi_ | [**applicants_all**](docs/apis/AtsApi.md#applicants_all) | **GET** /ats/applicants | List Applicants |

_AtsApi_ | [**applicants_delete**](docs/apis/AtsApi.md#applicants_delete) | **DELETE** /ats/applicants/{id} | Delete Applicant |

_AtsApi_ | [**applicants_one**](docs/apis/AtsApi.md#applicants_one) | **GET** /ats/applicants/{id} | Get Applicant |

_AtsApi_ | [**applicants_update**](docs/apis/AtsApi.md#applicants_update) | **PATCH** /ats/applicants/{id} | Update Applicant |

_AtsApi_ | [**applications_add**](docs/apis/AtsApi.md#applications_add) | **POST** /ats/applications | Create Application |

_AtsApi_ | [**applications_all**](docs/apis/AtsApi.md#applications_all) | **GET** /ats/applications | List Applications |

_AtsApi_ | [**applications_delete**](docs/apis/AtsApi.md#applications_delete) | **DELETE** /ats/applications/{id} | Delete Application |

_AtsApi_ | [**applications_one**](docs/apis/AtsApi.md#applications_one) | **GET** /ats/applications/{id} | Get Application |

_AtsApi_ | [**applications_update**](docs/apis/AtsApi.md#applications_update) | **PATCH** /ats/applications/{id} | Update Application |

_AtsApi_ | [**jobs_all**](docs/apis/AtsApi.md#jobs_all) | **GET** /ats/jobs | List Jobs |

_AtsApi_ | [**jobs_one**](docs/apis/AtsApi.md#jobs_one) | **GET** /ats/jobs/{id} | Get Job |

_ConnectorApi_ | [**api_resource_coverage_one**](docs/apis/ConnectorApi.md#api_resource_coverage_one) | **GET** /connector/apis/{id}/resources/{resource_id}/coverage | Get API Resource Coverage |

_ConnectorApi_ | [**api_resources_one**](docs/apis/ConnectorApi.md#api_resources_one) | **GET** /connector/apis/{id}/resources/{resource_id} | Get API Resource |

_ConnectorApi_ | [**apis_all**](docs/apis/ConnectorApi.md#apis_all) | **GET** /connector/apis | List APIs |

_ConnectorApi_ | [**apis_one**](docs/apis/ConnectorApi.md#apis_one) | **GET** /connector/apis/{id} | Get API |

_ConnectorApi_ | [**connector_docs_one**](docs/apis/ConnectorApi.md#connector_docs_one) | **GET** /connector/connectors/{id}/docs/{doc_id} | Get Connector Doc content |

_ConnectorApi_ | [**connector_resources_one**](docs/apis/ConnectorApi.md#connector_resources_one) | **GET** /connector/connectors/{id}/resources/{resource_id} | Get Connector Resource |

_ConnectorApi_ | [**connectors_all**](docs/apis/ConnectorApi.md#connectors_all) | **GET** /connector/connectors | List Connectors |

_ConnectorApi_ | [**connectors_one**](docs/apis/ConnectorApi.md#connectors_one) | **GET** /connector/connectors/{id} | Get Connector |

_CrmApi_ | [**activities_add**](docs/apis/CrmApi.md#activities_add) | **POST** /crm/activities | Create activity |

_CrmApi_ | [**activities_all**](docs/apis/CrmApi.md#activities_all) | **GET** /crm/activities | List activities |

_CrmApi_ | [**activities_delete**](docs/apis/CrmApi.md#activities_delete) | **DELETE** /crm/activities/{id} | Delete activity |

_CrmApi_ | [**activities_one**](docs/apis/CrmApi.md#activities_one) | **GET** /crm/activities/{id} | Get activity |

_CrmApi_ | [**activities_update**](docs/apis/CrmApi.md#activities_update) | **PATCH** /crm/activities/{id} | Update activity |

_CrmApi_ | [**companies_add**](docs/apis/CrmApi.md#companies_add) | **POST** /crm/companies | Create company |

_CrmApi_ | [**companies_all**](docs/apis/CrmApi.md#companies_all) | **GET** /crm/companies | List companies |

_CrmApi_ | [**companies_delete**](docs/apis/CrmApi.md#companies_delete) | **DELETE** /crm/companies/{id} | Delete company |

_CrmApi_ | [**companies_one**](docs/apis/CrmApi.md#companies_one) | **GET** /crm/companies/{id} | Get company |

_CrmApi_ | [**companies_update**](docs/apis/CrmApi.md#companies_update) | **PATCH** /crm/companies/{id} | Update company |

_CrmApi_ | [**contacts_add**](docs/apis/CrmApi.md#contacts_add) | **POST** /crm/contacts | Create contact |

_CrmApi_ | [**contacts_all**](docs/apis/CrmApi.md#contacts_all) | **GET** /crm/contacts | List contacts |

_CrmApi_ | [**contacts_delete**](docs/apis/CrmApi.md#contacts_delete) | **DELETE** /crm/contacts/{id} | Delete contact |

_CrmApi_ | [**contacts_one**](docs/apis/CrmApi.md#contacts_one) | **GET** /crm/contacts/{id} | Get contact |

_CrmApi_ | [**contacts_update**](docs/apis/CrmApi.md#contacts_update) | **PATCH** /crm/contacts/{id} | Update contact |

_CrmApi_ | [**custom_object_schemas_add**](docs/apis/CrmApi.md#custom_object_schemas_add) | **POST** /crm/custom-object-schemas | Create custom object schema |

_CrmApi_ | [**custom_object_schemas_all**](docs/apis/CrmApi.md#custom_object_schemas_all) | **GET** /crm/custom-object-schemas | List custom object schemas |

_CrmApi_ | [**custom_object_schemas_delete**](docs/apis/CrmApi.md#custom_object_schemas_delete) | **DELETE** /crm/custom-object-schemas/{id} | Delete custom object schema |

_CrmApi_ | [**custom_object_schemas_one**](docs/apis/CrmApi.md#custom_object_schemas_one) | **GET** /crm/custom-object-schemas/{id} | Get custom object schema |

_CrmApi_ | [**custom_object_schemas_update**](docs/apis/CrmApi.md#custom_object_schemas_update) | **PATCH** /crm/custom-object-schemas/{id} | Update custom object schema |

_CrmApi_ | [**custom_objects_add**](docs/apis/CrmApi.md#custom_objects_add) | **POST** /crm/custom-objects/{object_id} | Create custom object |

_CrmApi_ | [**custom_objects_all**](docs/apis/CrmApi.md#custom_objects_all) | **GET** /crm/custom-objects/{object_id} | List custom objects |

_CrmApi_ | [**custom_objects_delete**](docs/apis/CrmApi.md#custom_objects_delete) | **DELETE** /crm/custom-objects/{object_id}/{id} | Delete custom object |

_CrmApi_ | [**custom_objects_one**](docs/apis/CrmApi.md#custom_objects_one) | **GET** /crm/custom-objects/{object_id}/{id} | Get custom object |

_CrmApi_ | [**custom_objects_update**](docs/apis/CrmApi.md#custom_objects_update) | **PATCH** /crm/custom-objects/{object_id}/{id} | Update custom object |

_CrmApi_ | [**leads_add**](docs/apis/CrmApi.md#leads_add) | **POST** /crm/leads | Create lead |

_CrmApi_ | [**leads_all**](docs/apis/CrmApi.md#leads_all) | **GET** /crm/leads | List leads |

_CrmApi_ | [**leads_delete**](docs/apis/CrmApi.md#leads_delete) | **DELETE** /crm/leads/{id} | Delete lead |

_CrmApi_ | [**leads_one**](docs/apis/CrmApi.md#leads_one) | **GET** /crm/leads/{id} | Get lead |

_CrmApi_ | [**leads_update**](docs/apis/CrmApi.md#leads_update) | **PATCH** /crm/leads/{id} | Update lead |

_CrmApi_ | [**notes_add**](docs/apis/CrmApi.md#notes_add) | **POST** /crm/notes | Create note |

_CrmApi_ | [**notes_all**](docs/apis/CrmApi.md#notes_all) | **GET** /crm/notes | List notes |

_CrmApi_ | [**notes_delete**](docs/apis/CrmApi.md#notes_delete) | **DELETE** /crm/notes/{id} | Delete note |

_CrmApi_ | [**notes_one**](docs/apis/CrmApi.md#notes_one) | **GET** /crm/notes/{id} | Get note |

_CrmApi_ | [**notes_update**](docs/apis/CrmApi.md#notes_update) | **PATCH** /crm/notes/{id} | Update note |

_CrmApi_ | [**opportunities_add**](docs/apis/CrmApi.md#opportunities_add) | **POST** /crm/opportunities | Create opportunity |

_CrmApi_ | [**opportunities_all**](docs/apis/CrmApi.md#opportunities_all) | **GET** /crm/opportunities | List opportunities |

_CrmApi_ | [**opportunities_delete**](docs/apis/CrmApi.md#opportunities_delete) | **DELETE** /crm/opportunities/{id} | Delete opportunity |

_CrmApi_ | [**opportunities_one**](docs/apis/CrmApi.md#opportunities_one) | **GET** /crm/opportunities/{id} | Get opportunity |

_CrmApi_ | [**opportunities_update**](docs/apis/CrmApi.md#opportunities_update) | **PATCH** /crm/opportunities/{id} | Update opportunity |

_CrmApi_ | [**pipelines_add**](docs/apis/CrmApi.md#pipelines_add) | **POST** /crm/pipelines | Create pipeline |

_CrmApi_ | [**pipelines_all**](docs/apis/CrmApi.md#pipelines_all) | **GET** /crm/pipelines | List pipelines |

_CrmApi_ | [**pipelines_delete**](docs/apis/CrmApi.md#pipelines_delete) | **DELETE** /crm/pipelines/{id} | Delete pipeline |

_CrmApi_ | [**pipelines_one**](docs/apis/CrmApi.md#pipelines_one) | **GET** /crm/pipelines/{id} | Get pipeline |

_CrmApi_ | [**pipelines_update**](docs/apis/CrmApi.md#pipelines_update) | **PATCH** /crm/pipelines/{id} | Update pipeline |

_CrmApi_ | [**users_add**](docs/apis/CrmApi.md#users_add) | **POST** /crm/users | Create user |

_CrmApi_ | [**users_all**](docs/apis/CrmApi.md#users_all) | **GET** /crm/users | List users |

_CrmApi_ | [**users_delete**](docs/apis/CrmApi.md#users_delete) | **DELETE** /crm/users/{id} | Delete user |

_CrmApi_ | [**users_one**](docs/apis/CrmApi.md#users_one) | **GET** /crm/users/{id} | Get user |

_CrmApi_ | [**users_update**](docs/apis/CrmApi.md#users_update) | **PATCH** /crm/users/{id} | Update user |

_EcommerceApi_ | [**customers_all**](docs/apis/EcommerceApi.md#customers_all) | **GET** /ecommerce/customers | List Customers |

_EcommerceApi_ | [**customers_one**](docs/apis/EcommerceApi.md#customers_one) | **GET** /ecommerce/customers/{id} | Get Customer |

_EcommerceApi_ | [**orders_all**](docs/apis/EcommerceApi.md#orders_all) | **GET** /ecommerce/orders | List Orders |

_EcommerceApi_ | [**orders_one**](docs/apis/EcommerceApi.md#orders_one) | **GET** /ecommerce/orders/{id} | Get Order |

_EcommerceApi_ | [**products_all**](docs/apis/EcommerceApi.md#products_all) | **GET** /ecommerce/products | List Products |

_EcommerceApi_ | [**products_one**](docs/apis/EcommerceApi.md#products_one) | **GET** /ecommerce/products/{id} | Get Product |

_EcommerceApi_ | [**stores_one**](docs/apis/EcommerceApi.md#stores_one) | **GET** /ecommerce/store | Get Store |

_FileStorageApi_ | [**drive_groups_add**](docs/apis/FileStorageApi.md#drive_groups_add) | **POST** /file-storage/drive-groups | Create DriveGroup |

_FileStorageApi_ | [**drive_groups_all**](docs/apis/FileStorageApi.md#drive_groups_all) | **GET** /file-storage/drive-groups | List DriveGroups |

_FileStorageApi_ | [**drive_groups_delete**](docs/apis/FileStorageApi.md#drive_groups_delete) | **DELETE** /file-storage/drive-groups/{id} | Delete DriveGroup |

_FileStorageApi_ | [**drive_groups_one**](docs/apis/FileStorageApi.md#drive_groups_one) | **GET** /file-storage/drive-groups/{id} | Get DriveGroup |

_FileStorageApi_ | [**drive_groups_update**](docs/apis/FileStorageApi.md#drive_groups_update) | **PATCH** /file-storage/drive-groups/{id} | Update DriveGroup |

_FileStorageApi_ | [**drives_add**](docs/apis/FileStorageApi.md#drives_add) | **POST** /file-storage/drives | Create Drive |

_FileStorageApi_ | [**drives_all**](docs/apis/FileStorageApi.md#drives_all) | **GET** /file-storage/drives | List Drives |

_FileStorageApi_ | [**drives_delete**](docs/apis/FileStorageApi.md#drives_delete) | **DELETE** /file-storage/drives/{id} | Delete Drive |

_FileStorageApi_ | [**drives_one**](docs/apis/FileStorageApi.md#drives_one) | **GET** /file-storage/drives/{id} | Get Drive |

_FileStorageApi_ | [**drives_update**](docs/apis/FileStorageApi.md#drives_update) | **PATCH** /file-storage/drives/{id} | Update Drive |

_FileStorageApi_ | [**files_all**](docs/apis/FileStorageApi.md#files_all) | **GET** /file-storage/files | List Files |

_FileStorageApi_ | [**files_delete**](docs/apis/FileStorageApi.md#files_delete) | **DELETE** /file-storage/files/{id} | Delete File |

_FileStorageApi_ | [**files_download**](docs/apis/FileStorageApi.md#files_download) | **GET** /file-storage/files/{id}/download | Download File |

_FileStorageApi_ | [**files_export**](docs/apis/FileStorageApi.md#files_export) | **GET** /file-storage/files/{id}/export | Export File |

_FileStorageApi_ | [**files_one**](docs/apis/FileStorageApi.md#files_one) | **GET** /file-storage/files/{id} | Get File |

_FileStorageApi_ | [**files_search**](docs/apis/FileStorageApi.md#files_search) | **POST** /file-storage/files/search | Search Files |

_FileStorageApi_ | [**files_update**](docs/apis/FileStorageApi.md#files_update) | **PATCH** /file-storage/files/{id} | Rename or move File |

_FileStorageApi_ | [**folders_add**](docs/apis/FileStorageApi.md#folders_add) | **POST** /file-storage/folders | Create Folder |

_FileStorageApi_ | [**folders_copy**](docs/apis/FileStorageApi.md#folders_copy) | **POST** /file-storage/folders/{id}/copy | Copy Folder |

_FileStorageApi_ | [**folders_delete**](docs/apis/FileStorageApi.md#folders_delete) | **DELETE** /file-storage/folders/{id} | Delete Folder |

_FileStorageApi_ | [**folders_one**](docs/apis/FileStorageApi.md#folders_one) | **GET** /file-storage/folders/{id} | Get Folder |

_FileStorageApi_ | [**folders_update**](docs/apis/FileStorageApi.md#folders_update) | **PATCH** /file-storage/folders/{id} | Rename or move Folder |

_FileStorageApi_ | [**shared_links_add**](docs/apis/FileStorageApi.md#shared_links_add) | **POST** /file-storage/shared-links | Create Shared Link |

_FileStorageApi_ | [**shared_links_all**](docs/apis/FileStorageApi.md#shared_links_all) | **GET** /file-storage/shared-links | List SharedLinks |

_FileStorageApi_ | [**shared_links_delete**](docs/apis/FileStorageApi.md#shared_links_delete) | **DELETE** /file-storage/shared-links/{id} | Delete Shared Link |

_FileStorageApi_ | [**shared_links_one**](docs/apis/FileStorageApi.md#shared_links_one) | **GET** /file-storage/shared-links/{id} | Get Shared Link |

_FileStorageApi_ | [**shared_links_update**](docs/apis/FileStorageApi.md#shared_links_update) | **PATCH** /file-storage/shared-links/{id} | Update Shared Link |

_FileStorageApi_ | [**upload_sessions_add**](docs/apis/FileStorageApi.md#upload_sessions_add) | **POST** /file-storage/upload-sessions | Start Upload Session |

_FileStorageApi_ | [**upload_sessions_delete**](docs/apis/FileStorageApi.md#upload_sessions_delete) | **DELETE** /file-storage/upload-sessions/{id} | Abort Upload Session |

_FileStorageApi_ | [**upload_sessions_finish**](docs/apis/FileStorageApi.md#upload_sessions_finish) | **POST** /file-storage/upload-sessions/{id}/finish | Finish Upload Session |

_FileStorageApi_ | [**upload_sessions_one**](docs/apis/FileStorageApi.md#upload_sessions_one) | **GET** /file-storage/upload-sessions/{id} | Get Upload Session |

_HrisApi_ | [**companies_add**](docs/apis/HrisApi.md#companies_add) | **POST** /hris/companies | Create Company |

_HrisApi_ | [**companies_all**](docs/apis/HrisApi.md#companies_all) | **GET** /hris/companies | List Companies |

_HrisApi_ | [**companies_delete**](docs/apis/HrisApi.md#companies_delete) | **DELETE** /hris/companies/{id} | Delete Company |

_HrisApi_ | [**companies_one**](docs/apis/HrisApi.md#companies_one) | **GET** /hris/companies/{id} | Get Company |

_HrisApi_ | [**companies_update**](docs/apis/HrisApi.md#companies_update) | **PATCH** /hris/companies/{id} | Update Company |

_HrisApi_ | [**departments_add**](docs/apis/HrisApi.md#departments_add) | **POST** /hris/departments | Create Department |

_HrisApi_ | [**departments_all**](docs/apis/HrisApi.md#departments_all) | **GET** /hris/departments | List Departments |

_HrisApi_ | [**departments_delete**](docs/apis/HrisApi.md#departments_delete) | **DELETE** /hris/departments/{id} | Delete Department |

_HrisApi_ | [**departments_one**](docs/apis/HrisApi.md#departments_one) | **GET** /hris/departments/{id} | Get Department |

_HrisApi_ | [**departments_update**](docs/apis/HrisApi.md#departments_update) | **PATCH** /hris/departments/{id} | Update Department |

_HrisApi_ | [**employee_payrolls_all**](docs/apis/HrisApi.md#employee_payrolls_all) | **GET** /hris/payrolls/employees/{employee_id} | List Employee Payrolls |

_HrisApi_ | [**employee_payrolls_one**](docs/apis/HrisApi.md#employee_payrolls_one) | **GET** /hris/payrolls/employees/{employee_id}/payrolls/{payroll_id} | Get Employee Payroll |

_HrisApi_ | [**employee_schedules_all**](docs/apis/HrisApi.md#employee_schedules_all) | **GET** /hris/schedules/employees/{employee_id} | List Employee Schedules |

_HrisApi_ | [**employees_add**](docs/apis/HrisApi.md#employees_add) | **POST** /hris/employees | Create Employee |

_HrisApi_ | [**employees_all**](docs/apis/HrisApi.md#employees_all) | **GET** /hris/employees | List Employees |

_HrisApi_ | [**employees_delete**](docs/apis/HrisApi.md#employees_delete) | **DELETE** /hris/employees/{id} | Delete Employee |

_HrisApi_ | [**employees_one**](docs/apis/HrisApi.md#employees_one) | **GET** /hris/employees/{id} | Get Employee |

_HrisApi_ | [**employees_update**](docs/apis/HrisApi.md#employees_update) | **PATCH** /hris/employees/{id} | Update Employee |

_HrisApi_ | [**payrolls_all**](docs/apis/HrisApi.md#payrolls_all) | **GET** /hris/payrolls | List Payroll |

_HrisApi_ | [**payrolls_one**](docs/apis/HrisApi.md#payrolls_one) | **GET** /hris/payrolls/{payroll_id} | Get Payroll |

_HrisApi_ | [**time_off_requests_add**](docs/apis/HrisApi.md#time_off_requests_add) | **POST** /hris/time-off-requests | Create Time Off Request |

_HrisApi_ | [**time_off_requests_all**](docs/apis/HrisApi.md#time_off_requests_all) | **GET** /hris/time-off-requests | List Time Off Requests |

_HrisApi_ | [**time_off_requests_delete**](docs/apis/HrisApi.md#time_off_requests_delete) | **DELETE** /hris/time-off-requests/employees/{employee_id}/time-off-requests/{id} | Delete Time Off Request |

_HrisApi_ | [**time_off_requests_one**](docs/apis/HrisApi.md#time_off_requests_one) | **GET** /hris/time-off-requests/employees/{employee_id}/time-off-requests/{id} | Get Time Off Request |

_HrisApi_ | [**time_off_requests_update**](docs/apis/HrisApi.md#time_off_requests_update) | **PATCH** /hris/time-off-requests/employees/{employee_id}/time-off-requests/{id} | Update Time Off Request |

_IssueTrackingApi_ | [**collection_tags_all**](docs/apis/IssueTrackingApi.md#collection_tags_all) | **GET** /issue-tracking/collections/{collection_id}/tags | List Tags |

_IssueTrackingApi_ | [**collection_ticket_comments_add**](docs/apis/IssueTrackingApi.md#collection_ticket_comments_add) | **POST** /issue-tracking/collections/{collection_id}/tickets/{ticket_id}/comments | Create Comment |

_IssueTrackingApi_ | [**collection_ticket_comments_all**](docs/apis/IssueTrackingApi.md#collection_ticket_comments_all) | **GET** /issue-tracking/collections/{collection_id}/tickets/{ticket_id}/comments | List Comments |

_IssueTrackingApi_ | [**collection_ticket_comments_delete**](docs/apis/IssueTrackingApi.md#collection_ticket_comments_delete) | **DELETE** /issue-tracking/collections/{collection_id}/tickets/{ticket_id}/comments/{id} | Delete Comment |

_IssueTrackingApi_ | [**collection_ticket_comments_one**](docs/apis/IssueTrackingApi.md#collection_ticket_comments_one) | **GET** /issue-tracking/collections/{collection_id}/tickets/{ticket_id}/comments/{id} | Get Comment |

_IssueTrackingApi_ | [**collection_ticket_comments_update**](docs/apis/IssueTrackingApi.md#collection_ticket_comments_update) | **PATCH** /issue-tracking/collections/{collection_id}/tickets/{ticket_id}/comments/{id} | Update Comment |

_IssueTrackingApi_ | [**collection_tickets_add**](docs/apis/IssueTrackingApi.md#collection_tickets_add) | **POST** /issue-tracking/collections/{collection_id}/tickets | Create Ticket |

_IssueTrackingApi_ | [**collection_tickets_all**](docs/apis/IssueTrackingApi.md#collection_tickets_all) | **GET** /issue-tracking/collections/{collection_id}/tickets | List Tickets |

_IssueTrackingApi_ | [**collection_tickets_delete**](docs/apis/IssueTrackingApi.md#collection_tickets_delete) | **DELETE** /issue-tracking/collections/{collection_id}/tickets/{ticket_id} | Delete Ticket |

_IssueTrackingApi_ | [**collection_tickets_one**](docs/apis/IssueTrackingApi.md#collection_tickets_one) | **GET** /issue-tracking/collections/{collection_id}/tickets/{ticket_id} | Get Ticket |

_IssueTrackingApi_ | [**collection_tickets_update**](docs/apis/IssueTrackingApi.md#collection_tickets_update) | **PATCH** /issue-tracking/collections/{collection_id}/tickets/{ticket_id} | Update Ticket |

_IssueTrackingApi_ | [**collection_users_all**](docs/apis/IssueTrackingApi.md#collection_users_all) | **GET** /issue-tracking/collections/{collection_id}/users | List Users |

_IssueTrackingApi_ | [**collection_users_one**](docs/apis/IssueTrackingApi.md#collection_users_one) | **GET** /issue-tracking/collections/{collection_id}/users/{id} | Get user |

_IssueTrackingApi_ | [**collections_all**](docs/apis/IssueTrackingApi.md#collections_all) | **GET** /issue-tracking/collections | List Collections |

_IssueTrackingApi_ | [**collections_one**](docs/apis/IssueTrackingApi.md#collections_one) | **GET** /issue-tracking/collections/{collection_id} | Get Collection |

_LeadApi_ | [**leads_add**](docs/apis/LeadApi.md#leads_add) | **POST** /lead/leads | Create lead |

_LeadApi_ | [**leads_all**](docs/apis/LeadApi.md#leads_all) | **GET** /lead/leads | List leads |

_LeadApi_ | [**leads_delete**](docs/apis/LeadApi.md#leads_delete) | **DELETE** /lead/leads/{id} | Delete lead |

_LeadApi_ | [**leads_one**](docs/apis/LeadApi.md#leads_one) | **GET** /lead/leads/{id} | Get lead |

_LeadApi_ | [**leads_update**](docs/apis/LeadApi.md#leads_update) | **PATCH** /lead/leads/{id} | Update lead |

_PosApi_ | [**items_add**](docs/apis/PosApi.md#items_add) | **POST** /pos/items | Create Item |

_PosApi_ | [**items_all**](docs/apis/PosApi.md#items_all) | **GET** /pos/items | List Items |

_PosApi_ | [**items_delete**](docs/apis/PosApi.md#items_delete) | **DELETE** /pos/items/{id} | Delete Item |

_PosApi_ | [**items_one**](docs/apis/PosApi.md#items_one) | **GET** /pos/items/{id} | Get Item |

_PosApi_ | [**items_update**](docs/apis/PosApi.md#items_update) | **PATCH** /pos/items/{id} | Update Item |

_PosApi_ | [**locations_add**](docs/apis/PosApi.md#locations_add) | **POST** /pos/locations | Create Location |

_PosApi_ | [**locations_all**](docs/apis/PosApi.md#locations_all) | **GET** /pos/locations | List Locations |

_PosApi_ | [**locations_delete**](docs/apis/PosApi.md#locations_delete) | **DELETE** /pos/locations/{id} | Delete Location |

_PosApi_ | [**locations_one**](docs/apis/PosApi.md#locations_one) | **GET** /pos/locations/{id} | Get Location |

_PosApi_ | [**locations_update**](docs/apis/PosApi.md#locations_update) | **PATCH** /pos/locations/{id} | Update Location |

_PosApi_ | [**merchants_add**](docs/apis/PosApi.md#merchants_add) | **POST** /pos/merchants | Create Merchant |

_PosApi_ | [**merchants_all**](docs/apis/PosApi.md#merchants_all) | **GET** /pos/merchants | List Merchants |

_PosApi_ | [**merchants_delete**](docs/apis/PosApi.md#merchants_delete) | **DELETE** /pos/merchants/{id} | Delete Merchant |

_PosApi_ | [**merchants_one**](docs/apis/PosApi.md#merchants_one) | **GET** /pos/merchants/{id} | Get Merchant |

_PosApi_ | [**merchants_update**](docs/apis/PosApi.md#merchants_update) | **PATCH** /pos/merchants/{id} | Update Merchant |

_PosApi_ | [**modifier_groups_add**](docs/apis/PosApi.md#modifier_groups_add) | **POST** /pos/modifier-groups | Create Modifier Group |

_PosApi_ | [**modifier_groups_all**](docs/apis/PosApi.md#modifier_groups_all) | **GET** /pos/modifier-groups | List Modifier Groups |

_PosApi_ | [**modifier_groups_delete**](docs/apis/PosApi.md#modifier_groups_delete) | **DELETE** /pos/modifier-groups/{id} | Delete Modifier Group |

_PosApi_ | [**modifier_groups_one**](docs/apis/PosApi.md#modifier_groups_one) | **GET** /pos/modifier-groups/{id} | Get Modifier Group |

_PosApi_ | [**modifier_groups_update**](docs/apis/PosApi.md#modifier_groups_update) | **PATCH** /pos/modifier-groups/{id} | Update Modifier Group |

_PosApi_ | [**modifiers_add**](docs/apis/PosApi.md#modifiers_add) | **POST** /pos/modifiers | Create Modifier |

_PosApi_ | [**modifiers_all**](docs/apis/PosApi.md#modifiers_all) | **GET** /pos/modifiers | List Modifiers |

_PosApi_ | [**modifiers_delete**](docs/apis/PosApi.md#modifiers_delete) | **DELETE** /pos/modifiers/{id} | Delete Modifier |

_PosApi_ | [**modifiers_one**](docs/apis/PosApi.md#modifiers_one) | **GET** /pos/modifiers/{id} | Get Modifier |

_PosApi_ | [**modifiers_update**](docs/apis/PosApi.md#modifiers_update) | **PATCH** /pos/modifiers/{id} | Update Modifier |

_PosApi_ | [**order_types_add**](docs/apis/PosApi.md#order_types_add) | **POST** /pos/order-types | Create Order Type |

_PosApi_ | [**order_types_all**](docs/apis/PosApi.md#order_types_all) | **GET** /pos/order-types | List Order Types |

_PosApi_ | [**order_types_delete**](docs/apis/PosApi.md#order_types_delete) | **DELETE** /pos/order-types/{id} | Delete Order Type |

_PosApi_ | [**order_types_one**](docs/apis/PosApi.md#order_types_one) | **GET** /pos/order-types/{id} | Get Order Type |

_PosApi_ | [**order_types_update**](docs/apis/PosApi.md#order_types_update) | **PATCH** /pos/order-types/{id} | Update Order Type |

_PosApi_ | [**orders_add**](docs/apis/PosApi.md#orders_add) | **POST** /pos/orders | Create Order |

_PosApi_ | [**orders_all**](docs/apis/PosApi.md#orders_all) | **GET** /pos/orders | List Orders |

_PosApi_ | [**orders_delete**](docs/apis/PosApi.md#orders_delete) | **DELETE** /pos/orders/{id} | Delete Order |

_PosApi_ | [**orders_one**](docs/apis/PosApi.md#orders_one) | **GET** /pos/orders/{id} | Get Order |

_PosApi_ | [**orders_pay**](docs/apis/PosApi.md#orders_pay) | **POST** /pos/orders/{id}/pay | Pay Order |

_PosApi_ | [**orders_update**](docs/apis/PosApi.md#orders_update) | **PATCH** /pos/orders/{id} | Update Order |

_PosApi_ | [**payments_add**](docs/apis/PosApi.md#payments_add) | **POST** /pos/payments | Create Payment |

_PosApi_ | [**payments_all**](docs/apis/PosApi.md#payments_all) | **GET** /pos/payments | List Payments |

_PosApi_ | [**payments_delete**](docs/apis/PosApi.md#payments_delete) | **DELETE** /pos/payments/{id} | Delete Payment |

_PosApi_ | [**payments_one**](docs/apis/PosApi.md#payments_one) | **GET** /pos/payments/{id} | Get Payment |

_PosApi_ | [**payments_update**](docs/apis/PosApi.md#payments_update) | **PATCH** /pos/payments/{id} | Update Payment |

_PosApi_ | [**tenders_add**](docs/apis/PosApi.md#tenders_add) | **POST** /pos/tenders | Create Tender |

_PosApi_ | [**tenders_all**](docs/apis/PosApi.md#tenders_all) | **GET** /pos/tenders | List Tenders |

_PosApi_ | [**tenders_delete**](docs/apis/PosApi.md#tenders_delete) | **DELETE** /pos/tenders/{id} | Delete Tender |

_PosApi_ | [**tenders_one**](docs/apis/PosApi.md#tenders_one) | **GET** /pos/tenders/{id} | Get Tender |

_PosApi_ | [**tenders_update**](docs/apis/PosApi.md#tenders_update) | **PATCH** /pos/tenders/{id} | Update Tender |

_SmsApi_ | [**messages_add**](docs/apis/SmsApi.md#messages_add) | **POST** /sms/messages | Create Message |

_SmsApi_ | [**messages_all**](docs/apis/SmsApi.md#messages_all) | **GET** /sms/messages | List Messages |

_SmsApi_ | [**messages_delete**](docs/apis/SmsApi.md#messages_delete) | **DELETE** /sms/messages/{id} | Delete Message |

_SmsApi_ | [**messages_one**](docs/apis/SmsApi.md#messages_one) | **GET** /sms/messages/{id} | Get Message |

_SmsApi_ | [**messages_update**](docs/apis/SmsApi.md#messages_update) | **PATCH** /sms/messages/{id} | Update Message |

_VaultApi_ | [**connection_custom_mappings_all**](docs/apis/VaultApi.md#connection_custom_mappings_all) | **GET** /vault/connections/{unified_api}/{service_id}/{resource}/custom-mappings | List connection custom mappings |

_VaultApi_ | [**connection_settings_all**](docs/apis/VaultApi.md#connection_settings_all) | **GET** /vault/connections/{unified_api}/{service_id}/{resource}/config | Get resource settings |

_VaultApi_ | [**connection_settings_update**](docs/apis/VaultApi.md#connection_settings_update) | **PATCH** /vault/connections/{unified_api}/{service_id}/{resource}/config | Update settings |

_VaultApi_ | [**connections_all**](docs/apis/VaultApi.md#connections_all) | **GET** /vault/connections | Get all connections |

_VaultApi_ | [**connections_delete**](docs/apis/VaultApi.md#connections_delete) | **DELETE** /vault/connections/{unified_api}/{service_id} | Deletes a connection |

_VaultApi_ | [**connections_import**](docs/apis/VaultApi.md#connections_import) | **POST** /vault/connections/{unified_api}/{service_id}/import | Import connection |

_VaultApi_ | [**connections_one**](docs/apis/VaultApi.md#connections_one) | **GET** /vault/connections/{unified_api}/{service_id} | Get connection |

_VaultApi_ | [**connections_token**](docs/apis/VaultApi.md#connections_token) | **POST** /vault/connections/{unified_api}/{service_id}/token | Authorize Access Token |

_VaultApi_ | [**connections_update**](docs/apis/VaultApi.md#connections_update) | **PATCH** /vault/connections/{unified_api}/{service_id} | Update connection |

_VaultApi_ | [**consumer_request_counts_all**](docs/apis/VaultApi.md#consumer_request_counts_all) | **GET** /vault/consumers/{consumer_id}/stats | Consumer request counts |

_VaultApi_ | [**consumers_add**](docs/apis/VaultApi.md#consumers_add) | **POST** /vault/consumers | Create consumer |

_VaultApi_ | [**consumers_all**](docs/apis/VaultApi.md#consumers_all) | **GET** /vault/consumers | Get all consumers |

_VaultApi_ | [**consumers_delete**](docs/apis/VaultApi.md#consumers_delete) | **DELETE** /vault/consumers/{consumer_id} | Delete consumer |

_VaultApi_ | [**consumers_one**](docs/apis/VaultApi.md#consumers_one) | **GET** /vault/consumers/{consumer_id} | Get consumer |

_VaultApi_ | [**consumers_update**](docs/apis/VaultApi.md#consumers_update) | **PATCH** /vault/consumers/{consumer_id} | Update consumer |

_VaultApi_ | [**create_callback_state**](docs/apis/VaultApi.md#create_callback_state) | **POST** /vault/connections/{unified_api}/{service_id}/callback-state | Create Callback State |

_VaultApi_ | [**custom_fields_all**](docs/apis/VaultApi.md#custom_fields_all) | **GET** /vault/connections/{unified_api}/{service_id}/{resource}/custom-fields | Get resource custom fields |

_VaultApi_ | [**custom_mappings_all**](docs/apis/VaultApi.md#custom_mappings_all) | **GET** /vault/custom-mappings/{unified_api}/{service_id} | List custom mappings |

_VaultApi_ | [**logs_all**](docs/apis/VaultApi.md#logs_all) | **GET** /vault/logs | Get all consumer request logs |

_VaultApi_ | [**sessions_create**](docs/apis/VaultApi.md#sessions_create) | **POST** /vault/sessions | Create Session |

_VaultApi_ | [**validate_connection_state**](docs/apis/VaultApi.md#validate_connection_state) | **POST** /vault/connections/{unified_api}/{service_id}/validate | Validate Connection State |

_WebhookApi_ | [**event_logs_all**](docs/apis/WebhookApi.md#event_logs_all) | **GET** /webhook/logs | List event logs |

_WebhookApi_ | [**webhooks_add**](docs/apis/WebhookApi.md#webhooks_add) | **POST** /webhook/webhooks | Create webhook subscription |

_WebhookApi_ | [**webhooks_all**](docs/apis/WebhookApi.md#webhooks_all) | **GET** /webhook/webhooks | List webhook subscriptions |

_WebhookApi_ | [**webhooks_delete**](docs/apis/WebhookApi.md#webhooks_delete) | **DELETE** /webhook/webhooks/{id} | Delete webhook subscription |

_WebhookApi_ | [**webhooks_one**](docs/apis/WebhookApi.md#webhooks_one) | **GET** /webhook/webhooks/{id} | Get webhook subscription |

_WebhookApi_ | [**webhooks_update**](docs/apis/WebhookApi.md#webhooks_update) | **PATCH** /webhook/webhooks/{id} | Update webhook subscription |



## Documentation For Models

 - [AccountingCustomer](docs/models/AccountingCustomer.md)
 - [AccountingDepartment](docs/models/AccountingDepartment.md)
 - [AccountingDepartmentsFilter](docs/models/AccountingDepartmentsFilter.md)
 - [AccountingEventType](docs/models/AccountingEventType.md)
 - [AccountingLocation](docs/models/AccountingLocation.md)
 - [AccountingLocationsFilter](docs/models/AccountingLocationsFilter.md)
 - [ActivitiesFilter](docs/models/ActivitiesFilter.md)
 - [ActivitiesSort](docs/models/ActivitiesSort.md)
 - [Activity](docs/models/Activity.md)
 - [ActivityAttendee](docs/models/ActivityAttendee.md)
 - [Address](docs/models/Address.md)
 - [AgedCreditors](docs/models/AgedCreditors.md)
 - [AgedDebtors](docs/models/AgedDebtors.md)
 - [AgedReportFilter](docs/models/AgedReportFilter.md)
 - [Allocation](docs/models/Allocation.md)
 - [Api](docs/models/Api.md)
 - [ApiResource](docs/models/ApiResource.md)
 - [ApiResourceCoverage](docs/models/ApiResourceCoverage.md)
 - [ApiResourceCoverageCoverage](docs/models/ApiResourceCoverageCoverage.md)
 - [ApiResourceLinkedResources](docs/models/ApiResourceLinkedResources.md)
 - [ApiResources](docs/models/ApiResources.md)
 - [ApiStatus](docs/models/ApiStatus.md)
 - [ApisFilter](docs/models/ApisFilter.md)
 - [Applicant](docs/models/Applicant.md)
 - [ApplicantSocialLinks](docs/models/ApplicantSocialLinks.md)
 - [ApplicantWebsites](docs/models/ApplicantWebsites.md)
 - [ApplicantsFilter](docs/models/ApplicantsFilter.md)
 - [Application](docs/models/Application.md)
 - [ApplicationStage](docs/models/ApplicationStage.md)
 - [Assignee](docs/models/Assignee.md)
 - [AtsActivity](docs/models/AtsActivity.md)
 - [AtsEventType](docs/models/AtsEventType.md)
 - [Attachment](docs/models/Attachment.md)
 - [AttachmentReference](docs/models/AttachmentReference.md)
 - [AttachmentReferenceType](docs/models/AttachmentReferenceType.md)
 - [AuthType](docs/models/AuthType.md)
 - [BadRequestResponse](docs/models/BadRequestResponse.md)
 - [BalanceByPeriod](docs/models/BalanceByPeriod.md)
 - [BalanceByTransaction](docs/models/BalanceByTransaction.md)
 - [BalanceSheet](docs/models/BalanceSheet.md)
 - [BalanceSheetAccount](docs/models/BalanceSheetAccount.md)
 - [BalanceSheetAccountRecord](docs/models/BalanceSheetAccountRecord.md)
 - [BalanceSheetAccounts](docs/models/BalanceSheetAccounts.md)
 - [BalanceSheetAssetsAccount](docs/models/BalanceSheetAssetsAccount.md)
 - [BalanceSheetEquityAccount](docs/models/BalanceSheetEquityAccount.md)
 - [BalanceSheetFilter](docs/models/BalanceSheetFilter.md)
 - [BalanceSheetLiabilitiesAccount](docs/models/BalanceSheetLiabilitiesAccount.md)
 - [BalanceSheetReports](docs/models/BalanceSheetReports.md)
 - [BalanceSheetUncategorizedItemsAccount](docs/models/BalanceSheetUncategorizedItemsAccount.md)
 - [BankAccount](docs/models/BankAccount.md)
 - [BankFeedAccount](docs/models/BankFeedAccount.md)
 - [BankFeedStatement](docs/models/BankFeedStatement.md)
 - [BankFeedStatementTransactions](docs/models/BankFeedStatementTransactions.md)
 - [Benefit](docs/models/Benefit.md)
 - [Bill](docs/models/Bill.md)
 - [BillLineItem](docs/models/BillLineItem.md)
 - [BillPayment](docs/models/BillPayment.md)
 - [BillPaymentAllocations](docs/models/BillPaymentAllocations.md)
 - [BillsFilter](docs/models/BillsFilter.md)
 - [BillsSort](docs/models/BillsSort.md)
 - [Branch](docs/models/Branch.md)
 - [CashDetails](docs/models/CashDetails.md)
 - [Collection](docs/models/Collection.md)
 - [CollectionTag](docs/models/CollectionTag.md)
 - [CollectionTicketComment](docs/models/CollectionTicketComment.md)
 - [CollectionUser](docs/models/CollectionUser.md)
 - [CollectionsSort](docs/models/CollectionsSort.md)
 - [CommentsSort](docs/models/CommentsSort.md)
 - [CompaniesFilter](docs/models/CompaniesFilter.md)
 - [CompaniesSort](docs/models/CompaniesSort.md)
 - [Company](docs/models/Company.md)
 - [CompanyInfo](docs/models/CompanyInfo.md)
 - [CompanyRowType](docs/models/CompanyRowType.md)
 - [Compensation](docs/models/Compensation.md)
 - [Connection](docs/models/Connection.md)
 - [ConnectionConfiguration](docs/models/ConnectionConfiguration.md)
 - [ConnectionDefaults](docs/models/ConnectionDefaults.md)
 - [ConnectionImportData](docs/models/ConnectionImportData.md)
 - [ConnectionImportDataCredentials](docs/models/ConnectionImportDataCredentials.md)
 - [ConnectionMetadata](docs/models/ConnectionMetadata.md)
 - [ConnectionState](docs/models/ConnectionState.md)
 - [ConnectionWebhook](docs/models/ConnectionWebhook.md)
 - [Connector](docs/models/Connector.md)
 - [ConnectorDoc](docs/models/ConnectorDoc.md)
 - [ConnectorEvent](docs/models/ConnectorEvent.md)
 - [ConnectorOauthScopes](docs/models/ConnectorOauthScopes.md)
 - [ConnectorOauthScopes1](docs/models/ConnectorOauthScopes1.md)
 - [ConnectorResource](docs/models/ConnectorResource.md)
 - [ConnectorSetting](docs/models/ConnectorSetting.md)
 - [ConnectorStatus](docs/models/ConnectorStatus.md)
 - [ConnectorTlsSupport](docs/models/ConnectorTlsSupport.md)
 - [ConnectorUnifiedApis](docs/models/ConnectorUnifiedApis.md)
 - [ConnectorsFilter](docs/models/ConnectorsFilter.md)
 - [Consumer](docs/models/Consumer.md)
 - [ConsumerConnection](docs/models/ConsumerConnection.md)
 - [ConsumerMetadata](docs/models/ConsumerMetadata.md)
 - [ConsumerRequestCountsInDateRangeResponse](docs/models/ConsumerRequestCountsInDateRangeResponse.md)
 - [ConsumerRequestCountsInDateRangeResponseData](docs/models/ConsumerRequestCountsInDateRangeResponseData.md)
 - [Contact](docs/models/Contact.md)
 - [ContactsFilter](docs/models/ContactsFilter.md)
 - [ContactsSort](docs/models/ContactsSort.md)
 - [CopyFolderRequest](docs/models/CopyFolderRequest.md)
 - [CostOfGoodsSold](docs/models/CostOfGoodsSold.md)
 - [Country](docs/models/Country.md)
 - [CreateAccountingDepartmentResponse](docs/models/CreateAccountingDepartmentResponse.md)
 - [CreateAccountingLocationResponse](docs/models/CreateAccountingLocationResponse.md)
 - [CreateActivityResponse](docs/models/CreateActivityResponse.md)
 - [CreateApplicantResponse](docs/models/CreateApplicantResponse.md)
 - [CreateApplicationResponse](docs/models/CreateApplicationResponse.md)
 - [CreateAttachmentRequest](docs/models/CreateAttachmentRequest.md)
 - [CreateAttachmentResponse](docs/models/CreateAttachmentResponse.md)
 - [CreateBankFeedAccountResponse](docs/models/CreateBankFeedAccountResponse.md)
 - [CreateBankFeedStatementResponse](docs/models/CreateBankFeedStatementResponse.md)
 - [CreateBillPaymentResponse](docs/models/CreateBillPaymentResponse.md)
 - [CreateBillResponse](docs/models/CreateBillResponse.md)
 - [CreateCallbackState](docs/models/CreateCallbackState.md)
 - [CreateCallbackStateResponse](docs/models/CreateCallbackStateResponse.md)
 - [CreateCallbackStateResponseData](docs/models/CreateCallbackStateResponseData.md)
 - [CreateCommentResponse](docs/models/CreateCommentResponse.md)
 - [CreateCompanyResponse](docs/models/CreateCompanyResponse.md)
 - [CreateConnectionResponse](docs/models/CreateConnectionResponse.md)
 - [CreateConsumerResponse](docs/models/CreateConsumerResponse.md)
 - [CreateContactResponse](docs/models/CreateContactResponse.md)
 - [CreateCreditNoteResponse](docs/models/CreateCreditNoteResponse.md)
 - [CreateCustomMappingRequest](docs/models/CreateCustomMappingRequest.md)
 - [CreateCustomMappingResponse](docs/models/CreateCustomMappingResponse.md)
 - [CreateCustomObjectResponse](docs/models/CreateCustomObjectResponse.md)
 - [CreateCustomObjectSchemaResponse](docs/models/CreateCustomObjectSchemaResponse.md)
 - [CreateCustomerResponse](docs/models/CreateCustomerResponse.md)
 - [CreateDepartmentResponse](docs/models/CreateDepartmentResponse.md)
 - [CreateDriveGroupResponse](docs/models/CreateDriveGroupResponse.md)
 - [CreateDriveResponse](docs/models/CreateDriveResponse.md)
 - [CreateEcommerceCustomerResponse](docs/models/CreateEcommerceCustomerResponse.md)
 - [CreateEcommerceOrderResponse](docs/models/CreateEcommerceOrderResponse.md)
 - [CreateEmployeeResponse](docs/models/CreateEmployeeResponse.md)
 - [CreateExpenseResponse](docs/models/CreateExpenseResponse.md)
 - [CreateFileRequest](docs/models/CreateFileRequest.md)
 - [CreateFileResponse](docs/models/CreateFileResponse.md)
 - [CreateFolderRequest](docs/models/CreateFolderRequest.md)
 - [CreateFolderResponse](docs/models/CreateFolderResponse.md)
 - [CreateHrisCompanyResponse](docs/models/CreateHrisCompanyResponse.md)
 - [CreateInvoiceItemResponse](docs/models/CreateInvoiceItemResponse.md)
 - [CreateInvoiceResponse](docs/models/CreateInvoiceResponse.md)
 - [CreateItemResponse](docs/models/CreateItemResponse.md)
 - [CreateJobResponse](docs/models/CreateJobResponse.md)
 - [CreateJournalEntryResponse](docs/models/CreateJournalEntryResponse.md)
 - [CreateLeadResponse](docs/models/CreateLeadResponse.md)
 - [CreateLedgerAccountResponse](docs/models/CreateLedgerAccountResponse.md)
 - [CreateLocationResponse](docs/models/CreateLocationResponse.md)
 - [CreateMerchantResponse](docs/models/CreateMerchantResponse.md)
 - [CreateMessageResponse](docs/models/CreateMessageResponse.md)
 - [CreateModifierGroupResponse](docs/models/CreateModifierGroupResponse.md)
 - [CreateModifierResponse](docs/models/CreateModifierResponse.md)
 - [CreateNoteResponse](docs/models/CreateNoteResponse.md)
 - [CreateOpportunityResponse](docs/models/CreateOpportunityResponse.md)
 - [CreateOrderResponse](docs/models/CreateOrderResponse.md)
 - [CreateOrderTypeResponse](docs/models/CreateOrderTypeResponse.md)
 - [CreatePaymentResponse](docs/models/CreatePaymentResponse.md)
 - [CreatePipelineResponse](docs/models/CreatePipelineResponse.md)
 - [CreatePosPaymentResponse](docs/models/CreatePosPaymentResponse.md)
 - [CreateProductResponse](docs/models/CreateProductResponse.md)
 - [CreatePurchaseOrderResponse](docs/models/CreatePurchaseOrderResponse.md)
 - [CreateSessionResponse](docs/models/CreateSessionResponse.md)
 - [CreateSessionResponseData](docs/models/CreateSessionResponseData.md)
 - [CreateSharedLinkResponse](docs/models/CreateSharedLinkResponse.md)
 - [CreateSubsidiaryResponse](docs/models/CreateSubsidiaryResponse.md)
 - [CreateSupplierResponse](docs/models/CreateSupplierResponse.md)
 - [CreateTaxRateResponse](docs/models/CreateTaxRateResponse.md)
 - [CreateTenderResponse](docs/models/CreateTenderResponse.md)
 - [CreateTicketResponse](docs/models/CreateTicketResponse.md)
 - [CreateTimeOffRequestResponse](docs/models/CreateTimeOffRequestResponse.md)
 - [CreateTrackingCategoryResponse](docs/models/CreateTrackingCategoryResponse.md)
 - [CreateUploadSessionRequest](docs/models/CreateUploadSessionRequest.md)
 - [CreateUploadSessionResponse](docs/models/CreateUploadSessionResponse.md)
 - [CreateUserResponse](docs/models/CreateUserResponse.md)
 - [CreateWebhookRequest](docs/models/CreateWebhookRequest.md)
 - [CreateWebhookResponse](docs/models/CreateWebhookResponse.md)
 - [CreditNote](docs/models/CreditNote.md)
 - [CreditNotesFilter](docs/models/CreditNotesFilter.md)
 - [CreditNotesSort](docs/models/CreditNotesSort.md)
 - [CreditOrDebit](docs/models/CreditOrDebit.md)
 - [CrmEventType](docs/models/CrmEventType.md)
 - [Currency](docs/models/Currency.md)
 - [CustomField](docs/models/CustomField.md)
 - [CustomFieldFinder](docs/models/CustomFieldFinder.md)
 - [CustomMapping](docs/models/CustomMapping.md)
 - [CustomMappings](docs/models/CustomMappings.md)
 - [CustomObject](docs/models/CustomObject.md)
 - [CustomObjectFields](docs/models/CustomObjectFields.md)
 - [CustomObjectSchema](docs/models/CustomObjectSchema.md)
 - [CustomObjectSchemaFields](docs/models/CustomObjectSchemaFields.md)
 - [CustomObjectSchemaOptions](docs/models/CustomObjectSchemaOptions.md)
 - [CustomObjectSchemasSort](docs/models/CustomObjectSchemasSort.md)
 - [CustomObjectsSort](docs/models/CustomObjectsSort.md)
 - [Customer](docs/models/Customer.md)
 - [CustomersFilter](docs/models/CustomersFilter.md)
 - [CustomersSort](docs/models/CustomersSort.md)
 - [Deduction](docs/models/Deduction.md)
 - [DeleteAccountingDepartmentResponse](docs/models/DeleteAccountingDepartmentResponse.md)
 - [DeleteAccountingLocationResponse](docs/models/DeleteAccountingLocationResponse.md)
 - [DeleteActivityResponse](docs/models/DeleteActivityResponse.md)
 - [DeleteApplicantResponse](docs/models/DeleteApplicantResponse.md)
 - [DeleteApplicationResponse](docs/models/DeleteApplicationResponse.md)
 - [DeleteAttachmentResponse](docs/models/DeleteAttachmentResponse.md)
 - [DeleteBankFeedAccountResponse](docs/models/DeleteBankFeedAccountResponse.md)
 - [DeleteBankFeedStatementResponse](docs/models/DeleteBankFeedStatementResponse.md)
 - [DeleteBillPaymentResponse](docs/models/DeleteBillPaymentResponse.md)
 - [DeleteBillResponse](docs/models/DeleteBillResponse.md)
 - [DeleteCommentResponse](docs/models/DeleteCommentResponse.md)
 - [DeleteCompanyResponse](docs/models/DeleteCompanyResponse.md)
 - [DeleteConsumerResponse](docs/models/DeleteConsumerResponse.md)
 - [DeleteContactResponse](docs/models/DeleteContactResponse.md)
 - [DeleteCreditNoteResponse](docs/models/DeleteCreditNoteResponse.md)
 - [DeleteCustomObjectResponse](docs/models/DeleteCustomObjectResponse.md)
 - [DeleteCustomObjectSchemaResponse](docs/models/DeleteCustomObjectSchemaResponse.md)
 - [DeleteCustomerResponse](docs/models/DeleteCustomerResponse.md)
 - [DeleteDepartmentResponse](docs/models/DeleteDepartmentResponse.md)
 - [DeleteDriveGroupResponse](docs/models/DeleteDriveGroupResponse.md)
 - [DeleteDriveResponse](docs/models/DeleteDriveResponse.md)
 - [DeleteEcommerceCustomerResponse](docs/models/DeleteEcommerceCustomerResponse.md)
 - [DeleteEcommerceOrderResponse](docs/models/DeleteEcommerceOrderResponse.md)
 - [DeleteEmployeeResponse](docs/models/DeleteEmployeeResponse.md)
 - [DeleteExpenseResponse](docs/models/DeleteExpenseResponse.md)
 - [DeleteFileResponse](docs/models/DeleteFileResponse.md)
 - [DeleteFolderResponse](docs/models/DeleteFolderResponse.md)
 - [DeleteHrisCompanyResponse](docs/models/DeleteHrisCompanyResponse.md)
 - [DeleteInvoiceItemResponse](docs/models/DeleteInvoiceItemResponse.md)
 - [DeleteInvoiceResponse](docs/models/DeleteInvoiceResponse.md)
 - [DeleteItemResponse](docs/models/DeleteItemResponse.md)
 - [DeleteJobResponse](docs/models/DeleteJobResponse.md)
 - [DeleteJournalEntryResponse](docs/models/DeleteJournalEntryResponse.md)
 - [DeleteLeadResponse](docs/models/DeleteLeadResponse.md)
 - [DeleteLedgerAccountResponse](docs/models/DeleteLedgerAccountResponse.md)
 - [DeleteLocationResponse](docs/models/DeleteLocationResponse.md)
 - [DeleteMerchantResponse](docs/models/DeleteMerchantResponse.md)
 - [DeleteMessageResponse](docs/models/DeleteMessageResponse.md)
 - [DeleteModifierGroupResponse](docs/models/DeleteModifierGroupResponse.md)
 - [DeleteModifierResponse](docs/models/DeleteModifierResponse.md)
 - [DeleteNoteResponse](docs/models/DeleteNoteResponse.md)
 - [DeleteOpportunityResponse](docs/models/DeleteOpportunityResponse.md)
 - [DeleteOrderResponse](docs/models/DeleteOrderResponse.md)
 - [DeleteOrderTypeResponse](docs/models/DeleteOrderTypeResponse.md)
 - [DeletePaymentResponse](docs/models/DeletePaymentResponse.md)
 - [DeletePipelineResponse](docs/models/DeletePipelineResponse.md)
 - [DeletePosPaymentResponse](docs/models/DeletePosPaymentResponse.md)
 - [DeleteProductResponse](docs/models/DeleteProductResponse.md)
 - [DeletePurchaseOrderResponse](docs/models/DeletePurchaseOrderResponse.md)
 - [DeleteSharedLinkResponse](docs/models/DeleteSharedLinkResponse.md)
 - [DeleteSubsidiaryResponse](docs/models/DeleteSubsidiaryResponse.md)
 - [DeleteSupplierResponse](docs/models/DeleteSupplierResponse.md)
 - [DeleteTaxRateResponse](docs/models/DeleteTaxRateResponse.md)
 - [DeleteTenderResponse](docs/models/DeleteTenderResponse.md)
 - [DeleteTicketResponse](docs/models/DeleteTicketResponse.md)
 - [DeleteTimeOffRequestResponse](docs/models/DeleteTimeOffRequestResponse.md)
 - [DeleteTrackingCategoryResponse](docs/models/DeleteTrackingCategoryResponse.md)
 - [DeleteUploadSessionResponse](docs/models/DeleteUploadSessionResponse.md)
 - [DeleteUserResponse](docs/models/DeleteUserResponse.md)
 - [DeleteWebhookResponse](docs/models/DeleteWebhookResponse.md)
 - [DeliveryUrl](docs/models/DeliveryUrl.md)
 - [Department](docs/models/Department.md)
 - [DeprecatedLinkedSupplier](docs/models/DeprecatedLinkedSupplier.md)
 - [DeprecatedLinkedTrackingCategory](docs/models/DeprecatedLinkedTrackingCategory.md)
 - [Drive](docs/models/Drive.md)
 - [DriveGroup](docs/models/DriveGroup.md)
 - [DriveGroupsFilter](docs/models/DriveGroupsFilter.md)
 - [DrivesFilter](docs/models/DrivesFilter.md)
 - [EcommerceAddress](docs/models/EcommerceAddress.md)
 - [EcommerceCustomer](docs/models/EcommerceCustomer.md)
 - [EcommerceCustomerAddresses](docs/models/EcommerceCustomerAddresses.md)
 - [EcommerceCustomersFilter](docs/models/EcommerceCustomersFilter.md)
 - [EcommerceDiscount](docs/models/EcommerceDiscount.md)
 - [EcommerceEventType](docs/models/EcommerceEventType.md)
 - [EcommerceOrder](docs/models/EcommerceOrder.md)
 - [EcommerceOrderLineItem](docs/models/EcommerceOrderLineItem.md)
 - [EcommerceOrderRefund](docs/models/EcommerceOrderRefund.md)
 - [EcommerceOrderStatus](docs/models/EcommerceOrderStatus.md)
 - [EcommerceOrdersFilter](docs/models/EcommerceOrdersFilter.md)
 - [EcommerceProduct](docs/models/EcommerceProduct.md)
 - [EcommerceProductCategories](docs/models/EcommerceProductCategories.md)
 - [EcommerceProductImages](docs/models/EcommerceProductImages.md)
 - [EcommerceProductImages1](docs/models/EcommerceProductImages1.md)
 - [EcommerceProductOptions](docs/models/EcommerceProductOptions.md)
 - [EcommerceProductOptions1](docs/models/EcommerceProductOptions1.md)
 - [EcommerceProductVariants](docs/models/EcommerceProductVariants.md)
 - [EcommerceStore](docs/models/EcommerceStore.md)
 - [Email](docs/models/Email.md)
 - [Employee](docs/models/Employee.md)
 - [EmployeeCompensation](docs/models/EmployeeCompensation.md)
 - [EmployeeEmploymentRole](docs/models/EmployeeEmploymentRole.md)
 - [EmployeeJob](docs/models/EmployeeJob.md)
 - [EmployeeList](docs/models/EmployeeList.md)
 - [EmployeeManager](docs/models/EmployeeManager.md)
 - [EmployeePayroll](docs/models/EmployeePayroll.md)
 - [EmployeeSchedules](docs/models/EmployeeSchedules.md)
 - [EmployeesFilter](docs/models/EmployeesFilter.md)
 - [EmployeesOneFilter](docs/models/EmployeesOneFilter.md)
 - [EmployeesSort](docs/models/EmployeesSort.md)
 - [EmploymentStatus](docs/models/EmploymentStatus.md)
 - [Error](docs/models/Error.md)
 - [ExecuteBaseUrl](docs/models/ExecuteBaseUrl.md)
 - [ExecuteWebhookEventRequest](docs/models/ExecuteWebhookEventRequest.md)
 - [ExecuteWebhookEventsRequest](docs/models/ExecuteWebhookEventsRequest.md)
 - [ExecuteWebhookResponse](docs/models/ExecuteWebhookResponse.md)
 - [Expense](docs/models/Expense.md)
 - [ExpenseLineItem](docs/models/ExpenseLineItem.md)
 - [Expenses](docs/models/Expenses.md)
 - [FileStorageEventType](docs/models/FileStorageEventType.md)
 - [FileType](docs/models/FileType.md)
 - [FilesFilter](docs/models/FilesFilter.md)
 - [FilesSearch](docs/models/FilesSearch.md)
 - [FilesSort](docs/models/FilesSort.md)
 - [Folder](docs/models/Folder.md)
 - [FormField](docs/models/FormField.md)
 - [FormFieldOption](docs/models/FormFieldOption.md)
 - [FormFieldOptionGroup](docs/models/FormFieldOptionGroup.md)
 - [Gender](docs/models/Gender.md)
 - [GetAccountingDepartmentResponse](docs/models/GetAccountingDepartmentResponse.md)
 - [GetAccountingDepartmentsResponse](docs/models/GetAccountingDepartmentsResponse.md)
 - [GetAccountingLocationResponse](docs/models/GetAccountingLocationResponse.md)
 - [GetAccountingLocationsResponse](docs/models/GetAccountingLocationsResponse.md)
 - [GetActivitiesResponse](docs/models/GetActivitiesResponse.md)
 - [GetActivityResponse](docs/models/GetActivityResponse.md)
 - [GetAgedCreditorsResponse](docs/models/GetAgedCreditorsResponse.md)
 - [GetAgedDebtorsResponse](docs/models/GetAgedDebtorsResponse.md)
 - [GetApiResourceCoverageResponse](docs/models/GetApiResourceCoverageResponse.md)
 - [GetApiResourceResponse](docs/models/GetApiResourceResponse.md)
 - [GetApiResponse](docs/models/GetApiResponse.md)
 - [GetApisResponse](docs/models/GetApisResponse.md)
 - [GetApplicantResponse](docs/models/GetApplicantResponse.md)
 - [GetApplicantsResponse](docs/models/GetApplicantsResponse.md)
 - [GetApplicationResponse](docs/models/GetApplicationResponse.md)
 - [GetApplicationsResponse](docs/models/GetApplicationsResponse.md)
 - [GetAttachmentResponse](docs/models/GetAttachmentResponse.md)
 - [GetAttachmentsResponse](docs/models/GetAttachmentsResponse.md)
 - [GetBalanceSheetResponse](docs/models/GetBalanceSheetResponse.md)
 - [GetBankFeedAccountResponse](docs/models/GetBankFeedAccountResponse.md)
 - [GetBankFeedAccountsResponse](docs/models/GetBankFeedAccountsResponse.md)
 - [GetBankFeedStatementResponse](docs/models/GetBankFeedStatementResponse.md)
 - [GetBankFeedStatementsResponse](docs/models/GetBankFeedStatementsResponse.md)
 - [GetBillPaymentResponse](docs/models/GetBillPaymentResponse.md)
 - [GetBillPaymentsResponse](docs/models/GetBillPaymentsResponse.md)
 - [GetBillResponse](docs/models/GetBillResponse.md)
 - [GetBillsResponse](docs/models/GetBillsResponse.md)
 - [GetCollectionResponse](docs/models/GetCollectionResponse.md)
 - [GetCollectionTagsResponse](docs/models/GetCollectionTagsResponse.md)
 - [GetCollectionUserResponse](docs/models/GetCollectionUserResponse.md)
 - [GetCollectionUsersResponse](docs/models/GetCollectionUsersResponse.md)
 - [GetCollectionsResponse](docs/models/GetCollectionsResponse.md)
 - [GetCommentResponse](docs/models/GetCommentResponse.md)
 - [GetCommentsResponse](docs/models/GetCommentsResponse.md)
 - [GetCompaniesResponse](docs/models/GetCompaniesResponse.md)
 - [GetCompanyInfoResponse](docs/models/GetCompanyInfoResponse.md)
 - [GetCompanyResponse](docs/models/GetCompanyResponse.md)
 - [GetConnectionResponse](docs/models/GetConnectionResponse.md)
 - [GetConnectionsResponse](docs/models/GetConnectionsResponse.md)
 - [GetConnectorResourceExampleResponse](docs/models/GetConnectorResourceExampleResponse.md)
 - [GetConnectorResourceExampleResponseData](docs/models/GetConnectorResourceExampleResponseData.md)
 - [GetConnectorResourceResponse](docs/models/GetConnectorResourceResponse.md)
 - [GetConnectorResourceSchemaResponse](docs/models/GetConnectorResourceSchemaResponse.md)
 - [GetConnectorResponse](docs/models/GetConnectorResponse.md)
 - [GetConnectorsResponse](docs/models/GetConnectorsResponse.md)
 - [GetConsumerResponse](docs/models/GetConsumerResponse.md)
 - [GetConsumersResponse](docs/models/GetConsumersResponse.md)
 - [GetConsumersResponseData](docs/models/GetConsumersResponseData.md)
 - [GetContactResponse](docs/models/GetContactResponse.md)
 - [GetContactsResponse](docs/models/GetContactsResponse.md)
 - [GetCreditNoteResponse](docs/models/GetCreditNoteResponse.md)
 - [GetCreditNotesResponse](docs/models/GetCreditNotesResponse.md)
 - [GetCustomFieldsResponse](docs/models/GetCustomFieldsResponse.md)
 - [GetCustomMappingResponse](docs/models/GetCustomMappingResponse.md)
 - [GetCustomMappingsResponse](docs/models/GetCustomMappingsResponse.md)
 - [GetCustomObjectResponse](docs/models/GetCustomObjectResponse.md)
 - [GetCustomObjectSchemaResponse](docs/models/GetCustomObjectSchemaResponse.md)
 - [GetCustomObjectSchemasResponse](docs/models/GetCustomObjectSchemasResponse.md)
 - [GetCustomObjectsResponse](docs/models/GetCustomObjectsResponse.md)
 - [GetCustomerResponse](docs/models/GetCustomerResponse.md)
 - [GetCustomersResponse](docs/models/GetCustomersResponse.md)
 - [GetDepartmentResponse](docs/models/GetDepartmentResponse.md)
 - [GetDepartmentsResponse](docs/models/GetDepartmentsResponse.md)
 - [GetDriveGroupResponse](docs/models/GetDriveGroupResponse.md)
 - [GetDriveGroupsResponse](docs/models/GetDriveGroupsResponse.md)
 - [GetDriveResponse](docs/models/GetDriveResponse.md)
 - [GetDrivesResponse](docs/models/GetDrivesResponse.md)
 - [GetEcommerceCustomerResponse](docs/models/GetEcommerceCustomerResponse.md)
 - [GetEcommerceCustomersResponse](docs/models/GetEcommerceCustomersResponse.md)
 - [GetEcommerceOrderResponse](docs/models/GetEcommerceOrderResponse.md)
 - [GetEcommerceOrdersResponse](docs/models/GetEcommerceOrdersResponse.md)
 - [GetEmployeePayrollResponse](docs/models/GetEmployeePayrollResponse.md)
 - [GetEmployeePayrollsResponse](docs/models/GetEmployeePayrollsResponse.md)
 - [GetEmployeeResponse](docs/models/GetEmployeeResponse.md)
 - [GetEmployeeSchedulesResponse](docs/models/GetEmployeeSchedulesResponse.md)
 - [GetEmployeesResponse](docs/models/GetEmployeesResponse.md)
 - [GetExpenseResponse](docs/models/GetExpenseResponse.md)
 - [GetExpensesResponse](docs/models/GetExpensesResponse.md)
 - [GetFileResponse](docs/models/GetFileResponse.md)
 - [GetFilesResponse](docs/models/GetFilesResponse.md)
 - [GetFolderResponse](docs/models/GetFolderResponse.md)
 - [GetFoldersResponse](docs/models/GetFoldersResponse.md)
 - [GetHrisCompaniesResponse](docs/models/GetHrisCompaniesResponse.md)
 - [GetHrisCompanyResponse](docs/models/GetHrisCompanyResponse.md)
 - [GetHrisJobResponse](docs/models/GetHrisJobResponse.md)
 - [GetHrisJobsResponse](docs/models/GetHrisJobsResponse.md)
 - [GetInvoiceItemResponse](docs/models/GetInvoiceItemResponse.md)
 - [GetInvoiceItemsResponse](docs/models/GetInvoiceItemsResponse.md)
 - [GetInvoiceResponse](docs/models/GetInvoiceResponse.md)
 - [GetInvoicesResponse](docs/models/GetInvoicesResponse.md)
 - [GetItemResponse](docs/models/GetItemResponse.md)
 - [GetItemsResponse](docs/models/GetItemsResponse.md)
 - [GetJobResponse](docs/models/GetJobResponse.md)
 - [GetJobsResponse](docs/models/GetJobsResponse.md)
 - [GetJournalEntriesResponse](docs/models/GetJournalEntriesResponse.md)
 - [GetJournalEntryResponse](docs/models/GetJournalEntryResponse.md)
 - [GetLeadResponse](docs/models/GetLeadResponse.md)
 - [GetLeadsResponse](docs/models/GetLeadsResponse.md)
 - [GetLedgerAccountResponse](docs/models/GetLedgerAccountResponse.md)
 - [GetLedgerAccountsResponse](docs/models/GetLedgerAccountsResponse.md)
 - [GetLocationResponse](docs/models/GetLocationResponse.md)
 - [GetLocationsResponse](docs/models/GetLocationsResponse.md)
 - [GetLogsResponse](docs/models/GetLogsResponse.md)
 - [GetMerchantResponse](docs/models/GetMerchantResponse.md)
 - [GetMerchantsResponse](docs/models/GetMerchantsResponse.md)
 - [GetMessageResponse](docs/models/GetMessageResponse.md)
 - [GetMessagesResponse](docs/models/GetMessagesResponse.md)
 - [GetModifierGroupResponse](docs/models/GetModifierGroupResponse.md)
 - [GetModifierGroupsResponse](docs/models/GetModifierGroupsResponse.md)
 - [GetModifierResponse](docs/models/GetModifierResponse.md)
 - [GetModifiersResponse](docs/models/GetModifiersResponse.md)
 - [GetNoteResponse](docs/models/GetNoteResponse.md)
 - [GetNotesResponse](docs/models/GetNotesResponse.md)
 - [GetOpportunitiesResponse](docs/models/GetOpportunitiesResponse.md)
 - [GetOpportunityResponse](docs/models/GetOpportunityResponse.md)
 - [GetOrderResponse](docs/models/GetOrderResponse.md)
 - [GetOrderTypeResponse](docs/models/GetOrderTypeResponse.md)
 - [GetOrderTypesResponse](docs/models/GetOrderTypesResponse.md)
 - [GetOrdersResponse](docs/models/GetOrdersResponse.md)
 - [GetPaymentResponse](docs/models/GetPaymentResponse.md)
 - [GetPaymentsResponse](docs/models/GetPaymentsResponse.md)
 - [GetPayrollResponse](docs/models/GetPayrollResponse.md)
 - [GetPayrollsResponse](docs/models/GetPayrollsResponse.md)
 - [GetPipelineResponse](docs/models/GetPipelineResponse.md)
 - [GetPipelinesResponse](docs/models/GetPipelinesResponse.md)
 - [GetPosPaymentResponse](docs/models/GetPosPaymentResponse.md)
 - [GetPosPaymentsResponse](docs/models/GetPosPaymentsResponse.md)
 - [GetProductResponse](docs/models/GetProductResponse.md)
 - [GetProductsResponse](docs/models/GetProductsResponse.md)
 - [GetProfitAndLossResponse](docs/models/GetProfitAndLossResponse.md)
 - [GetPurchaseOrderResponse](docs/models/GetPurchaseOrderResponse.md)
 - [GetPurchaseOrdersResponse](docs/models/GetPurchaseOrdersResponse.md)
 - [GetResourceExampleResponse](docs/models/GetResourceExampleResponse.md)
 - [GetResourceSchemaResponse](docs/models/GetResourceSchemaResponse.md)
 - [GetSharedLinkResponse](docs/models/GetSharedLinkResponse.md)
 - [GetSharedLinksResponse](docs/models/GetSharedLinksResponse.md)
 - [GetStoreResponse](docs/models/GetStoreResponse.md)
 - [GetStoresResponse](docs/models/GetStoresResponse.md)
 - [GetSubsidiariesResponse](docs/models/GetSubsidiariesResponse.md)
 - [GetSubsidiaryResponse](docs/models/GetSubsidiaryResponse.md)
 - [GetSupplierResponse](docs/models/GetSupplierResponse.md)
 - [GetSuppliersResponse](docs/models/GetSuppliersResponse.md)
 - [GetTaxRateResponse](docs/models/GetTaxRateResponse.md)
 - [GetTaxRatesResponse](docs/models/GetTaxRatesResponse.md)
 - [GetTenderResponse](docs/models/GetTenderResponse.md)
 - [GetTendersResponse](docs/models/GetTendersResponse.md)
 - [GetTicketResponse](docs/models/GetTicketResponse.md)
 - [GetTicketsResponse](docs/models/GetTicketsResponse.md)
 - [GetTimeOffRequestResponse](docs/models/GetTimeOffRequestResponse.md)
 - [GetTimeOffRequestsResponse](docs/models/GetTimeOffRequestsResponse.md)
 - [GetTrackingCategoriesResponse](docs/models/GetTrackingCategoriesResponse.md)
 - [GetTrackingCategoryResponse](docs/models/GetTrackingCategoryResponse.md)
 - [GetUploadSessionResponse](docs/models/GetUploadSessionResponse.md)
 - [GetUserResponse](docs/models/GetUserResponse.md)
 - [GetUsersResponse](docs/models/GetUsersResponse.md)
 - [GetWebhookEventLogsResponse](docs/models/GetWebhookEventLogsResponse.md)
 - [GetWebhookResponse](docs/models/GetWebhookResponse.md)
 - [GetWebhooksResponse](docs/models/GetWebhooksResponse.md)
 - [HrisCompany](docs/models/HrisCompany.md)
 - [HrisEventType](docs/models/HrisEventType.md)
 - [HrisJob](docs/models/HrisJob.md)
 - [HrisJobLocation](docs/models/HrisJobLocation.md)
 - [HrisJobs](docs/models/HrisJobs.md)
 - [IdempotencyKey](docs/models/IdempotencyKey.md)
 - [Income](docs/models/Income.md)
 - [IntegrationState](docs/models/IntegrationState.md)
 - [Invoice](docs/models/Invoice.md)
 - [InvoiceItem](docs/models/InvoiceItem.md)
 - [InvoiceItemAssetAccount](docs/models/InvoiceItemAssetAccount.md)
 - [InvoiceItemExpenseAccount](docs/models/InvoiceItemExpenseAccount.md)
 - [InvoiceItemFilter](docs/models/InvoiceItemFilter.md)
 - [InvoiceItemIncomeAccount](docs/models/InvoiceItemIncomeAccount.md)
 - [InvoiceItemSalesDetails](docs/models/InvoiceItemSalesDetails.md)
 - [InvoiceItemsFilter](docs/models/InvoiceItemsFilter.md)
 - [InvoiceItemsSort](docs/models/InvoiceItemsSort.md)
 - [InvoiceLineItem](docs/models/InvoiceLineItem.md)
 - [InvoicePaymentAllocations](docs/models/InvoicePaymentAllocations.md)
 - [InvoiceResponse](docs/models/InvoiceResponse.md)
 - [InvoicesFilter](docs/models/InvoicesFilter.md)
 - [InvoicesSort](docs/models/InvoicesSort.md)
 - [IssueTrackingEventType](docs/models/IssueTrackingEventType.md)
 - [IssuesFilter](docs/models/IssuesFilter.md)
 - [Item](docs/models/Item.md)
 - [Job](docs/models/Job.md)
 - [JobLinks](docs/models/JobLinks.md)
 - [JobSalary](docs/models/JobSalary.md)
 - [JobStatus](docs/models/JobStatus.md)
 - [JournalEntriesFilter](docs/models/JournalEntriesFilter.md)
 - [JournalEntriesSort](docs/models/JournalEntriesSort.md)
 - [JournalEntry](docs/models/JournalEntry.md)
 - [JournalEntryLineItem](docs/models/JournalEntryLineItem.md)
 - [Lead](docs/models/Lead.md)
 - [LeadEventType](docs/models/LeadEventType.md)
 - [LeadsFilter](docs/models/LeadsFilter.md)
 - [LeadsSort](docs/models/LeadsSort.md)
 - [LedgerAccount](docs/models/LedgerAccount.md)
 - [LedgerAccountCategories](docs/models/LedgerAccountCategories.md)
 - [LedgerAccountParentAccount](docs/models/LedgerAccountParentAccount.md)
 - [LedgerAccounts](docs/models/LedgerAccounts.md)
 - [LedgerAccountsFilter](docs/models/LedgerAccountsFilter.md)
 - [LedgerAccountsSort](docs/models/LedgerAccountsSort.md)
 - [LinkedConnectorResource](docs/models/LinkedConnectorResource.md)
 - [LinkedCustomer](docs/models/LinkedCustomer.md)
 - [LinkedEcommerceCustomer](docs/models/LinkedEcommerceCustomer.md)
 - [LinkedEcommerceOrder](docs/models/LinkedEcommerceOrder.md)
 - [LinkedFolder](docs/models/LinkedFolder.md)
 - [LinkedInvoiceItem](docs/models/LinkedInvoiceItem.md)
 - [LinkedLedgerAccount](docs/models/LinkedLedgerAccount.md)
 - [LinkedParentCustomer](docs/models/LinkedParentCustomer.md)
 - [LinkedSupplier](docs/models/LinkedSupplier.md)
 - [LinkedTaxRate](docs/models/LinkedTaxRate.md)
 - [LinkedTrackingCategories](docs/models/LinkedTrackingCategories.md)
 - [LinkedTrackingCategory](docs/models/LinkedTrackingCategory.md)
 - [Links](docs/models/Links.md)
 - [Location](docs/models/Location.md)
 - [Log](docs/models/Log.md)
 - [LogOperation](docs/models/LogOperation.md)
 - [LogService](docs/models/LogService.md)
 - [LogsFilter](docs/models/LogsFilter.md)
 - [Merchant](docs/models/Merchant.md)
 - [Message](docs/models/Message.md)
 - [Meta](docs/models/Meta.md)
 - [MetaCursors](docs/models/MetaCursors.md)
 - [Modifier](docs/models/Modifier.md)
 - [ModifierGroup](docs/models/ModifierGroup.md)
 - [ModifierGroupFilter](docs/models/ModifierGroupFilter.md)
 - [NotFoundResponse](docs/models/NotFoundResponse.md)
 - [NotImplementedResponse](docs/models/NotImplementedResponse.md)
 - [Note](docs/models/Note.md)
 - [OAuthGrantType](docs/models/OAuthGrantType.md)
 - [Offer](docs/models/Offer.md)
 - [OpportunitiesFilter](docs/models/OpportunitiesFilter.md)
 - [OpportunitiesSort](docs/models/OpportunitiesSort.md)
 - [Opportunity](docs/models/Opportunity.md)
 - [Order](docs/models/Order.md)
 - [OrderCustomers](docs/models/OrderCustomers.md)
 - [OrderDiscounts](docs/models/OrderDiscounts.md)
 - [OrderFulfillments](docs/models/OrderFulfillments.md)
 - [OrderLineItems](docs/models/OrderLineItems.md)
 - [OrderPayments](docs/models/OrderPayments.md)
 - [OrderPickupDetails](docs/models/OrderPickupDetails.md)
 - [OrderPickupDetailsCurbsidePickupDetails](docs/models/OrderPickupDetailsCurbsidePickupDetails.md)
 - [OrderPickupDetailsRecipient](docs/models/OrderPickupDetailsRecipient.md)
 - [OrderRefunds](docs/models/OrderRefunds.md)
 - [OrderTenders](docs/models/OrderTenders.md)
 - [OrderType](docs/models/OrderType.md)
 - [OrdersSort](docs/models/OrdersSort.md)
 - [OtherExpenses](docs/models/OtherExpenses.md)
 - [OtherIncome](docs/models/OtherIncome.md)
 - [OutstandingBalanceByCurrency](docs/models/OutstandingBalanceByCurrency.md)
 - [OutstandingBalanceByCustomer](docs/models/OutstandingBalanceByCustomer.md)
 - [OutstandingBalanceBySupplier](docs/models/OutstandingBalanceBySupplier.md)
 - [Owner](docs/models/Owner.md)
 - [PaginationCoverage](docs/models/PaginationCoverage.md)
 - [PassThroughBody](docs/models/PassThroughBody.md)
 - [PassThroughQuery](docs/models/PassThroughQuery.md)
 - [Payment](docs/models/Payment.md)
 - [PaymentCard](docs/models/PaymentCard.md)
 - [PaymentFrequency](docs/models/PaymentFrequency.md)
 - [PaymentRequiredResponse](docs/models/PaymentRequiredResponse.md)
 - [PaymentStatus](docs/models/PaymentStatus.md)
 - [PaymentType](docs/models/PaymentType.md)
 - [PaymentUnit](docs/models/PaymentUnit.md)
 - [PaymentsFilter](docs/models/PaymentsFilter.md)
 - [PaymentsSort](docs/models/PaymentsSort.md)
 - [Payroll](docs/models/Payroll.md)
 - [PayrollTotals](docs/models/PayrollTotals.md)
 - [PayrollsFilter](docs/models/PayrollsFilter.md)
 - [Person](docs/models/Person.md)
 - [PhoneNumber](docs/models/PhoneNumber.md)
 - [Pipeline](docs/models/Pipeline.md)
 - [PipelineStages](docs/models/PipelineStages.md)
 - [PosBankAccount](docs/models/PosBankAccount.md)
 - [PosBankAccountAchDetails](docs/models/PosBankAccountAchDetails.md)
 - [PosPayment](docs/models/PosPayment.md)
 - [PosPaymentCardDetails](docs/models/PosPaymentCardDetails.md)
 - [PosPaymentExternalDetails](docs/models/PosPaymentExternalDetails.md)
 - [Price](docs/models/Price.md)
 - [ProbationPeriod](docs/models/ProbationPeriod.md)
 - [ProfitAndLoss](docs/models/ProfitAndLoss.md)
 - [ProfitAndLossFilter](docs/models/ProfitAndLossFilter.md)
 - [ProfitAndLossIndicator](docs/models/ProfitAndLossIndicator.md)
 - [ProfitAndLossRecord](docs/models/ProfitAndLossRecord.md)
 - [ProfitAndLossRecords](docs/models/ProfitAndLossRecords.md)
 - [ProfitAndLossSection](docs/models/ProfitAndLossSection.md)
 - [ProfitAndLossType](docs/models/ProfitAndLossType.md)
 - [PurchaseOrder](docs/models/PurchaseOrder.md)
 - [PurchaseOrdersFilter](docs/models/PurchaseOrdersFilter.md)
 - [PurchaseOrdersSort](docs/models/PurchaseOrdersSort.md)
 - [Raw](docs/models/Raw.md)
 - [RequestCountAllocation](docs/models/RequestCountAllocation.md)
 - [RequestRate](docs/models/RequestRate.md)
 - [ResolveWebhookEventRequest](docs/models/ResolveWebhookEventRequest.md)
 - [ResolveWebhookEventsRequest](docs/models/ResolveWebhookEventsRequest.md)
 - [ResolveWebhookResponse](docs/models/ResolveWebhookResponse.md)
 - [ResourceExample](docs/models/ResourceExample.md)
 - [ResourceStatus](docs/models/ResourceStatus.md)
 - [Schedule](docs/models/Schedule.md)
 - [ScheduleWorkPattern](docs/models/ScheduleWorkPattern.md)
 - [ScheduleWorkPatternOddWeeks](docs/models/ScheduleWorkPatternOddWeeks.md)
 - [SchemaSupport](docs/models/SchemaSupport.md)
 - [ServiceCharge](docs/models/ServiceCharge.md)
 - [ServiceCharges](docs/models/ServiceCharges.md)
 - [Session](docs/models/Session.md)
 - [SessionSettings](docs/models/SessionSettings.md)
 - [SessionTheme](docs/models/SessionTheme.md)
 - [SharedLink](docs/models/SharedLink.md)
 - [SharedLinkTarget](docs/models/SharedLinkTarget.md)
 - [SimpleFormFieldOption](docs/models/SimpleFormFieldOption.md)
 - [SocialLink](docs/models/SocialLink.md)
 - [SortDirection](docs/models/SortDirection.md)
 - [Status](docs/models/Status.md)
 - [Subsidiary](docs/models/Subsidiary.md)
 - [SubsidiaryReference](docs/models/SubsidiaryReference.md)
 - [Supplier](docs/models/Supplier.md)
 - [SuppliersFilter](docs/models/SuppliersFilter.md)
 - [SuppliersSort](docs/models/SuppliersSort.md)
 - [SupportedProperty](docs/models/SupportedProperty.md)
 - [Tags](docs/models/Tags.md)
 - [Tax](docs/models/Tax.md)
 - [TaxRate](docs/models/TaxRate.md)
 - [TaxRatesFilter](docs/models/TaxRatesFilter.md)
 - [Team](docs/models/Team.md)
 - [Tender](docs/models/Tender.md)
 - [Ticket](docs/models/Ticket.md)
 - [TicketsSort](docs/models/TicketsSort.md)
 - [TimeOffRequest](docs/models/TimeOffRequest.md)
 - [TimeOffRequestNotes](docs/models/TimeOffRequestNotes.md)
 - [TimeOffRequestsFilter](docs/models/TimeOffRequestsFilter.md)
 - [TooManyRequestsResponse](docs/models/TooManyRequestsResponse.md)
 - [TooManyRequestsResponseDetail](docs/models/TooManyRequestsResponseDetail.md)
 - [TrackingCategory](docs/models/TrackingCategory.md)
 - [TrackingItem](docs/models/TrackingItem.md)
 - [UnauthorizedResponse](docs/models/UnauthorizedResponse.md)
 - [UncategorizedAccounts](docs/models/UncategorizedAccounts.md)
 - [UnexpectedErrorResponse](docs/models/UnexpectedErrorResponse.md)
 - [UnifiedApiId](docs/models/UnifiedApiId.md)
 - [UnifiedFile](docs/models/UnifiedFile.md)
 - [UnifiedFilePermissions](docs/models/UnifiedFilePermissions.md)
 - [UnifiedId](docs/models/UnifiedId.md)
 - [UnprocessableResponse](docs/models/UnprocessableResponse.md)
 - [UpdateAccountingDepartmentResponse](docs/models/UpdateAccountingDepartmentResponse.md)
 - [UpdateAccountingLocationResponse](docs/models/UpdateAccountingLocationResponse.md)
 - [UpdateActivityResponse](docs/models/UpdateActivityResponse.md)
 - [UpdateApplicantResponse](docs/models/UpdateApplicantResponse.md)
 - [UpdateApplicationResponse](docs/models/UpdateApplicationResponse.md)
 - [UpdateBankFeedAccountResponse](docs/models/UpdateBankFeedAccountResponse.md)
 - [UpdateBankFeedStatementResponse](docs/models/UpdateBankFeedStatementResponse.md)
 - [UpdateBillPaymentResponse](docs/models/UpdateBillPaymentResponse.md)
 - [UpdateBillResponse](docs/models/UpdateBillResponse.md)
 - [UpdateCommentResponse](docs/models/UpdateCommentResponse.md)
 - [UpdateCompanyResponse](docs/models/UpdateCompanyResponse.md)
 - [UpdateConnectionResponse](docs/models/UpdateConnectionResponse.md)
 - [UpdateConsumerRequest](docs/models/UpdateConsumerRequest.md)
 - [UpdateConsumerResponse](docs/models/UpdateConsumerResponse.md)
 - [UpdateContactResponse](docs/models/UpdateContactResponse.md)
 - [UpdateCreditNoteResponse](docs/models/UpdateCreditNoteResponse.md)
 - [UpdateCustomMappingRequest](docs/models/UpdateCustomMappingRequest.md)
 - [UpdateCustomMappingResponse](docs/models/UpdateCustomMappingResponse.md)
 - [UpdateCustomObjectResponse](docs/models/UpdateCustomObjectResponse.md)
 - [UpdateCustomObjectSchemaResponse](docs/models/UpdateCustomObjectSchemaResponse.md)
 - [UpdateCustomerResponse](docs/models/UpdateCustomerResponse.md)
 - [UpdateDepartmentResponse](docs/models/UpdateDepartmentResponse.md)
 - [UpdateDriveGroupResponse](docs/models/UpdateDriveGroupResponse.md)
 - [UpdateDriveResponse](docs/models/UpdateDriveResponse.md)
 - [UpdateEcommerceCustomerResponse](docs/models/UpdateEcommerceCustomerResponse.md)
 - [UpdateEcommerceOrderResponse](docs/models/UpdateEcommerceOrderResponse.md)
 - [UpdateEmployeeResponse](docs/models/UpdateEmployeeResponse.md)
 - [UpdateExpenseResponse](docs/models/UpdateExpenseResponse.md)
 - [UpdateFileRequest](docs/models/UpdateFileRequest.md)
 - [UpdateFileResponse](docs/models/UpdateFileResponse.md)
 - [UpdateFolderRequest](docs/models/UpdateFolderRequest.md)
 - [UpdateFolderResponse](docs/models/UpdateFolderResponse.md)
 - [UpdateHrisCompanyResponse](docs/models/UpdateHrisCompanyResponse.md)
 - [UpdateInvoiceItemsResponse](docs/models/UpdateInvoiceItemsResponse.md)
 - [UpdateInvoiceResponse](docs/models/UpdateInvoiceResponse.md)
 - [UpdateItemResponse](docs/models/UpdateItemResponse.md)
 - [UpdateJobResponse](docs/models/UpdateJobResponse.md)
 - [UpdateJournalEntryResponse](docs/models/UpdateJournalEntryResponse.md)
 - [UpdateLeadResponse](docs/models/UpdateLeadResponse.md)
 - [UpdateLedgerAccountResponse](docs/models/UpdateLedgerAccountResponse.md)
 - [UpdateLocationResponse](docs/models/UpdateLocationResponse.md)
 - [UpdateMerchantResponse](docs/models/UpdateMerchantResponse.md)
 - [UpdateMessageResponse](docs/models/UpdateMessageResponse.md)
 - [UpdateModifierGroupResponse](docs/models/UpdateModifierGroupResponse.md)
 - [UpdateModifierResponse](docs/models/UpdateModifierResponse.md)
 - [UpdateNoteResponse](docs/models/UpdateNoteResponse.md)
 - [UpdateOpportunityResponse](docs/models/UpdateOpportunityResponse.md)
 - [UpdateOrderResponse](docs/models/UpdateOrderResponse.md)
 - [UpdateOrderTypeResponse](docs/models/UpdateOrderTypeResponse.md)
 - [UpdatePaymentResponse](docs/models/UpdatePaymentResponse.md)
 - [UpdatePipelineResponse](docs/models/UpdatePipelineResponse.md)
 - [UpdatePosPaymentResponse](docs/models/UpdatePosPaymentResponse.md)
 - [UpdateProductResponse](docs/models/UpdateProductResponse.md)
 - [UpdatePurchaseOrderResponse](docs/models/UpdatePurchaseOrderResponse.md)
 - [UpdateSharedLinkResponse](docs/models/UpdateSharedLinkResponse.md)
 - [UpdateSubsidiaryResponse](docs/models/UpdateSubsidiaryResponse.md)
 - [UpdateSupplierResponse](docs/models/UpdateSupplierResponse.md)
 - [UpdateTaxRateResponse](docs/models/UpdateTaxRateResponse.md)
 - [UpdateTenderResponse](docs/models/UpdateTenderResponse.md)
 - [UpdateTicketResponse](docs/models/UpdateTicketResponse.md)
 - [UpdateTimeOffRequestResponse](docs/models/UpdateTimeOffRequestResponse.md)
 - [UpdateTrackingCategoryResponse](docs/models/UpdateTrackingCategoryResponse.md)
 - [UpdateUploadSessionResponse](docs/models/UpdateUploadSessionResponse.md)
 - [UpdateUserResponse](docs/models/UpdateUserResponse.md)
 - [UpdateWebhookRequest](docs/models/UpdateWebhookRequest.md)
 - [UpdateWebhookResponse](docs/models/UpdateWebhookResponse.md)
 - [UploadSession](docs/models/UploadSession.md)
 - [Url](docs/models/Url.md)
 - [User](docs/models/User.md)
 - [ValidateConnectionStateResponse](docs/models/ValidateConnectionStateResponse.md)
 - [ValidateConnectionStateResponseData](docs/models/ValidateConnectionStateResponseData.md)
 - [VaultEventType](docs/models/VaultEventType.md)
 - [VirtualWebhooks](docs/models/VirtualWebhooks.md)
 - [VirtualWebhooksResources](docs/models/VirtualWebhooksResources.md)
 - [WalletDetails](docs/models/WalletDetails.md)
 - [Webhook](docs/models/Webhook.md)
 - [WebhookEvent](docs/models/WebhookEvent.md)
 - [WebhookEventLog](docs/models/WebhookEventLog.md)
 - [WebhookEventLogAttempts](docs/models/WebhookEventLogAttempts.md)
 - [WebhookEventLogService](docs/models/WebhookEventLogService.md)
 - [WebhookEventLogsFilter](docs/models/WebhookEventLogsFilter.md)
 - [WebhookEventLogsFilterService](docs/models/WebhookEventLogsFilterService.md)
 - [WebhookEventType](docs/models/WebhookEventType.md)
 - [WebhookSubscription](docs/models/WebhookSubscription.md)
 - [WebhookSupport](docs/models/WebhookSupport.md)
 - [Website](docs/models/Website.md)


## Documentation For Authorization



## apiKey


- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header



## applicationId


- **Type**: API key
- **API key parameter name**: x-apideck-app-id
- **Location**: HTTP header



## consumerId


- **Type**: API key
- **API key parameter name**: x-apideck-consumer-id
- **Location**: HTTP header


## Author

support@apideck.com


## Notes for Large OpenAPI documents

If the OpenAPI document is large, imports in apideck.apis and apideck.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:

- `from apideck.api.default_api import DefaultApi`
- `from apideck.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:

```
import sys
sys.setrecursionlimit(1500)
import apideck
from apideck.apis import *
from apideck.models import *
```

