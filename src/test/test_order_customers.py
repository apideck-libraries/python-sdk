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
from apideck.model.email import Email
from apideck.model.phone_number import PhoneNumber
globals()['Email'] = Email
globals()['PhoneNumber'] = PhoneNumber
from apideck.model.order_customers import OrderCustomers


class TestOrderCustomers(unittest.TestCase):
    """OrderCustomers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrderCustomers(self):
        """Test OrderCustomers"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OrderCustomers()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
