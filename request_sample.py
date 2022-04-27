import json
import requests
from requests.adapters import HTTPAdapter

from urllib.parse import urljoin, urlunsplit
from urllib.parse import urlencode


REQUEST_TIMEOUT = 90
class Client(object):
    """
    REST API client class
    """

    def __init__(self, base_url, username, password, **kwargs):
        """Initialize a client session"""
        self.session = requests.Session()
        self.session.mount("http://", HTTPAdapter(max_retries=kwargs.get("max_retries", 5)))
        self.session.mount("https://", HTTPAdapter(max_retries=kwargs.get("max_retries", 5)))
        self.session.auth = (username, password)
        self.session.verify = kwargs.get("ssl_cert_file", True)
        self.base_url = base_url
        self.session.headers.update(
            {"Content-Type": "application/json", "Accept": "application/json", "User-Agent": "Jenga Start Scripts"}
        )

    @staticmethod
    def construct_url(base_url, resource, **kwargs):
        url_parts = ("", "", urljoin(base_url, resource), urlencode(kwargs), "")
        return urlunsplit(url_parts)

    def _handle_response(self, response, resource):
        try:
            response.raise_for_status()
        except requests.HTTPError:
            try:
                result = response.json() if response.json() else response.text
            except ValueError:
                result = response.text
            raise requests.HTTPError(response, result, resource)  # pylint: disable=raise-missing-from

    def get(self, resource, **kwargs):
        """Send a GET request"""
        url = self.construct_url(self.base_url, resource, **kwargs)
        response = self.session.get(url, timeout=REQUEST_TIMEOUT)
        self._handle_response(response, resource)
        return json.loads(json.dumps(response.json()))

