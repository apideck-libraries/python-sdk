"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 8.85.1
    Generated by: https://openapi-generator.tech
"""


import unittest

import apideck
from apideck.api.ats_api import AtsApi  # noqa: E501


class TestAtsApi(unittest.TestCase):
    """AtsApi unit test stubs"""

    def setUp(self):
        self.api = AtsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_applicants_add(self):
        """Test case for applicants_add

        Create applicant  # noqa: E501
        """
        pass

    def test_applicants_all(self):
        """Test case for applicants_all

        List applicants  # noqa: E501
        """
        pass

    def test_applicants_one(self):
        """Test case for applicants_one

        Get applicant  # noqa: E501
        """
        pass

    def test_jobs_all(self):
        """Test case for jobs_all

        List Jobs  # noqa: E501
        """
        pass

    def test_jobs_one(self):
        """Test case for jobs_one

        Get Job  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
