from covid19viz import route
from collections import OrderedDict
from covid19viz.layouts import components, header


class CovIdDashBoard:

    def __init__(self):
        pass

    def header(self):
        """
        Get header element
        :return: dict
        """

        return header.header

    def components(self):
        """
        Register the required components orderd dict
        :return: dict
        """
        dash_components = OrderedDict([
            ("stats", components.component_stats),
            ("map", components.component_map),
            ("graph", components.component_graph),
            ("trending", components.component_trending),
            ("history", components.component_history)
            #("change", components.component_change)
        ])

        return dash_components

    def routes(self):
        """
        To register routes to the python dash
        :return: dict
        """
        routes = (
            {
                "url": "/static/<stylesheet>",
                "view_func": route.serve_stylesheet
            },
            {
                "url": "/static/img/<img>",
                "view_func": route.server_image
            },
        )

        return routes
