import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

def donut_by_species(df):
    pass

def bar_price(df):
    data = [go.Bar(
        x=df['Name'],  # NOC stands for National Olympic Committee
        y=df['Price']
    )]
    layout = go.Layout(
        title='Fish Prices'
    )
    fig = go.Figure(data=data, layout=layout)
    pyo.plot(fig, filename='fish_prices.html')
