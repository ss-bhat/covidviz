from covid19viz.config import DashConfigParser


class DashDict(dict):
    """
    Dictionary used to assign values during run time
    and this can be locker from edition. i.e read only
    """

    _editable = True

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

    def __setitem__(self, key, value):
        if not self._editable:
            raise AttributeError("Closed dict not allowed to set/edit attribute/values")
        else:
            dict.__setitem__(self, key, value)

    def __setattr__(self, key, value):
        if not self._editable:
            raise AttributeError("Closed dict not allowed to set/edit attribute/values")
        else:
            dict.__setattr__(self, key, value)


class APIGetActions:
    """
    This is to hold all API get actions. Controller fetches methods from this call for GET actions
    """
    pass


class APIPostActions:
    """
    This is to hold all API post actions. Controller fetches methods from this call for POST actions
    """
    pass


class DashConfig(DashDict):
    """
    Holds config details of this application as dictionary. This is available as read only dict
    """

    def __init__(self, *args, **kwargs):
        DashDict.__init__(self, *args, **kwargs)

    def __repr__(self):
        return DashConfig.__doc__


def _get_config():
    _config = DashConfigParser()
    _config._editable = False
    return _config.parse()


api_get = APIGetActions()
api_post = APIGetActions()
config = _get_config()



