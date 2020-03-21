import dash
import dash_html_components as html
import dash_core_components as dcc
from covid19viz.plugin import CovIdDashBoard
from covid19viz.utils import helper as h
from covid19viz.model import stats
import logging

log = logging.getLogger(__name__)


class RegisterDashApplication(CovIdDashBoard):

    def __init__(self):
        CovIdDashBoard.__init__(self)
        self._external_css = None
        self._app = dash.Dash(__name__)

    def register_routes(self):
        """
        Register all the routes to the dash board. Only css route is added
        :return: None
        """
        for r in self.routes():
            log.info("Adding route: {}".format(r.get('url')))
            self._app._add_url(r.get('url'), view_func=r.get('view_func'))

    def get_custom_css(self):
        """
        get custom css for the python dash application.
        :return: None
        """
        log.info("Adding all css files")
        # add css as external style sheet
        external_stylesheets = []
        for _file in h.get_all_css_files():
            external_stylesheets.append(("/static/{}".format(_file)))
        self._external_css = external_stylesheets

    def get_custom_css_layout(self):
        """
        Add custom css to the dashboard
        :return: None
        """
        links = [dcc.Location(id='url', refresh=False)]
        for _f in self._external_css:
            links.append(
                html.Link(
                    rel='stylesheet',
                    href="{}".format(_f)
                )
            )
        return links

    def prepare_app(self):
        """
        Add all layout and components to the dash application
        :return: None
        """

        # Register routes. This is used to call css
        self.register_routes()

        # get custom css stylesheet
        self.get_custom_css()

        # Header
        _header = self.header()

        children = []
        _components = self.components()

        for _c in _components:
            children.append(_components.get(_c))

        layout = html.Div([
            html.Div(
                children=self.get_custom_css_layout()
            ),
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
