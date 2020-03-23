
class BaseDashException(Exception):
    pass


class NotFound(BaseDashException):
    pass


class APIParameterError(BaseDashException):
    pass
