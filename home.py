from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.MATERIA, dbc.icons.FONT_AWESOME],
)

sidebar = html.Div(
    [
        html.Div(
            [
                html.H2("Navigation", style={"color": "#BFCBCE"}),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
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

app.layout = html.Div(
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
                        html.H1("About", style={"text-decoration": "underline"}),
                        html.Div(
                            '''
                            This website will teach you about cybersecurity.
                            '''
                        )
                    ]
                )
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
