import os
import time
from multiprocessing import Process,Lock,RLock

def speak(lock):
    for index in range(10):
        lock.acquire()
        print("好好",end="")
        print(f"学习",end="")
        print(f"天天",end="")
        print(f"向上")
        lock.release()

        time.sleep(1)

def study(lock):

    for index in range(15):
        with lock:
            print("a", end="")
            print(f"b", end="")
            print(f"c", end="")
            print(f"d")
        time.sleep(1)

if __name__ == '__main__':
    lock = RLock()
    p1 = Process(target=speak,args=(lock,))
    p2 = Process(target=study,args=(lock,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()