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
from apideck.model.currency import Currency
from apideck.model.custom_field import CustomField
from apideck.model.custom_mappings import CustomMappings
globals()['Currency'] = Currency
globals()['CustomField'] = CustomField
globals()['CustomMappings'] = CustomMappings
from apideck.model.bank_feed_account import BankFeedAccount


class TestBankFeedAccount(unittest.TestCase):
    """BankFeedAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBankFeedAccount(self):
        """Test BankFeedAccount"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BankFeedAccount()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
