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
from apideck.model.payment_frequency import PaymentFrequency
from apideck.model.payment_unit import PaymentUnit
globals()['Currency'] = Currency
globals()['PaymentFrequency'] = PaymentFrequency
globals()['PaymentUnit'] = PaymentUnit
from apideck.model.employee_compensation import EmployeeCompensation


class TestEmployeeCompensation(unittest.TestCase):
    """EmployeeCompensation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmployeeCompensation(self):
        """Test EmployeeCompensation"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EmployeeCompensation()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
