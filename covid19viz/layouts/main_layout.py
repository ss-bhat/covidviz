import dash_html_components as html
import logging

log = logging.getLogger(__name__)


def create_dash_layout(header, children, footer=None):
    """
    Create a dash layout
    :param header: header dash element
    :param children: children dash element
    :param footer: footer dash element
    :return: dict
    """

    # Create layout
    log.info("Creating layout")
    layout = html.Div([
        header,
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

    return layout
