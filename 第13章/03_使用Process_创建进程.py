import os
import time
from multiprocessing import Process
print(100,__name__)

def speak():
    for index in range(10):
        print(f"我在说话{index},进程是pid:{os.getpid()},我的的父进程是:{os.getppid()}")
        time.sleep(1)

def study():

    for index in range(15):
        print(f"我在学习{index},进程是pid:{os.getpid()},我的的父进程是:{os.getppid()}")
        time.sleep(1)

if __name__ == '__main__':
    print(os.getpid())
    p1 = Process(target=speak)
    p2 = Process(target=study)

    p1.start()
    p2.start()


