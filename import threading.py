import threading
import time


def class_start():
    time.sleep(30)
    print("you enter the class at 4 pm")
    
def snacks_time():
    time.sleep(20)
    print("you took the snack at 4:15")

    
def task_run():
    time.sleep(22)
    print("complete it at 4:30")
    
def photoshoot():
    time.sleep(17)
    print("take photo at 5pm")

def task_show():
    time.sleep(15)
    print("show the task at 5:15 pm") 

def class_end():
    time.sleep(25)
    print("end the class at 5:30 pm")
        
#class_start()
#snacks_time()
#task_run()
#photoshoot()
#task_show()
#class_end()




task1=threading.Thread(target=class_start)
task2=threading.Thread(target=snacks_time)
task3=threading.Thread(target=task_run)
task4=threading.Thread(target=photoshoot)
task5=threading.Thread(target=task_show)
task6=threading.Thread(target=class_end)


task1.start()
task2.start()
task3.start()
task4.start()
task5.start()
task6.start()


task1.join()
task2.join()
task3.join()
task4.join()
task5.join()
task6.join()

print("All task completed")










