import json
from flask import request
import logging

log = logging.getLogger(__name__)


class APIRequestObject:
    """
    Add additional parameters for the request object.
    This build/validates the context, request type and parses the data from the request.
    """

    def __init__(self, is_api=False):
        self.request = request
        self.is_api = is_api
        self.action = str(self.request.url).split("/")[-1]
        self.context = {
                        "action": self.action,
                        "url": self.request.url,
                        "is_api": self.is_api
                        }
        self.data_dict = dict()
        self._validate_get_data()

    def _validate_get_data(self):
        """
        Validate the request object - content-type must be application/json.
        :return: raise error -
        """
        log.info("Validating the request and parsing the request data")
        mimetype = self.request.mimetype

        if self.is_api and mimetype != 'application/json':
            # Coming from the url
            self.data_dict = dict(self.request.args)
        else:
            try:
                self.data_dict = self.request.get_json()
            except json.JSONDecodeError as e:
                log.error(e)

