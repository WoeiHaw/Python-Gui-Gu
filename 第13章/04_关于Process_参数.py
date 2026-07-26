import os
import time
from multiprocessing import Process,current_process
print(100,__name__)

def speak(a,b,msg):
    for index in range(10):
        print(f"{msg}--{a}--{b}--{current_process().name}--我在说话{index},进程是pid:{os.getgid()},我的的父进程是:{os.getpid()}")
        time.sleep(1)

def study():

    for index in range(15):
        print(f"我在学习{index},进程是pid:{os.getgid()},我的的父进程是:{os.getpid()}")
        time.sleep(1)

if __name__ == '__main__':
    print(os.getpid())
    p1 = Process(target=speak,name="说话进程",args=(666,888),kwargs={"msg":"尚硅谷"})
    p2 = Process(target=study)
    print(p1.name)
    print(p2.name)

    p1.start()
    p2.start()
