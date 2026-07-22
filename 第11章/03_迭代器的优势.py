import tracemalloc
class Fibo:
    def __init__(self,total):
        self.total = total
        self.index = 0
        self.pre = 1
        self.cur = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.total:
            raise StopIteration
        if self.index<2:
            value = 1
        else:
            value = self.pre + self.cur
            self.pre = self.cur
            self.cur = value
        self.index +=1
        return value

# f1 = Fibo(10)
# for item in f1:
#     print(item)

def fibo(total):
    if total <=0:
        return []
    if total == 1:
        return [1]
    nums = [1,1]
    for i in range(2,total):
        nums.append(nums[-1] + nums[-2])
    return nums
#
# f1 = fibo(10)
# for item in f1:
#     print(item)

# tracemalloc.start()
# f1 = Fibo(10000)
# m = tracemalloc.get_traced_memory()[1]
# print(f"内存占用是：{m/1024/2024}mb")

# tracemalloc.start()
# f1 = fibo(100000)
# m = tracemalloc.get_traced_memory()[1]
# print(f"内存占用是：{m/1024/2024}mb")

f1 = Fibo(100000)
for n in f1:
    if n>100:
        break
    print(n)


