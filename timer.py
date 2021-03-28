import sched
import time
import datetime

class timer():
    def __init__(self = 0):
        self.a = 1
        

    
    def delete_remind(id_sched):
        scheduler.cancel(id_sched)


    def get_list_remind():
        return scheduler.queue

    def create_remind(date):
        scheduler = sched.scheduler(time.time,
                                time.sleep)
        remind_ = scheduler.enterabs(date,
                             send_remind, 
                                argument = ("Событие произошло"))
        run_reminder(remind_)
        
    def create_loop_remind(time_loop):
        scheduler = sched.scheduler(time.time,
                                time.sleep)
        scheduler.every(time_loop).second.do(send_remind)

    # function to print time and
    # message of the event 
    def send_remind(message):
        print('EVENT:', time.time(), message)

        # printing starting time
        print ('START:', time.time())

        # event x with delay of 1 second
        # enters queue using enterabs method

        # e_x = scheduler.enterabs(time.time()+1, 1,
        #                      send_remind, 
        #                         argument = ("Event X", ))
        
        # executing the events
        
    def run_reminder(id_remind):
        scheduler.run(id_remind)

# Преобразование времени в секундах в дату.
    # datetime.datetime.fromtimestamp(time.time())

# Обратное преобразование
    # dt.timestamp()

# Повторное выполнение каждые 10 минут
    # schedule.every(10).minutes.do(job)

# Возвращает список предстоящих событий
    # scheduler.queue

# Возвращает true если очередь событий пуста 
    #scheduler.empty() 

    #scheduler.cancel()  
# удаляет событие из очереди. 
# Если событие не является событием, находящимся в данный момент в очереди,
# этот метод вызовет a ValueError.

# Добавляет событие в список
# scheduler.enterabs(time.time()+1, 1,
                            # send_remind, 
                            # argument = ("Event X", ))