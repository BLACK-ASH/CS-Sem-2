from threading import *
from time import sleep

def thread1():
    for i in range(5):
        print("This Is Non-Daemon Thread")
        sleep(2)

T = Thread(target = thread1)
T.start()
sleep(5)
print("Main Thread Execution")
