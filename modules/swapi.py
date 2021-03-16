# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                      swapi: Star Wars API requests & responses
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import requests


PAGINATION_NUMBER = 10
ROOT_URL = 'https://swapi.dev/api/'  # root the https API adress


def get_data(url_request: str, full_url: bool = False) -> dict:
    """ Sends a request to the SWAPI API and returns the received response. """
    url = _set_url(url_request, full_url)
    return requests.get(url).json()


def get_data_name(url_request: str, full_url: bool = False) -> str:
    """ Sends a request to the SWAPI API and returns the name of a specific thing. """
    url = _set_url(url_request, full_url)
    all_data = requests.get(url).json()
    return all_data['name']


def _set_url(url_request: str, full_url: bool) -> str:
    return url_request if full_url else ROOT_URL + url_request
