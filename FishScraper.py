import numpy as np
import pandas as pd
import plot_utils
import logging
logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.DEBUG)

class FishScraper:

    target_url = 'https://animalcrossing.fandom.com/wiki/Fish_(New_Horizons)'
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    def __init__(self, script_params):
        self.params = script_params

    def _extract(self):
        logging.info('Data Scrape')
        df_list = pd.read_html(self.target_url)
        return df_list

    def encode_checks_dashes(self, df):
        for month in self.months:
            df[month] = df[month].astype(str).str.replace(u"\u2713", 'True').replace({"-":'False'})
        return df

    def donut_prep(self, df):
        logging.info('Plotting Donut')
        #df.reset_index(drop=True, inplace=True)
        logging.debug('Donut Dataframe Head \n\n {}'.format(df.head(20).to_string()))
        #df = pd.pivot_table(df, columns='Name')
        #df.index = df.index.set_names(['Attributes'])
        #df.reset_index(inplace=True)
        #df = df.reindex([4,3,7,0,8,6,5,1,12,10,9,2,11,13,14])
        print(df)
        #print(pd.__version__)
        #print(df.sortlevel(["A","B"], ascending= [False,True], sort_remaining=False, inplace=True))
        #df["Attributes"] = df["Attributes"].astype('category', categories=self.months.extend(['Price','increments']))
        #plot_utils.donut_example(df)
        plot_utils.donut_by_species(df, self.months)
        return 0

    def plot_by_location(self, df):
        df = df[df['Location'] == self.params['Location']]
        df.reset_index(inplace=True)
        rad_incs = pd.Series(range(1,df['Name'].count()+1))
        df['increments']=1 - (0.05 * rad_incs)
        logging.debug('Encoded Dataframe Head \n\n {}'.format(df.head(20).to_string()))
        for my_col in self.months:
            #df[my_col] = np.where((df[my_col] == 'True'),df['increments'],np.nan)
            df[my_col] = np.where((df[my_col] == 'True'),1.0, 0.0)
        logging.debug('Encoded Dataframe Head \n\n {}'.format(df.head(20).to_string()))
        df_sample = df[df['Name'].isin(['Koi','Frog'])]
        #plot_utils.bar_price(df)
        self.donut_prep(df_sample)

        #plot_utils.radial_year(df, self.months)
        m=df[df['Name'] == "Koi"][self.months].values.flatten().tolist().append(df[df['Name'] == 'Koi'].loc[:,'Jan'].values[0])
        #m.append(df[df['Name'] == 'Koi'].loc[:,'Jan'].values[0])
        print(m)
        #print(df[df['Name'] == 'Koi'].loc[:,'Jan'].values[0])
        #prices = df.loc[:,'Price'].values
        #times = df.loc[:,'Time'].values
        #customdata = np.dstack((prices, times))
        #print(customdata[0][0][0])
        #print(customdata[0][0][1])
        #print(df.index[df['Name'] == "Catfish"][0])
        #print(np.dstack((prices, times))[0][df.index[df['Name'] == "Catfish"][0]][0])
        #print(np.dstack((prices, times))[0][df.index[df['Name'] == "Catfish"][0]][1])

        #for name in df['Name']:
        #    print(df[df['Name'] == name][self.months].values.flatten().tolist())

        #z1, z2, z3 = np.random.random((3,7,7))
        #print(z1)
        # count True/Falses and plot abundance by month
        # then go for it with the donut plot!!
        return 0

    def df_info(self, df):
        print("== Fish Count ==\n")
        print("River: {}".format(df['Location'][df['Location'] == 'River'].count()))
        print("Pond: {}".format(df['Location'][df['Location'] == 'Pond'].count()))
        print("Sea: {}".format(df['Location'][df['Location'] == 'Sea'].count()))
        return 0

    def _transform(self, df_list):
        if self.params['hemisphere'] == 'north':
            df = df_list[2]
        else:
            df = df_list[4]
        logging.debug('Raw Dataframe Head \n {}'.format(df.head().to_string()))
        df = self.encode_checks_dashes(df)
        logging.debug('Encoded Dataframe Head \n {}'.format(df.head().to_string()))
        self.df_info(df)
        df.drop(['Image'], axis=1, inplace=True)
        logging.info('Plotting by location')
        self.plot_by_location(df)
        return df

    def generate(self):
        df_list = self._extract()
        df = self._transform(df_list)
        return df
