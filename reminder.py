import csv
import pandas as pd
import os 
import json
import datetime as dt

path_table_reminder = r'C:\Users\Rikky\telegram_bot\reminder_bot\table_reminder.json'

def create_json_table(list_name_column):
    return 1

def reader_json():
    df = pd.read_json(path_table_reminder)
    return df

def writer_json(df):
    df.to_json(r'C:\Users\Rikky\telegram_bot\reminder_bot\table_reminder3.json')
    print(df)

def rewrite_csv(df):
    if os.path.isfile(path_table_reminder): 
        os.remove(path_table_reminder) 
        print("success") 
    else: print("File doesn't exists!")
    writer_json(df)

def transform_df(df):
    df.loc[1, 'column1'] = 'test'
    return df

if __name__ =='__main__':
    df=reader_json()
    # df=transform_df(df)
    # writer_json(df)
    print(df)
    print(dt.datetime.now())
    
    