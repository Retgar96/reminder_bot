import csv
import pandas as pd
import os 
import json
import datetime as dt
import asyncore
from transform import transform_df
import time
import datetime
from timer import timer

path_table_reminder = r'C:\Users\Rikky\telegram_bot\reminder_bot\table_reminder.json'
json_start = {
                "date":{"0":"2021-03-27",
                    "1":"2021-03-27",
                    "2":"2021-03-27",
                    "3":"2021-03-27"},
                "message":{"0":"buy milk",
                    "1":"standup",
                    "2":"go drink coffe",
                    "3":"sleep"},
                "repeat":{"0":"year",
                    "1":"month",
                    "2":"week",
                    "3":"one"}
                }


def create_json_table():


    df = pd.DataFrame.from_dict(json_start)

    if os.path.isfile(path_table_reminder): 
        print("success") 
    else: print("File doesn't exists!")
    writer_json(df)

def reader_json():
    df = pd.read_json(path_table_reminder)
    return df

def writer_json(df):
    df.to_json(path_table_reminder)
    # print(df)

def rewrite_csv(df):
    if os.path.isfile(path_table_reminder): 
        os.remove(path_table_reminder) 
        print("success") 
    else: print("File doesn't exists!")
    writer_json(df)

def transform_df_(df):
    df.loc[1, 'column1'] = 'test'
    return df

if __name__ =='__main__':
    # df=reader_json()
    # df=transform_df(df)
    # writer_json(df)
    # print(df)
    # print(dt.datetime.now())
    # create_json_table()
    # df = reader_json()
    # trans = transform_df()
    # df = trans.delet_row(df,3)
    # tes = trans.test(4,3)
    # print(datetime.datetime.fromtimestamp(time.time()))
    
# datetime.datetime(2020, 5, 6, 13, 52, 5)
    timer.create_loop_remind(5)
# дальше работаем как с объектом 
# получаем строку 
# >>> dt.strfptint('%d.%m.%Y %H:%M')