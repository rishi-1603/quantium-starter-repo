import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv("formatted_output.csv")
df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)

app.layout = html.Div(
    style={"padding": "20px", "fontFamily": "Arial"},
    children=[
        html.H1(
            "Pink Morsels Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#2c3e50"
            }
        ),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "East", "value": "east"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={"marginBottom": "20px"}
        ),

        dcc.Graph(id="sales-graph")
    ]
)

@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(region):

    if region == "all":
        filtered = df
    else:
        filtered = df[df["region"].str.lower() == region]

    filtered = filtered.sort_values("date")

    fig = px.line(
        filtered,
        x="date",
        y="sales",
        title=f"Sales - {region.title()}"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)