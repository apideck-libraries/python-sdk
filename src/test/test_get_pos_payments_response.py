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
from apideck.model.links import Links
from apideck.model.meta import Meta
from apideck.model.pos_payment import PosPayment
from apideck.model.raw import Raw
globals()['Links'] = Links
globals()['Meta'] = Meta
globals()['PosPayment'] = PosPayment
globals()['Raw'] = Raw
from apideck.model.get_pos_payments_response import GetPosPaymentsResponse


class TestGetPosPaymentsResponse(unittest.TestCase):
    """GetPosPaymentsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetPosPaymentsResponse(self):
        """Test GetPosPaymentsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetPosPaymentsResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
