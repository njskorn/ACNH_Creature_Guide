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

    def plot_by_location(self, df):
        df = df[df['Location'] == self.params['Location']]
        df.reset_index(inplace=True)
        rad_incs = pd.Series(range(1,df['Name'].count()+1))
        df['increments']=rad_incs
        logging.debug('Encoded Dataframe Head \n\n {}'.format(df.head(20).to_string()))
        for my_col in self.months:
            df[my_col] = np.where((df[my_col] == 'True'),df['increments'],np.nan)
        logging.debug('Encoded Dataframe Head \n\n {}'.format(df.head(20).to_string()))

        plot_utils.radial_year(df, self.months)
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

params = {
    "hemisphere":"north",
    "Location":"Pond"
}
fish = FishScraper(params)
df = fish.generate()
