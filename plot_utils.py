import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

def donut_by_species(df):
    pass

def bar_price(df):
    data = [go.Bar(
        x=df['Name'],
        y=df['Price']
    )]
    layout = go.Layout(
        title='Fish Prices'
    )
    fig = go.Figure(data=data, layout=layout)
    pyo.plot(fig, filename='fish_prices.html')

def bar_abundance(df):

    data = [go.Bar(
        x=df['Name'],
        y=df['Price']
    )]
    layout = go.Layout(
        title='Fish Prices'
    )
    fig = go.Figure(data=data, layout=layout)
    pyo.plot(fig, filename='fish_prices.html')

def radial_year(df, months):


    trace1 = go.Scatterpolar(
        #r = [np.nan,4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,np.nan,np.nan],
        r = df[df['Name'] == "Catfish"][months].values.flatten().tolist(),
        theta  = months,
        mode='lines',
        line=dict(
            shape='spline',
            smoothing=1,
            width=10
        ),
        name='Catfish'
    )

    trace2 = go.Scatterpolar(
        #r = [np.nan,4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,np.nan,np.nan],
        r = df[df['Name'] == "Gar"][months].values.flatten().tolist(),
        theta  = months,
        mode='lines',
        line=dict(
            shape='spline',
            smoothing=1,
            width=10
        ),
        name='Gar'
    )

    data = [trace1, trace2]
    fig = go.Figure(data=data)
    pyo.plot(fig, filename='radial_test.html')
