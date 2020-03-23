from covid19viz.logic import api
from collections import OrderedDict
from covid19viz.layouts import components, header


class CovIdDashBoard:

    def __init__(self):
        self._api_url = "/api/action/"

    def header(self):
        """
        Get header element
        :return: dict
        """

        return header.header

    def dash_components(self):
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
        ])

        return dash_components

    def api_action(self):
        """
        To register all API's
        :return: dict
        """
        actions = (
            {
                "action": "get_stats",
                "type": "GET",
                "module": api.get_stats

            },
            {
                "action": "get_all_records_by_country",
                "type": "GET",
                "module": ""

            },
            {
                "action": "get_all_records_by_provinces",
                "type": "GET",
                "module": ""

            },
            {
                "action": "filter_by_country",
                "type": "GET",
                "module": ""

            },
            {
                "action": "filter_by_province",
                "type": "GET",
                "module": ""

            },
            {
                "action": "show_available_countries",
                "type": "GET",
                "module": ""

            },
            {
                "action": "show_available_regions",
                "type": "GET",
                "module": ""

            },
            {
                "action": "get_history_by_country",
                "type": "GET",
                "module": ""

            },
            {
                "action": "get_history_by_province",
                "type": "GET",
                "module": ""

            }
        )

        return actions
