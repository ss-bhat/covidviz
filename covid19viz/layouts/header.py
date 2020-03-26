import dash_html_components as html
from covid19viz.toolkit import config
from covid19viz.utils import helper as h

header = html.Header(
    children=[
        html.H3(
            children="{} - {}".format(config.get('dash.app_title'), h.get_last_updated_date(as_string=True)),
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
