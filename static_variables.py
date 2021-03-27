class static_variables:
    # def __init__(self, path_table_reminder, json_start):
    #     self.path_table_reminder = r'C:\Users\Rikky\telegram_bot\reminder_bot\table_reminder4.json'
    #     self.json_start = {
    #                         "date":{"0":"2021-03-27",
    #                             "1":"2021-03-27",
    #                             "2":"2021-03-27",
    #                             "3":"2021-03-27"},
    #                         "message":{"0":"buy milk",
    #                             "1":"standup",
    #                             "2":"go drink coffe",
    #                             "3":"sleep"},
    #                         "repeat":{"0":"year",
    #                             "1":"month",
    #                             "2":"week",
    #                             "3":"one"}
    #                         }

    def path_table_reminder():
        return r'C:\Users\Rikky\telegram_bot\reminder_bot\table_reminder4.json'
    
    def json_start(): 
        return {
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