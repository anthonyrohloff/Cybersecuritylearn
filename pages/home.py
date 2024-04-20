from dash import html
import dash_bootstrap_components as dbc

sidebar = html.Div(
    [
        html.Div(
            [
                html.H2("Navigation", style={"color": "#BFCBCE"}),
            ],
            className="sidebar-header",
        ),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div([
                            html.I(className="fas fa-home me-2"),
                            html.Span("Home", style={"color": "#BFCBCE", "verticalAlign": "middle"})
                        ], className="d-flex align-items-center")
                    ],
                    href="/",
                    active="exact",
                    className="nav-link",
                ),
                html.Br(),
                dbc.NavLink(
                    [
                        html.Div([
                            html.I(className="fas fa-user me-2"),
                            html.Span("About", style={"color": "#BFCBCE", "verticalAlign": "middle"})
                        ], className="d-flex align-items-center")
                    ],
                    href="/about",
                    active="exact",
                    className="nav-link",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)

layout = html.Div(
    [
        sidebar,
        html.Div(
            className="content",
            children=[
                html.Div(
                    className="app-header",
                    children=[
                        html.Div('Cybersecuritylearn', className="app-header--title")
                    ]
                ),
                html.Div(
                    className="app-body",
                    children=[
                        html.H1("Home", style={"text-decoration": "underline"}),
                        html.Div(
                            '''
                            Welcome to the home page.
                            '''
                        )
                    ]
                )
            ]
        )
    ]
)
