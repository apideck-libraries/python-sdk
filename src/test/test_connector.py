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
from apideck.model.connector_doc import ConnectorDoc
from apideck.model.connector_event import ConnectorEvent
from apideck.model.connector_oauth_scopes import ConnectorOauthScopes
from apideck.model.connector_setting import ConnectorSetting
from apideck.model.connector_status import ConnectorStatus
from apideck.model.connector_tls_support import ConnectorTlsSupport
from apideck.model.connector_unified_apis import ConnectorUnifiedApis
from apideck.model.linked_connector_resource import LinkedConnectorResource
from apideck.model.schema_support import SchemaSupport
from apideck.model.webhook_support import WebhookSupport
globals()['ConnectorDoc'] = ConnectorDoc
globals()['ConnectorEvent'] = ConnectorEvent
globals()['ConnectorOauthScopes'] = ConnectorOauthScopes
globals()['ConnectorSetting'] = ConnectorSetting
globals()['ConnectorStatus'] = ConnectorStatus
globals()['ConnectorTlsSupport'] = ConnectorTlsSupport
globals()['ConnectorUnifiedApis'] = ConnectorUnifiedApis
globals()['LinkedConnectorResource'] = LinkedConnectorResource
globals()['SchemaSupport'] = SchemaSupport
globals()['WebhookSupport'] = WebhookSupport
from apideck.model.connector import Connector


class TestConnector(unittest.TestCase):
    """Connector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConnector(self):
        """Test Connector"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Connector()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
