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
from apideck.model.bank_account import BankAccount
from apideck.model.bill_line_item import BillLineItem
from apideck.model.currency import Currency
from apideck.model.custom_field import CustomField
from apideck.model.custom_mappings import CustomMappings
from apideck.model.linked_ledger_account import LinkedLedgerAccount
from apideck.model.linked_supplier import LinkedSupplier
from apideck.model.linked_tracking_categories import LinkedTrackingCategories
from apideck.model.pass_through_body import PassThroughBody
globals()['BankAccount'] = BankAccount
globals()['BillLineItem'] = BillLineItem
globals()['Currency'] = Currency
globals()['CustomField'] = CustomField
globals()['CustomMappings'] = CustomMappings
globals()['LinkedLedgerAccount'] = LinkedLedgerAccount
globals()['LinkedSupplier'] = LinkedSupplier
globals()['LinkedTrackingCategories'] = LinkedTrackingCategories
globals()['PassThroughBody'] = PassThroughBody
from apideck.model.bill import Bill


class TestBill(unittest.TestCase):
    """Bill unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBill(self):
        """Test Bill"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Bill()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
