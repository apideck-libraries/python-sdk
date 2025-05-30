"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.17.2
    Contact: support@apideck.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.address import Address
from apideck.model.allocation import Allocation
from apideck.model.currency import Currency
from apideck.model.custom_field import CustomField
from apideck.model.custom_mappings import CustomMappings
from apideck.model.invoice_line_item import InvoiceLineItem
from apideck.model.linked_customer import LinkedCustomer
from apideck.model.linked_ledger_account import LinkedLedgerAccount
from apideck.model.linked_tracking_categories import LinkedTrackingCategories
from apideck.model.pass_through_body import PassThroughBody
globals()['Address'] = Address
globals()['Allocation'] = Allocation
globals()['Currency'] = Currency
globals()['CustomField'] = CustomField
globals()['CustomMappings'] = CustomMappings
globals()['InvoiceLineItem'] = InvoiceLineItem
globals()['LinkedCustomer'] = LinkedCustomer
globals()['LinkedLedgerAccount'] = LinkedLedgerAccount
globals()['LinkedTrackingCategories'] = LinkedTrackingCategories
globals()['PassThroughBody'] = PassThroughBody
from apideck.model.credit_note import CreditNote


class TestCreditNote(unittest.TestCase):
    """CreditNote unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreditNote(self):
        """Test CreditNote"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CreditNote()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
