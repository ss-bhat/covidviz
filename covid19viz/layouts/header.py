import dash_html_components as html
from covid19viz.toolkit import config


header = html.Header(
    children=[
        html.Img(
            src="/assets/img/virus2.png",
            className="logo"
        ),
        html.H3(
            children=config.get('dash.app_title'),
            className="logo-text",
            style={
                "color": config.get('dash.ui.text_color')
            }
        )
    ],
    id="nav-panel",
    className="navbar navbar-light",
    style={
        "background-color": config.get('dash.ui.header_background_color')
    }
)
