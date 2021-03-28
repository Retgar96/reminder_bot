import sched
import time
import datetime

class timer():
    def __init__(self = 0):
        self.a = 1
        scheduler = sched.scheduler(time.time,
                                time.sleep)

    
    def delete_remind():
        return 1
    # function to print time and
    # name of the event 
    def print_event(name):
        print('EVENT:', time.time(), name)

        # printing starting time
        print ('START:', time.time())

        # event x with delay of 1 second
        # enters queue using enterabs method
        e_x = scheduler.enterabs(time.time()+1, 1,
                                print_event, 
                                argument = ("Event X", ))
        
        # executing the events
        scheduler.run()


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
                            # print_event, 
                            # argument = ("Event X", ))