from flask import jsonify, make_response
from covid19viz.utils import errors
from collections import OrderedDict
from covid19viz.utils.request_object import APIRequestObject
from covid19viz.toolkit import api_get, api_post
import logging

log = logging.getLogger(__name__)


class APIResponseObject(APIRequestObject):

    """
    All API actions are wrapped round this. This decides for a given request method
    suitable function name can be executed or not. Also prepares the user context before executing the API
    This object is wrapped around flask request object and self.request contains all the attributes for flask request
    """

    def __init__(self, *args, **kwargs):
        APIRequestObject.__init__(self, is_api=True)
        self._response = None

    def __repr__(self):
        """
        Representation
        :return:
        """
        return "This API response object contains an attribute response"

    def __str__(self):
        """
        This is print method
        :return:
        """
        return APIResponseObject.__doc__

    def __call__(self, *args, **kwargs):
        """
        Call the main prepare method
        :param args:
        :param kwargs:
        :return: prepares the response
        """
        _func = args[0]
        self._prepare(_func)

    @property
    def response(self):
        """
        Response property
        :return: Flask response
        """
        return self._response

    @response.setter
    def response(self, resp):
        """
        Set the response
        :param resp:
        :return: Flask response function
        """
        self._response = resp

    def _make_error_response(self, e, err_code=404):
        """
        This makes the flask json response with suitable error code and error message.
        :param e: Error object
        :return: Json Response
        """
        msg = e.args[0]
        _error = dict()
        _error['error_type'] = e.__class__.__name__
        if err_code == 500:
            _error['message'] = "Internal Server Error"
        else:
            _error['message'] = msg

        self.response = make_response(jsonify({"status": "failed", "error": _error}), err_code)

    def _make_success_response(self, result):
        """
        This will create a success response 200. If the result is of type list include count.
        :param result: result from the api action either dictionary or list
        :return:
        """
        resp = OrderedDict()

        resp['status'] = "success"
        if isinstance(result, list):
            resp['count'] = len(result)
        resp['result'] = result
        self.response = make_response(jsonify(resp), 200)

    def _prepare(self, func):
        """
        Handle all possible errors that arise from during api calls and suitable response will be set
        :param func:
        :return:
        """

        try:
            result = func(self.context, self.data_dict)
            self._make_success_response(result)
        except errors.APIValidationError as e:
            self._make_error_response(e, 406)
        except errors.APIParameterError as e:
            self._make_error_response(e, 406)
        except errors.APIBadRequestType as e:
            self._make_error_response(e, 400)
        except errors.APIActionNotFound as e:
            self._make_error_response(e, 400)
        except Exception as e:
            log.error(e)
            self._make_error_response(e, 500)

    @staticmethod
    def actions(action_name):
        """
        All the /api/action/<action_name> should pass through this.
        Action name is processed and suitable response is given.
        :param action_name: function api action (get ot post)
        :return: JSON response
        """
        # Instantiate API response object
        resp = APIResponseObject()

        try:
            if resp.request.method == "GET":
                func = getattr(api_get, action_name)
                resp(func)
                return resp.response

            elif resp.request.method == "POST":
                func = getattr(api_post, action_name)
                resp(func)

            else:
                raise errors.NotImplemented("This is not implemented")
        except AttributeError:
            try:
                raise errors.APIActionNotFound("API action not available")
            except errors.APIActionNotFound as e:
                resp._make_error_response(e, 400)
                return resp.response
        except errors.NotImplemented as e:
            resp._make_error_response(e, 400)
            return resp.response
