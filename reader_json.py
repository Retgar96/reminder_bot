import pandas as pd
import os 
import json
import datetime as dt


class reader_json():
    def __init__(self):
        self.path_table_reminder = r'C:\Users\Rikky\telegram_bot\reminder_bot\table_reminder.json'
        self.json_start = {
                            "id_user_1":{
                                
                                "remind_1":{
                                "time":"2020.03.04",
                                "message":"message_remind",
                                "type_remind":"loop_week"
                                },
                                "remind_2":{
                                "time":"2021.03.16",
                                "message":"message_remind",
                                "type_remind":"disposable"
                                },
                                "remind_3":{
                                "time":"2021.03.23",
                                "message":"message_remind",
                                "type_remind":"disposable"
                                }
                            },
                            "id_user_2":{
                                
                                "remind_1":{
                                "time":"2020.03.04",
                                "message":"message_remind",
                                "type_remind":"disposable"
                                },
                                "remind_2":{
                                "time":"2021.03.16",
                                "message":"message_remind",
                                "type_remind":"disposable"
                                },
                                "remind_3":{
                                "time":"2021.03.23",
                                "message":"message_remind",
                                "type_remind":"loop_day"
                                }
                            }
                        }

    def create_json_table(self):

        df = pd.DataFrame.from_dict(self.json_start)

        if os.path.isfile(self.path_table_reminder): 
            print("File exist") 
        else:
            print("File doesn't exists") 
            df.to_json(self.path_table_reminder)
            print("success") 
            
        

    def read_json(self):
        df = pd.read_json(self.path_table_reminder)
        return df

    def write_json(self,df):
        df.to_json(self.path_table_reminder)

    def rewrite_csv(self,df):
        if os.path.isfile(self.path_table_reminder): 
            os.remove(self.path_table_reminder) 
            print("success") 
        else: print("File doesn't exists!")
        writer_json(df)

    def get_list_remind(self,id):

        print('time')
