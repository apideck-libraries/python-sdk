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
from apideck.model.linked_invoice_item import LinkedInvoiceItem
from apideck.model.linked_ledger_account import LinkedLedgerAccount
from apideck.model.linked_tax_rate import LinkedTaxRate
from apideck.model.linked_tracking_categories import LinkedTrackingCategories
globals()['LinkedInvoiceItem'] = LinkedInvoiceItem
globals()['LinkedLedgerAccount'] = LinkedLedgerAccount
globals()['LinkedTaxRate'] = LinkedTaxRate
globals()['LinkedTrackingCategories'] = LinkedTrackingCategories
from apideck.model.bill_line_item import BillLineItem


class TestBillLineItem(unittest.TestCase):
    """BillLineItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBillLineItem(self):
        """Test BillLineItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BillLineItem()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
