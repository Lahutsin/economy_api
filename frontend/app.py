import dash
from dash import dcc, html
import requests
import os
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

API_URL = os.getenv("API_URL", "http://api:8000")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H3("Settings", className="sidebar-title"),

        html.Label("Data Source"),
        dcc.Dropdown(
            id="provider-dropdown",
            options=[
                {"label": "World Bank", "value": "world_bank"},
                {"label": "IMF", "value": "imf"}
            ],
            value="world_bank",
            clearable=False
        ),

        html.Label("Country"),
        dcc.Dropdown(
            id="country-dropdown",
            options=[
                {"label": "USA", "value": "US"},
                {"label": "France", "value": "FR"}
            ],
            value="US",
            clearable=False
        ),

        html.Label("Indicator"),
        dcc.Dropdown(
            id="indicator-dropdown",
            options=[
                {"label": "GDP", "value": "NY.GDP.MKTP.CD"},
                {"label": "Inflation", "value": "FP.CPI.TOTL.ZG"}
            ],
            value="NY.GDP.MKTP.CD",
            clearable=False
        ),

        html.Label("Period"),
        dcc.RangeSlider(
            id="year-slider",
            min=2000, max=2023, step=1,
            marks={year: str(year) for year in range(2000, 2024, 3)},
            value=[2010, 2023]
        ),

        html.Button("Update", id="update-button", n_clicks=0, className="update-btn")
    ], className="sidebar"),

    html.Div([
        html.H3("Economic Data", className="chart-title"),
        dcc.Graph(id="economy-chart"),
    ], className="content")
], className="container")

@app.callback(
    Output("economy-chart", "figure"),
    [
        Input("update-button", "n_clicks"),
        Input("provider-dropdown", "value"),
        Input("country-dropdown", "value"),
        Input("indicator-dropdown", "value"),
        Input("year-slider", "value"),
    ]
)
def update_chart(n_clicks, provider, country, indicator, year_range):
    if not country:
        return px.line(title="Enter a country code")

    response = requests.get(f"{API_URL}/economy/{country}/{indicator}")
    if response.status_code != 200:
        return px.line(title="Error loading data")

    data = response.json().get("World Bank", [])
    df = pd.DataFrame(data)
    
    if df.empty:
        return px.line(title="No data available")

    df = df[(df["date"].astype(int) >= year_range[0]) & (df["date"].astype(int) <= year_range[1])]
    df["date"] = df["date"].astype(str)
    df = df.sort_values(by="date", ascending=True)

    fig = px.line(df, x="date", y="value", title=f"{indicator} for {country}", markers=True)
    fig.update_layout(xaxis_title="Year", yaxis_title="Value", template="plotly_white")

    return fig


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
