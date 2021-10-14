# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AirportModelCheckpoint(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, longname: str=None, shortname: str=None):  # noqa: E501
        """AirportModelCheckpoint - a model defined in Swagger

        :param id: The id of this AirportModelCheckpoint.  # noqa: E501
        :type id: int
        :param longname: The longname of this AirportModelCheckpoint.  # noqa: E501
        :type longname: str
        :param shortname: The shortname of this AirportModelCheckpoint.  # noqa: E501
        :type shortname: str
        """
        self.swagger_types = {
            'id': int,
            'longname': str,
            'shortname': str
        }

        self.attribute_map = {
            'id': 'id',
            'longname': 'longname',
            'shortname': 'shortname'
        }
        self._id = id
        self._longname = longname
        self._shortname = shortname

    @classmethod
    def from_dict(cls, dikt) -> 'AirportModelCheckpoint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AirportModel_checkpoint of this AirportModelCheckpoint.  # noqa: E501
        :rtype: AirportModelCheckpoint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this AirportModelCheckpoint.


        :return: The id of this AirportModelCheckpoint.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this AirportModelCheckpoint.


        :param id: The id of this AirportModelCheckpoint.
        :type id: int
        """

        self._id = id

    @property
    def longname(self) -> str:
        """Gets the longname of this AirportModelCheckpoint.


        :return: The longname of this AirportModelCheckpoint.
        :rtype: str
        """
        return self._longname

    @longname.setter
    def longname(self, longname: str):
        """Sets the longname of this AirportModelCheckpoint.


        :param longname: The longname of this AirportModelCheckpoint.
        :type longname: str
        """

        self._longname = longname

    @property
    def shortname(self) -> str:
        """Gets the shortname of this AirportModelCheckpoint.


        :return: The shortname of this AirportModelCheckpoint.
        :rtype: str
        """
        return self._shortname

    @shortname.setter
    def shortname(self, shortname: str):
        """Sets the shortname of this AirportModelCheckpoint.


        :param shortname: The shortname of this AirportModelCheckpoint.
        :type shortname: str
        """

        self._shortname = shortname
