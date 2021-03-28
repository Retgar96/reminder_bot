    # library imported
import sched
import time

class timer():
    def __init__(self = 0):
        self.a = 1

    # instance is created
    scheduler = sched.scheduler(time.time,
                                time.sleep)
                                
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
                            argument = ("Event X", ));
    
    # executing the events
    scheduler.run()