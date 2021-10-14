import connexion
import six
import xmltodict
import json
import requests

from swagger_server.models.all_airports import AllAirports  # noqa: E501
from swagger_server import util


def get_airports():  # noqa: E501
    """Gets all the airports data

     # noqa: E501


    :rtype: AllAirports
    """

    url = "https://www.tsa.gov/data/apcp.xml"
    response = requests.get(url)
    data = xmltodict.parse(response.content)
    return data, 200
