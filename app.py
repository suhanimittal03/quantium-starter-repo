from dash import Dash, html, dcc 
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('pink_morsels_sales_data.csv')
# print(df.head())

fig = px.line(df, x="date", y="sales", title="Sales Variation for pink morsel with time")
fig_reg = px.line(df, x="date", y="sales", color="region", title="Sales Variation for pink morsel with time")

app.layout = html.Div(children=[
    html.H1(children="Sales Data Graph"),

    html.Div(),
    
    dcc.Graph(
        id='sales-data graph',
        figure=fig
    ),

    html.H2(children="Sales Data with region"),
    dcc.Graph(
        id='sales-data graph with region',
        figure=fig_reg
    )
])

if __name__ == '__main__':
    app.run(debug=True)