import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from covid19viz.plugin import CovIdDashBoard
from covid19viz.model import stats
from covid19viz.utils import helper as h
import logging

log = logging.getLogger(__name__)


class RegisterDashApplication(CovIdDashBoard):

    def __init__(self):
        CovIdDashBoard.__init__(self)
        self._app = dash.Dash(
            __name__,
            assets_folder=h.get_static_dir_path()
        )

    @property
    def app(self):
        self.prepare_app()
        return self._app

    def register_routes(self):
        """
        Register all the routes to the dash board. Only css route is added
        :return: None
        """
        for r in self.routes():
            log.info("Adding route: {}".format(r.get('url')))
            self._app._add_url(r.get('url'), view_func=r.get('view_func'))

    def prepare_app(self):
        """
        Add all layout and components to the dash application
        :return: None
        """
        import os
        import logging.config
        logging_cnf = os.getcwd() + '/logger.ini'
        logging.config.fileConfig(logging_cnf)

        # Register routes. This is used to call css
        log.info("Adding routes")
        self.register_routes()

        # Header
        log.info("gathering header")
        _header = self.header()

        # Load components
        log.info("loading components")
        children = []
        _components = self.components()

        for _c in _components:
            children.append(_components.get(_c))

        # Create layout
        log.info("Creating layout")
        layout = html.Div([
            _header,
            html.Main(
                children=[
                    html.Div(
                        children=[
                            html.Div(
                                children=children,
                                id='page-content'
                            )
                        ],
                        className="container"
                    )
                ]
            )

        ])
        self._app.layout = layout

        @self._app.callback(
            Output(component_id='history-country-action', component_property='children'),
            [Input(component_id='history-country-action-input', component_property='value')]
        )
        def update_top_10_country_history(action):

            return dcc.Graph(
                id="history-cases-country",
                figure=stats.top_10_countries_cases_by_time(action),
                className="graph"
            )

        @self._app.callback(
            Output(component_id='graphs', component_property='children'),
            [Input('map-flex', "n_clicks")]
        )
        def update_graph(data):
            ctx = dash.callback_context
            print("************")
            print(ctx)
            for evt in ctx.triggered:
                print(evt)
            element = html.Div(
                children=[
                    html.Div(
                        children=[
                                dcc.Graph(
                                    id="stats-by-country",
                                    figure=stats.get_stats_by_country(country="india"),
                                    className="graph"
                                )
                        ],
                        className="stats-card",
                    ),
                    html.Div(
                        children=[
                            dcc.Graph(
                                id="current-cases-country",
                                figure=stats.get_current_stats_for_country(country='india'),
                                className="graph"
                            )
                        ],
                        className="stats-card"
                    )
                ],
                id="update-graph",
                className="flex-container"
            )
            return element
