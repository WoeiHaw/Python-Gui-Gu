import os
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
#
# def work(n):
#     print(f"work正在执行任务{n}.............{os.getpid()}")
#     time.sleep(1)
#
# if __name__ == "__main__":
#     print("---------------start---------------")
#     executor = ProcessPoolExecutor(3)
#     executor.submit(work,1)
#     executor.submit(work,2)
#     executor.submit(work,3)
#     executor.submit(work,4)
#     executor.submit(work,5)
#     executor.submit(work,6)
#     executor.submit(work,7)
#     executor.shutdown(wait=True)
#     print("---------------end---------------")


# def work(n):
#     print(f"work正在执行任务{n}.............{os.getpid()}")
#     time.sleep(1)
#     return f"我是任务{n}的结果"
#
# if __name__ == "__main__":
#     print("---------------start---------------")
#     executor = ProcessPoolExecutor(3)
    # future1=executor.submit(work,1)
    # future2=executor.submit(work,2)
    # future3=executor.submit(work,3)
    # future4=executor.submit(work,4)
    # future5=executor.submit(work,5)
    # future6=executor.submit(work,6)
    # future7=executor.submit(work,7)

    # futures = [executor.submit(work,index) for index in range(1,8)]
    #
    # executor.shutdown(wait=True)
    # print(future1.result())
    # print(future2.result())
    # print(future3.result())
    # print(future4.result())
    # print(future5.result())
    # print(future6.result())
    # print(future7.result())

    # for f in futures:
    #     print(f.result())
    # print("---------------end---------------")

# def work(n):
#     print(f"work正在执行任务{n}.............{os.getpid()}")
#     if n ==1:
#         time.sleep(15)
#     elif n ==2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f"我是任务{n}的结果"
#
# if __name__ == "__main__":
#     print("---------------start---------------")
#     executor = ProcessPoolExecutor(3)
#
#     futures = [executor.submit(work,index) for index in range(1,8)]
#     result_list = []
#     for f in as_completed(futures):
#         result_list.append(f.result())
#     executor.shutdown(wait=True)
#
#     print(result_list)
#
#
#     print("---------------end---------------")



# def work(n):
#     print(f"work正在执行任务{n}.............{os.getpid()}")
#     time.sleep(1)
#     return f"我是任务{n}的结果"
#
# if __name__ == "__main__":
#     print("---------------start---------------")
#     executor = ProcessPoolExecutor(3)
#
#     result_list = []
#     def done_func(future):
#         result_list.append(future.result())
#
#     for index in range(1,8):
#         f = executor.submit(work,index)
#         f.add_done_callback(done_func)
#     executor.shutdown(wait=True)
#     print(result_list)
#     print("---------------end---------------")


# def work(n):
#     print(f"work正在执行任务{n}.............{os.getpid()}")
#     if n ==1:
#         time.sleep(15)
#     elif n ==2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f"我是任务{n}的结果"
#
# if __name__ == "__main__":
#     print("---------------start---------------")
#     executor = ProcessPoolExecutor(3)
#
#     result = executor.map(work,[n for n in range(1,9)])
#     print(list(result))
#
#     executor.shutdown(wait=True)
#
#
#
#     print("---------------end---------------")




def work(n):
    print(f"work正在执行任务{n}.............{os.getpid()}")
    if n ==1:
        time.sleep(15)
    elif n ==2:
        time.sleep(10)
    else:
        time.sleep(1)
    return f"我是任务{n}的结果"

if __name__ == "__main__":
    print("---------------start---------------")
    with ProcessPoolExecutor(3) as executor:
        result = executor.map(work,[n for n in range(1,9)])
        print(list(result))

    print("---------------end---------------")






