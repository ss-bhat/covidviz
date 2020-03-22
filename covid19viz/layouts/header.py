import dash_html_components as html


header = html.Header(
    children=[
        html.Img(
            src="/assets/img/virus2.png",
            className="logo"
        ),
        html.H3(
            children="Covid-19 Outbreak Stats",
            className="logo-text"
        )
    ],
    id="nav-panel",
    className="navbar navbar-light"
)
