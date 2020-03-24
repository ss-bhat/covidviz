import dash_html_components as html
import dash_core_components as dcc
from covid19viz.model import stats, map
from covid19viz.toolkit import config

_stats = stats.get_statistics()

component_stats = html.Div(
    children=[
        html.Div(
            children=[
                html.Img(
                    src="/assets/img/virus2.png",
                    className="logo"
                ),

                "TOTAL CONFIRMED",
                dcc.Markdown(
                    children="""
                    #### {}
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
                html.Img(
                    src="/assets/img/virus2.png",
                    className="logo"
                ),
                "TOTAL RECOVERED",
                dcc.Markdown(
                    children="""
                    #### {}
                    """.format(_stats['recovered'])
                )
            ],
            className="stats-card card2",
            style={
                "background-color": config.get('dash.ui.component_background_color'),
                "color": config.get('dash.ui.recovered_color')
            }
        ),
        html.Div(
            children=[
                html.Img(
                    src="/assets/img/virus2.png",
                    className="logo"
                ),
                "TOTAL DEATHS",
                dcc.Markdown(
                    children="""
                    #### {}
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
                        #map.get_map()
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
                html.Div(
                    children=[
                            dcc.Graph(
                                id="stats-by-country",
                                figure=stats.get_stats_by_country(),
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
                            figure=stats.get_current_stats_for_country(),
                            className="graph"
                        )
                    ],
                    className="stats-card",
                    style={
                        "background-color": config.get('dash.ui.component_background_color')
                    }
                )
            ],
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
                            {'label': '  Recovered', 'value': 'recovered'},
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

