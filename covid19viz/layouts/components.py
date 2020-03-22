import dash_html_components as html
import dash_core_components as dcc
from covid19viz.model import stats, map

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
            className="stats-card card1"
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
            className="stats-card card2"
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
            className="stats-card card3"
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
    style={"min-height": "500px"}
)


component_graph = html.Div(
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
        ),
        html.Div(
            children=[
                dcc.Graph(
                    id="current-cases-country",
                    figure=stats.get_current_stats_for_country(),
                    className="graph"
                )
            ],
            className="stats-card"
        )
    ],
    id="graphs",
    className="flex-container"
)

component_trending = html.Div(
    children=[
        html.Div(
            children=[
                dcc.Graph(
                    id="highest-cases-country",
                    figure=stats.top_10_countries_confirmed_cases(),
                    className="graph"
                )
            ],
            className="stats-card"
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
                        id="history-country-action-input"
                    ),
                html.Div(
                    id="history-country-action"
                )
            ],
            className="stats-card"
        )

    ],
    id="trending-history",
    className="flex-container"
)

