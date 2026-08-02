# join 方法的作用：阻塞当前进程，等join前面的进程执行完，在继续往下执行
# join(timeout),其中 timeout是可选参数，表示等多久，单位是秒
import os
import time
from multiprocessing import Process
print(100,__name__)

def speak():
    for index in range(10):
        print(f"我在说话{index},进程是pid:{os.getgid()},我的的父进程是:{os.getpid()}")
        time.sleep(1)

def study():

    for index in range(15):
        print(f"我在学习{index},进程是pid:{os.getgid()},我的的父进程是:{os.getpid()}")
        time.sleep(1)

if __name__ == '__main__':
    print("我是主进程中的【第一行】打印")
    p1 = Process(target=speak)
    p2 = Process(target=study)
    p1.start()
    p1.join(5)
    p2.start()
    # p1.join()
    # p2.join()
    print("我是主进程中的【最后一行】打印")
