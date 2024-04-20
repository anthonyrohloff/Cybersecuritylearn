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
                        html.Br(),
                        html.H2("About Me", style={"text-decoration": "underline"}),
                        html.Div(
                            "Hello!"
                        ),
                        html.Br(),
                        html.Div(
                            "My name is Anthony Rohloff, and I am a cybersecurity engineering student at the University of Cincinnati. I have minors in computer science, business administration, and embedded systems. My studies are at the intersection of electrical engineering, computer engineering, and computer science."
                        ),
                        html.Br(),
                        html.Div("Outside of school, I have also furthered my knowledge in the field of cybersecurity by earning two certifications. First, I earned SC-900, Microsoft Security, Identity, and Compliance Fundamentals. This certification helped me cement a strong foundation for essential cybersecurity concepts, as well as teach me about Microsoft-specific technologies such as Microsoft Entra and Sentinel. After that, I can proudly say I studied, took, and passed CompTIA Security+ SY0-701 on the first attempt. This certification is a highly popular certification for those trying to break into the industry due to its wide scope and application-oriented questions."),
                        html.Br(),
                        html.Div(
                            "Additionally, I have experience as a controls engineering intern at BMW Manufacturing Co. in Spartanburg, South Carolina. In my department, I have had the opportunity to complete over 100 hours of professional development training, as well as work on technically-involved projects. These trainings and projects included topics such as Splunk, Profinet, Python, Power BI, and Agile work methodology."
                        ),
                        html.Br(),
                        html.Div([
                            "Please feel free to connect with me on ",
                            html.A(
                                [html.I(className="fa-brands fa-linkedin"), "LinkedIn"],
                                href='https://www.linkedin.com/in/anthonyrohloff/',
                                target="_blank"
                            ),
                            " for more detailed and updated information about my education, professional experiences, and projects."
                        ]),
                        html.Img(src='assets/images/headshot.JPG', style={'width': '25%', 'height': '25%', 'float': 'right'})
                    ]
                )
            ]
        )
    ]
)
