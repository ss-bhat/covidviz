import dash_html_components as html
import dash_core_components as dcc
from covid19viz.model import stats
from covid19viz.toolkit import config
from covid19viz.utils import helper as h

_stats = stats.get_statistics()

component_stats = html.Div(
    children=[
        html.Div(
            children=[
                "TOTAL CONFIRMED - {}".format(h.get_last_updated_date(as_string=True)),
                dcc.Markdown(
                    children="""
                    ### {}
                    """.format(_stats['confirmed'])
                )
            ],
            className="stats-card card1",
            style={
                "background-color": config.get('dash.ui.component_background_color'),
                "color": config.get('dash.ui.confirmed_color')
            }
        ),
        html.Div(
            children=[
                "TOTAL DEATHS - {}".format(h.get_last_updated_date(as_string=True)),
                dcc.Markdown(
                    children="""
                    ### {}
                    """.format(_stats['deaths'])
                )
            ],
            className="stats-card card3",
            style={
                "background-color": config.get('dash.ui.component_background_color'),
                "color": config.get('dash.ui.deaths_color')
            }
        )
    ],
    id="stats",
    className="flex-container"
)

component_map = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                    ],
                    id="map",
                    style={"height": "100%"},
                    className="graph"
                )

            ],
            className="stats-card"
        )
    ],
    id="map-flex",
    className="flex-container",
    style={"minHeight": "700px"}
)


component_graph = html.Div(
    children=[
        html.Div(
            children=[
                html.Label(
                    children="Select Country: ",
                    style={'color': config.get('dash.ui.text_color')}
                ),
                dcc.Dropdown(
                    options=stats.get_all_countries_options(),
                    value=config.get('dash.default_country'),
                    style={
                        'maxWidth': "50%",
                        'background-color': config.get('dash.ui.layout_background_color'),
                        'color': config.get('dash.ui.text_color'),
                        'maxHeight': "40px"
                    },
                    id="select-country",
                    placeholder="Select Country"
                )
            ],
            style={
                "padding-left": "10px",
                "margin-left": "10px"
            }
        ),
        html.Div(
            id="update-graph",
            className="flex-container"
        )
    ],
    id="graphs"
)

component_trending = html.Div(
    children=[
        html.Div(
            children=[
                dcc.Graph(
                    id="highest-cases-country",
                    figure=stats.top_n_countries_confirmed_cases(),
                    className="graph"
                )
            ],
            className="stats-card",
            style={
                "background-color": config.get('dash.ui.component_background_color')
            }
        )

    ],
    id="trending",
    className="flex-container"
)

component_history = html.Div(
    children=[
        html.Div(
            children=[
                dcc.RadioItems(
                        options=[
                            {'label': '  Confirmed', 'value': 'confirmed'},
                            {'label': '  Deaths', 'value': 'deaths'}
                        ],
                        value='confirmed',
                        className="radio-buttons",
                        labelClassName="radio-button-label",
                        id="history-country-action-input",
                        style={
                            "color": config.get('dash.ui.text_color')
                        }
                    ),
                html.Div(
                    id="history-country-action"
                )
            ],
            className="stats-card",
            style={
                "background-color": config.get('dash.ui.component_background_color')
            }
        )

    ],
    id="trending-history",
    className="flex-container",
)

