"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.6.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import apideck
from apideck.model.address import Address
from apideck.model.bank_account import BankAccount
from apideck.model.currency import Currency
from apideck.model.email import Email
from apideck.model.linked_ledger_account import LinkedLedgerAccount
from apideck.model.linked_parent_customer import LinkedParentCustomer
from apideck.model.linked_tax_rate import LinkedTaxRate
from apideck.model.phone_number import PhoneNumber
from apideck.model.website import Website
globals()['Address'] = Address
globals()['BankAccount'] = BankAccount
globals()['Currency'] = Currency
globals()['Email'] = Email
globals()['LinkedLedgerAccount'] = LinkedLedgerAccount
globals()['LinkedParentCustomer'] = LinkedParentCustomer
globals()['LinkedTaxRate'] = LinkedTaxRate
globals()['PhoneNumber'] = PhoneNumber
globals()['Website'] = Website
from apideck.model.customer import Customer


class TestCustomer(unittest.TestCase):
    """Customer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomer(self):
        """Test Customer"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Customer()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()