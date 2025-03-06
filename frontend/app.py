import dash
from dash import dcc, html
import os
import requests

API_URL = os.getenv("API_URL", "http://api:8000")

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='country-input', type='text', placeholder='Enter Country'),
    html.Div(id='output')
])

@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('country-input', 'value')]
)
def update_output(country):
    if country:
        response = requests.get(f'{API_URL}/economy/{country}')
        data = response.json()
        return html.Div([
            html.H3(f"Economy Data for {country}"),
            html.P(f"IMF Data: {data['IMF']}"),
            html.P(f"World Bank Data: {data['World Bank']}"),
        ])
    return "Enter a country to get economy data"

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
