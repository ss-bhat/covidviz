import dash_html_components as html
from covid19viz.toolkit import config

header = html.Header(
    children=[
        html.H2(
            children=config.get('dash.app_title'),
            className="logo-text",
            style={
                "color": config.get('dash.ui.text_color')
            }
        ),
        html.Nav(
            html.Ul(
                children=[
                    html.A(
                        "API Documentation",
                        href="https://github.com/gtkChop/covidviz/blob/master/README.md",
                        target="_blank",
                        className="navbar-brand btn btn-outline-info btn-sm"
                    ),
                    html.A(
                        "About",
                        href="https://github.com/gtkChop/covidviz/blob/master/README.md",
                        target="_blank",
                        className="navbar-brand btn btn-outline-info btn-sm"
                    )
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
