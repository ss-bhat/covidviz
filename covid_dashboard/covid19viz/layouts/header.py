import dash_html_components as html
from covid19viz.toolkit import config

header = html.Header(
    children=[
        html.H2(
            children=config.get('dash.app_title'),
            className="logo-text",
            style={
                "color": config.get('dash.ui.title_color'),
                "font-style": "oblique",
                "font-weight": "700"
            }
        ),
        html.Nav(
            html.Ul(
                children=[
                    html.A(
                        "Dashboard",
                        href="/",
                        className="navbar-brand btn btn-outline-info btn-sm",
                        style={
                            "font-size": "small"
                        }
                    ),
                    html.A(
                        "API Documentation",
                        href="#",
                        id="api-documentation",
                        className="navbar-brand btn btn-outline-info btn-sm",
                        style={
                            "font-size": "small"
                        }
                    ),
                ],
                className="navbar-nav"
            ),
            className="navbar navbar-expand-lg navbar-dark ml-auto"
        )
    ],
    id="nav-panel",
    className="navbar navbar-light",
    style={
        "background-color": config.get('dash.ui.header_background_color')
    }
)

footer = html.Footer(
    children=[
        html.A(
            children="Powered By: Dash",
            href="https://plotly.com/dash/",
            target="_blank",
            className="logo-text",
            style={
                "color": "#52545a",
                "margin": "10px"
            }
        )
    ],
    id="footer-panel",
    className="navbar navbar-light",
    style={
        "background-color": config.get('dash.ui.header_background_color')
    }
)