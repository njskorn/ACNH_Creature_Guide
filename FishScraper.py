import pandas as pd
import plot_utils as putils

class FishScraper:

    target_url = 'https://animalcrossing.fandom.com/wiki/Fish_(New_Horizons)'
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    def __init__(self, script_params):
        self.params = script_params

    def _extract(self):
        df_list = pd.read_html(self.target_url)
        return df_list

    def encode_checks_dashes(self, df):
        for month in self.months:
            df[month] = df[month].astype(str).str.replace(u"\u2713", "True").replace({"-":"False"})
        return df

    def plot_by_location(self, df):
        df = df[df['Location'] == self.params['Location']]
        print(df.head(13))
        return 0

    def df_info(self, df):
        print("River: {}".format(df['Location'][df['Location'] == 'River'].count()))
        print("Pond: {}".format(df['Location'][df['Location'] == 'Pond'].count()))
        print("Sea: {}".format(df['Location'][df['Location'] == 'Sea'].count()))
        return 0

    def _transform(self, df_list):
        if self.params['hemisphere'] == 'north':
            df = df_list[2]
        else:
            df = df_list[4]
        print(df.head())
        df = self.encode_checks_dashes(df)
        self.df_info(df)
        print(df.head())
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
