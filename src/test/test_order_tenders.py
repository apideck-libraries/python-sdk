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
from apideck.model.payment_card import PaymentCard
globals()['Currency'] = Currency
globals()['PaymentCard'] = PaymentCard
from apideck.model.order_tenders import OrderTenders


class TestOrderTenders(unittest.TestCase):
    """OrderTenders unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrderTenders(self):
        """Test OrderTenders"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OrderTenders()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
