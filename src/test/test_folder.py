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
from apideck.model.custom_mappings import CustomMappings
from apideck.model.linked_folder import LinkedFolder
from apideck.model.owner import Owner
globals()['CustomMappings'] = CustomMappings
globals()['LinkedFolder'] = LinkedFolder
globals()['Owner'] = Owner
from apideck.model.folder import Folder


class TestFolder(unittest.TestCase):
    """Folder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFolder(self):
        """Test Folder"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Folder()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
