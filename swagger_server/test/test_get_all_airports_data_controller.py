# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.all_airports import AllAirports  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGetAllAirportsDataController(BaseTestCase):
    """GetAllAirportsDataController integration test stubs"""

    def test_get_airports(self):
        """Test case for get_airports

        Gets all the airports data
        """
        response = self.client.open(
            '//airports',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
