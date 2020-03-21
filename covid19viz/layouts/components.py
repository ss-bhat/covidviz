import dash_html_components as html
import dash_core_components as dcc
from covid19viz.model import stats

_stats = stats.get_statistics()

component_stats = html.Div(
    children=[
        html.Div(
            children=[
                html.Img(
                    src="/static/img/virus2.png",
                    className="logo"
                ),

                "CONFIRMED",
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
                    src="/static/img/virus2.png",
                    className="logo"
                ),
                "RECOVERED",
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
                    src="/static/img/virus2.png",
                    className="logo"
                ),
                "DEATHS",
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
                    html.H4(
                        children="Map"
                    )
                ],
                className="stats-card"
        )

    ],
    id="map",
    className="flex-container"
)


component_graph = html.Div(
    children=[
        html.Div(
            children=[
                html.H4(
                    children="stats 1"
                )
            ],
            className="stats-card"
        ),
        html.Div(
            children=[
                html.H4(
                    children="stats 2"
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
                    figure=stats.top_10_countries_confirmed_cases()
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
                dcc.Graph(
                    id="history-cases-country",
                    figure=stats.top_10_countries_confirmed_cases_by_time()
                )
            ],
            className="stats-card"
        )

    ],
    id="trending-history",
    className="flex-container"
)

