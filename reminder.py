
import pandas as pd
import os 
import json
import datetime as dt
import asyncore
from transform import transform_df
from reader_json import reader_json

if __name__ =='__main__':

    rdjson = reader_json()
    rdjson.create_json_table()
    df = rdjson.read_json()
    print(df)
    # tfdf = transform_df()
    # df = 




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

# дальше работаем как с объектом 
# получаем строку 
# >>> dt.strfptint('%d.%m.%Y %H:%M')