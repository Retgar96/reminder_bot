import pandas as pd
import datetime 

class transform_df():

    def __init__(self = 0):
        self.a = 0

    def transform_df_(self,df):
        df.loc[1, 'column1'] = 'test'
        return df

    def add_row(self,df, date, message, repeat):
        df2 = pd.DataFrame({"date": [date], "message": [message], "repeat": [repeat]})
        df.append(df2)
        return df

    def delet_row(self,df,id):
        df.drop([id],inplace=True)
        df.reset_index(inplace=True)
        return df

    def test(self,a,b):
        return a+b