import pandas as pd


class ProphetTools:

    '''(Pdb) df['open'].reset_index().rename(columns={'index':'ds', 'open':'y'})'''

    @staticmethod
    def prophetify(dataframe, series_name):
        return dataframe[series_name].reset_index().rename(columns={'index':'ds', series_name:'y'})