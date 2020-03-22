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
            ("graph", components.component_graph),
            ("map", components.component_map),
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
                'url': "/all_country_location/",
                "view_func": route.get_locations_for_all_country
            },

        )

        return routes
