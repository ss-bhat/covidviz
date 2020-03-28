import dash_core_components as dcc
import dash_html_components as html
from dash.exceptions import PreventUpdate
from covid19viz.toolkit import config
from covid19viz.model import stats
import os
import logging

log = logging.getLogger(__name__)


def update_top_10_country_history(action):
    """
    Call back for radio buttons. Which updates the top n countries
    history confirmed or recovered or death
    :param action:
    :return: dash graph object
    """
    logging.info("Callback function executing for top n country history")

    return dcc.Graph(
        id="history-cases-country",
        figure=stats.top_n_countries_cases_by_time(action),
        className="graph"
    )


def update_historical_data_for_country(country):
    """
    Update data per country
    :param country: str
    :return: dash div component
    """
    if not country:
        raise PreventUpdate
    return [
            html.Div(
                children=[
                    dcc.Graph(
                        id="stats-by-country",
                        figure=stats.get_stats_by_country(country=country),
                        className="graph"
                    )
                ],
                className="stats-card",
                style={
                    "background-color": config.get('dash.ui.component_background_color')
                }
            ),
            html.Div(
                children=[
                    dcc.Graph(
                        id="current-cases-country",
                        figure=stats.get_current_stats_for_country(country=country),
                        className="graph"
                    )
                ],
                className="stats-card",
                style={
                    "background-color": config.get('dash.ui.component_background_color')
                }
            )
        ]


def select_top_countries(value):
    """

    :param value:
    :return:
    """
    if not value:
        raise PreventUpdate

    element = dcc.Graph(
                    id="highest-cases-country",
                    figure=stats.top_n_countries_confirmed_cases(int(value)),
                    className="graph",
                    style={
                        "background-color": config.get('dash.ui.component_background_color')
                    }
                )
    return element


def get_api_documentation(click):
    """
    Get markdown from github
    :return: markdown
    """
    if not click:
        raise PreventUpdate

    _dir = os.path.dirname(os.path.abspath(__file__))
    with open("{}/README.md".format(_dir), 'r') as f:
        content = f.read()
        f.close()
    return html.Div(
        dcc.Markdown(
            content,
            style={
                'color': "#e4dede"
            }
        ),
        style={
            "padding": "10px"
        }
    )
