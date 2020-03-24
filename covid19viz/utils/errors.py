
class BaseAppException(Exception):
    pass


class BaseDashException(BaseAppException):
    pass


class BaseApiException(BaseAppException):
    pass


class NotFound(BaseDashException):
    pass


class APIParameterError(BaseApiException):
    pass


class APIBadRequestType(BaseApiException):
    pass


class APIValidationError(BaseApiException):
    pass


class APIActionNotFound(BaseApiException):
    pass


class PluginError(BaseAppException):
    pass


class NotImplemented(BaseAppException):
    pass
