import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px


def donut_by_species(dfo, months):
    fig = go.Figure()
    # Add all traces.
    # Build dataset
    cols = ['Frog','Koi']
    index=months
    df = pd.DataFrame(columns=cols)
    df['Months'] = months
    df['Frog'] = 0
    df['Koi'] = 1
    df['Frog'][df['Months'].isin(['May','Jun','Jul','Aug'])] = 1
    #print(df.head(20))
    dfd = pd.DataFrame(columns=['Name','slices', 'increments'])
    print(dfo.head())
    for idx, col in enumerate(cols, 0):
        print(idx)
        print(col)
        pie_slices=df.iloc[:,idx].tolist()
        count_pre0 = 0
        count1 = 0
        count_post0 = 0
        for m in pie_slices:
            if count1 > 0:
                if m == 1:
                    count1+=1
                else:
                    count_post0+=1
            else:
                if m == 1:
                    count1+=1
                else:
                    count_pre0+=1
        my_list = [count_pre0, count1, count_post0]
        dfd.loc[idx] = [col, my_list, dfo.loc[dfo['Name'] == col]['increments'].item()]


    print(dfd.head())

    for index, row in dfd.iterrows():
        print(row['slices'])
        print(row['Name'])

        fig.add_trace(
            go.Pie(
                values=row['slices'],
                labels=[' ',row['Name'],'  '],
                domain={'x':[0,1], 'y':[0, 1]}, # change these for outer dimensions
                hole=row['increments'],
                direction='clockwise',
                sort=False,
                marker={'colors':['#FFFFFF','#5DADE2','#FFFFFF']},
                showlegend=True))
        pyo.plot(fig, filename='iter_test.html')


    #print([next(c[n]) for n in x])
        #fig.add_trace(go.Scatter(x = anz_d_df.index , y = anz_d_df.iloc[:,idx], mode ='lines', name = col))
    #pyo.plot(fig, filename='iter_test.html')
    return

def donut_example(df):
    data = [
        # Portfolio (inner donut)
        go.Pie(values=[4,4,4],
        labels=[' ','Frog','  '],
        #textinfo='label',
        domain={'x':[0,1], 'y':[0, 1]}, # change these for outer dimensions
        hole=0.4,
        direction='clockwise',
        sort=False,
        marker={'colors':['#FFFFFF','#5DADE2','#FFFFFF']},
        showlegend=True),

        go.Pie(values=[0,1,0],
        labels=[' ','Koi','  '],
        #textinfo='label',
        domain={'x':[0,1], 'y':[0, 1]}, # change these for outer dimensions
        hole=0.6,
        direction='clockwise',
        sort=False,
        marker={'colors':['#FFFFFF','#F1948A','#FFFFFF']},
        showlegend=True),

        # Individual components (outer donut)
        go.Pie(values=[1,1,1,1],
        labels=['january','Light Red','Medium Blue','Light Blue'],
        textinfo='label',
        domain={'x':[0,1], 'y':[0,1]},
        hole=0.9,
        direction='clockwise',
        sort=False,
        marker={'colors':['#EC7063','#F1948A','#5DADE2','#FFFFFF']},
        showlegend=False)]

    fig = go.Figure(data=data, layout={'title':'Nested Pie Chart'})
    pyo.plot(fig, filename='donut_test.html')
    return



def iter_example(df):
    fig = go.Figure()
    # Add all traces.
    # Build dataset
    cols = ['Australian Capital Territory',
        'New South Wales',
        'Northern Territory',
        'Queensland',
        'South Australia',
        'Tasmania',
        'Victoria',
        'Western Australia',
        'New Zealand']
    index = pd.date_range(start='2020-01-22', periods=10)
    anz_d_df = pd.DataFrame(0,columns=cols, index=index)
    anz_d_df['Tasmania'] = 1
    anz_d_df['Queensland'] = 5
    print(anz_d_df.head(20))

    for idx, col in enumerate(anz_d_df.columns, 0):
        fig.add_trace(go.Scatter(x = anz_d_df.index , y = anz_d_df.iloc[:,idx], mode ='lines', name = col))
    pyo.plot(fig, filename='iter_test.html')
    return


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
