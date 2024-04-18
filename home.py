from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.Div(
        className="app-header",
        children=[
            html.Div('Cybersecuritylearn', className="app-header--title")
        ]
    ),
    html.Div(
        children=html.Div([
            html.H1("About", 
                    style={"text-decoration": "underline"}),
            html.Div('''
                This website will teach you about cybersecurity.
            ''')
        ])
    )
])

if __name__ == '__main__':
    app.run(debug=True)