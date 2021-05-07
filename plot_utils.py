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
    names = df.loc[:,'Name'].values
    prices = df.loc[:,'Price'].values
    times = df.loc[:,'Time'].values

    trace1 = go.Scatterpolar(
        #r = [np.nan,4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,np.nan,np.nan],
        r = df[df['Name'] == "Catfish"][months].values.flatten().tolist(),
        theta  = months,
        mode='lines',
        line=dict(shape='spline',smoothing=1.3,width=20),
        name='Catfish',
        meta = np.dstack((prices, times))[0][df.index[df['Name'] == "Catfish"][0]],
        hovertemplate="<b>Price: $%{meta[0]} </b><br><b>Times: %{meta[1]} </b><br>"
    )
    trace2 = go.Scatterpolar(
        r = df[df['Name'] == "Gar"][months].values.flatten().tolist(),
        theta  = months,
        mode='lines',
        line=dict(shape='spline',smoothing=1.3,width=20),
        name='Gar',
        meta = np.dstack((names,prices, times))[0][df.index[df['Name'] == "Gar"][0]],
        hovertemplate="<b>Price: $%{meta[1]} </b><br><b>Times: %{meta[2]} </b><br>"
    )
    trace3 = go.Scatterpolar(
        #r = [np.nan,4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,np.nan,np.nan],
        r = df[df['Name'] == "Carp"][months].values.flatten().tolist(),
        theta  = months,
        mode='lines',
        line=dict(shape='spline',smoothing=1.3,width=20),
        name='Carp',
        meta = np.dstack((prices, times))[0][df.index[df['Name'] == "Carp"][0]],
        hovertemplate="<b>Price: $%{meta[0]} </b><br><b>Times: %{meta[1]} </b><br>"
    )
    trace4 = go.Scatterpolar(
        #r = [np.nan,4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,np.nan,np.nan],
        r = df[df['Name'] == "Giant snakehead"][months].values.flatten().tolist(),
        theta  = months,
        mode='lines',
        line=dict(shape='spline',smoothing=1.3,width=20),
        name='Giant snakehead',
        meta = np.dstack((prices, times))[0][df.index[df['Name'] == "Giant snakehead"][0]],
        hovertemplate="<b>Price: $%{meta[0]} </b><br><b>Times: %{meta[1]} </b><br>"
    )
    trace5 = go.Scatterpolar(
        #r = [np.nan,4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,np.nan,np.nan],
        r = df[df['Name'] == "Frog"][months].values.flatten().tolist(),
        theta  = months,
        mode='lines',
        line=dict(shape='spline',smoothing=1.3,width=20),
        name='Frog',
        meta = np.dstack((prices, times))[0][df.index[df['Name'] == "Frog"][0]],
        hovertemplate="<b>Price: $%{meta[0]} </b><br><b>Times: %{meta[1]} </b><br>"
    )
    trace6 = go.Scatterpolar(
        #r = [np.nan,4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,np.nan,np.nan],
        r = df[df['Name'] == "Tadpole"][months].values.flatten().tolist(),
        theta  = months,
        mode='lines',
        line=dict(shape='spline',smoothing=1.3,width=20),
        name='Tadpole',
        meta = np.dstack((prices, times))[0][df.index[df['Name'] == "Tadpole"][0]],
        hovertemplate="<b>Price: $%{meta[0]} </b><br><b>Times: %{meta[1]} </b><br>"
    )
    trace7 = go.Scatterpolar(
        #r = [np.nan,4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,np.nan,np.nan],
        r = df[df['Name'] == "Crawfish"][months].values.flatten().tolist(),
        theta  = months,
        mode='lines',
        line=dict(shape='spline',smoothing=1.3,width=20),
        name='Crawfish',
        meta = np.dstack((prices, times))[0][df.index[df['Name'] == "Crawfish"][0]],
        hovertemplate="<b>Price: $%{meta[0]} </b><br><b>Times: %{meta[1]} </b><br>"
    )
    trace8 = go.Scatterpolar(
        #r = [np.nan,4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,np.nan,np.nan],
        r = df[df['Name'] == "Killifish"][months].values.flatten().tolist(),
        theta  = months,
        mode='lines',
        line=dict(shape='spline',smoothing=1.3,width=20),
        name='Killifish',
        meta = np.dstack((prices, times))[0][df.index[df['Name'] == "Killifish"][0]],
        hovertemplate="<b>Price: $%{meta[0]} </b><br><b>Times: %{meta[1]} </b><br>"
    )
    trace9 = go.Scatterpolar(
        #r = [np.nan,4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,np.nan,np.nan],
        r = df[df['Name'] == "Ranchu goldfish"][months].values.flatten().tolist(),
        theta  = months,
        mode='lines',
        line=dict(shape='spline',smoothing=1.3,width=20),
        name='Ranchu goldfish',
        meta = np.dstack((prices, times))[0][df.index[df['Name'] == "Ranchu goldfish"][0]],
        hovertemplate="<b>Price: $%{meta[0]} </b><br><b>Times: %{meta[1]} </b><br>"
    )
    trace10 = go.Scatterpolar(
        #r = [np.nan,4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,np.nan,np.nan],
        r = df[df['Name'] == "Pop-eyed goldfish"][months].values.flatten().tolist(),
        theta  = months,
        mode='lines',
        line=dict(shape='spline',smoothing=1.3,width=20),
        name='Pop-eyed goldfish',
        meta = np.dstack((prices, times))[0][df.index[df['Name'] == "Pop-eyed goldfish"][0]],
        hovertemplate="<b>Price: $%{meta[0]} </b><br><b>Times: %{meta[1]} </b><br>"
    )
    trace11 = go.Scatterpolar(
        #r = [np.nan,4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,np.nan,np.nan],
        r = df[df['Name'] == "Goldfish"][months].values.flatten().tolist(),
        theta  = months,
        mode='lines',
        line=dict(shape='spline',smoothing=1.3,width=20),
        name='Goldfish',
        meta = np.dstack((prices, times))[0][df.index[df['Name'] == "Goldfish"][0]],
        hovertemplate="<b>Price: $%{meta[0]} </b><br><b>Times: %{meta[1]} </b><br>"
    )
    trace12 = go.Scatterpolar(
        #r = [np.nan,4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,np.nan,np.nan],
        r = df[df['Name'] == "Koi"][months].values.flatten().tolist(),
        theta  = months,
        mode='lines',
        line=dict(shape='spline',smoothing=1.3,width=20),
        name='Koi',
        connectgaps=True,
        meta = np.dstack((prices, times))[0][df.index[df['Name'] == "Koi"][0]],
        hovertemplate="<b>Price: $%{meta[0]} </b><br><b>Times: %{meta[1]} </b><br>"
    )
    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12]
    fig = go.Figure(data=data,
        layout=go.Layout(title=go.layout.Title(text='Animal Crossing New Horizons: Availability of Fish in Ponds (Northern Hemisphere)')))
    pyo.plot(fig, filename='radial_test.html')
