import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import get_native_id, RLock

# def work(n,lock):
#     with lock:
#         print(f"work正在执行任务{n}.............{get_native_id()}")
#     time.sleep(1)
#
# if __name__ == "__main__":
#     print("---------------start---------------")
#     executor = ThreadPoolExecutor(3)
#     lock = RLock()
#     executor.submit(work,1,lock)
#     executor.submit(work,2,lock)
#     executor.submit(work,3,lock)
#     executor.submit(work,4,lock)
#     executor.submit(work,5,lock)
#     executor.submit(work,6,lock)
#     executor.submit(work,7,lock)
#     executor.shutdown(wait=True)
#     print("---------------end---------------")

# def work(n,lock):
#     with lock:
#         print(f"work正在执行任务{n}.............{get_native_id()}")
#     time.sleep(1)
#     return f"任务{n}的结果"
#
# if __name__ == "__main__":
#     print("---------------start---------------")
#     executor = ThreadPoolExecutor(3)
#     lock = RLock()
#     futures = [executor.submit(work,index,lock) for index in range(1,8)]
#
#     executor.shutdown(wait=True)
#     for f in futures:
#         print(f.result())
#     print("---------------end---------------")


# def work(n,lock):
#     with lock:
#         print(f"work正在执行任务{n}.............{get_native_id()}")
#     if n ==1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f"任务{n}的结果"
#
# if __name__ == "__main__":
#     print("---------------start---------------")
#     executor = ThreadPoolExecutor(3)
#     lock = RLock()
#     futures = [executor.submit(work,index,lock) for index in range(1,8)]
#     result_list = []
#
#     for f in as_completed(futures):
#         result_list.append(f.result())
#
#     executor.shutdown(wait=True)
#     print(result_list)
#
#     print("---------------end---------------")


# def work(n,lock):
#     with lock:
#         print(f"work正在执行任务{n}.............{get_native_id()}")
#     if n ==1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f"任务{n}的结果"
#
# if __name__ == "__main__":
#     print("---------------start---------------")
#     executor = ThreadPoolExecutor(3)
#     lock = RLock()
#     result_list = []
#
#     def done_func(f):
#         result_list.append(f.result())
#
#     for index in range(1,8):
#         f = executor.submit(work,index,lock)
#         f.add_done_callback(done_func)
#
#
#     executor.shutdown(wait=True)
#     print(result_list)
#
#     print("---------------end---------------")


# def work(n,lock):
#     with lock:
#         print(f"work正在执行任务{n}.............{get_native_id()}")
#     if n ==1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f"任务{n}的结果"
#
# if __name__ == "__main__":
#     print("---------------start---------------")
#     executor = ThreadPoolExecutor(3)
#     lock = RLock()
#
#     result = executor.map(work,[i for i in range(1,8)],[lock]*7)
#     print(list(result))
#
#
#     executor.shutdown(wait=True)
#
#     print("---------------end---------------")

def work(n,lock):
    with lock:
        print(f"work正在执行任务{n}.............{get_native_id()}")
    if n ==1:
        time.sleep(15)
    elif n == 2:
        time.sleep(10)
    else:
        time.sleep(1)
    return f"任务{n}的结果"

if __name__ == "__main__":
    print("---------------start---------------")
    with ThreadPoolExecutor(3) as executor:
        lock = RLock()

        result = executor.map(work,[i for i in range(1,8)],[lock]*7)
        print(list(result))



    print("---------------end---------------")