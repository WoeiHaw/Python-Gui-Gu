import time
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
def cpu_task(n):
    print(f"任务{n}开始了")
    total = 0
    for i in range(10000000):
        total += i * i
    return total


if __name__ == '__main__':
    # print("==========多进程完成【cpu密集型任务】=======")
    # start = time.time()
    # with ProcessPoolExecutor(4) as executor:
    #     list(executor.map(cpu_task,[1,2,3,4]))
    # end = time.time()-start
    # print(f"多进程总耗时：{end}秒\n")
    print("==========多进线完成【cpu密集型任务】=======")
    start = time.time()
    with ThreadPoolExecutor(4) as executor:
        list(executor.map(cpu_task, [1, 2, 3, 4]))
    end = time.time() - start
    print(f"多线程总耗时：{end}秒\n")