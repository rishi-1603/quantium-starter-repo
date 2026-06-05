import dash
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("My Dashboard", id="header"),

    dcc.Graph(id="visualization"),

    dcc.Dropdown(
        id="region-picker",
        options=[
            {"label": "North", "value": "north"},
            {"label": "South", "value": "south"}
        ],
        value="north"
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)