"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.4.2
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.allocation import Allocation
from apideck.model.currency import Currency
from apideck.model.custom_field import CustomField
from apideck.model.linked_customer import LinkedCustomer
from apideck.model.linked_ledger_account import LinkedLedgerAccount
from apideck.model.linked_supplier import LinkedSupplier
globals()['Allocation'] = Allocation
globals()['Currency'] = Currency
globals()['CustomField'] = CustomField
globals()['LinkedCustomer'] = LinkedCustomer
globals()['LinkedLedgerAccount'] = LinkedLedgerAccount
globals()['LinkedSupplier'] = LinkedSupplier
from apideck.model.payment import Payment


class TestPayment(unittest.TestCase):
    """Payment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPayment(self):
        """Test Payment"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Payment()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
