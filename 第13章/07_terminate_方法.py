import os
import time
from multiprocessing import Process

def speak():
    try:
        for index in range(10):
            print(f"我在说话{index},进程是pid:{os.getgid()},我的的父进程是:{os.getpid()}")
            time.sleep(1)
    #注意：使用terminate终止进程，不会引起finally执行
    finally:
        print("我是finally里的逻辑")


def study():

    for index in range(15):
        print(f"我在学习{index},进程是pid:{os.getgid()},我的的父进程是:{os.getpid()}")
        time.sleep(1)

if __name__ == '__main__':
    print("我是主进程中的【第一行】打印")

    print(os.getpid())
    p1 = Process(target=speak)
    p2 = Process(target=study)

    p1.start()
    p2.start()
    time.sleep(3)
    print("我是主进程，我准备强制终止p1进程。。。。。。")
    p1.terminate()
    p1.join()
    print(p1.is_alive())
    print("我是主进程中的【最后一行】打印")
