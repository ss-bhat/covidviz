from covid19viz.logic import api
from collections import OrderedDict
from covid19viz.utils import helper as h
from covid19viz.layouts import components, header, main_layout
from dash.dependencies import Input, Output
from covid19viz.logic import callbacks


class CovIdDashBoardAPIPlugin:
    """
    Dashboard and API plugin. Register all required API actions (GET or POST supported) and
    all dash components header, components and callbacks

    :parameter: api_url: url for the API actions

    Methods:
        dash_header: defines the header of the page
        dash_components: defines all the graphing components of the page
        dash_callbacks: defines the dash callbacks
        api_action: defines API actions
    """

    def __init__(self):
        self.api_url = "/api/v1/action"

    def dash_layout(self):
        """
        Register dash layout function. The layout function receives header, component and footer parameters
        :return: func
        """
        return main_layout.create_dash_layout

    def dash_header(self):
        """
        Get header element
        :return: dict
        """

        return header.header

    def dash_footer(self):
        """
        Register dash application footer
        :return:
        """
        return None

    def dash_components(self):
        """
        Register the required components orderd dict
        :return: Ordered Dict
        """
        dash_components = OrderedDict([
            ("stats", components.component_stats),
            ("map", components.component_map),
            ("graph", components.component_graph),
            ("trending", components.component_trending),
            ("history", components.component_history)
        ])

        return dash_components

    def dash_callbacks(self):
        """
        Register python dash callbacks to the app
            Format:
                module=<callback function>
                output=<dash output object>
                input=<dash input object> should be list
                state=<dash state object> should be list

        :return: tuple
        """
        dash_callbacks = (
            {
                "module": callbacks.update_top_10_country_history,
                "output": Output(component_id='history-country-action', component_property='children'),
                "input": [Input(component_id='history-country-action-input', component_property='value')],
                "state": []
            },
            {
                "module": callbacks.update_historical_data_for_country,
                "output": Output(component_id='update-graph', component_property='children'),
                "input": [Input(component_id='select-country', component_property='value')],
                "state": []
            },
        )

        return dash_callbacks

    def api_action(self):
        """
        To register all API's of this application
            Format: dict
                action = <action name>
                type = <GET or POST>
                module = <view function> which should returns dict or list

        :return: tuple
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
                "module": api.get_all_records_by_country

            },
            {
                "action": "get_all_records_by_provinces",
                "type": "GET",
                "module": api.get_all_records_by_provinces

            },
            {
                "action": "filter_by_country",
                "type": "GET",
                "module": api.filter_by_country

            },
            {
                "action": "filter_by_province",
                "type": "GET",
                "module": api.filter_by_province

            },
            {
                "action": "show_available_countries",
                "type": "GET",
                "module": api.show_available_countries

            },
            {
                "action": "show_available_regions",
                "type": "GET",
                "module": api.show_available_regions

            },
            {
                "action": "get_history_by_country",
                "type": "GET",
                "module": api.get_history_by_country

            },
            {
                "action": "get_history_by_province",
                "type": "GET",
                "module": api.get_history_by_province

            },
            {
                "action": "get_dash_ui_config",
                "type": "GET",
                "module": api.get_dash_ui_config
            }
        )

        return actions
