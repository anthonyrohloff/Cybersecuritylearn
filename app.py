from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from pages.home import layout as home_layout
from pages.about import layout as about_layout

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.MATERIA, dbc.icons.FONT_AWESOME, 'assets/sidebar.css', 'assets/body.css', 'assets/header.css', 'assets/typography.css'],
    use_pages=True
)

app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ]
)

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/':
        return home_layout
    elif pathname == '/about':
        return about_layout
    else:
        return 'Page not found'

if __name__ == '__main__':
    app.run_server(debug=True)
