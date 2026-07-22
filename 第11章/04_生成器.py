# def demo():
#     print("demo函数开始执行了")
#     print(100)
#       yield
#     a = 200
#     print(a)
#
# d = demo()
# print(d)

# def demo():
#     print("demo函数开始执行了")
#     print(100)
#     yield "我是第一个yield所返回的数据"
#     a=200
#     print(a)
#     yield "我是第二个yield所返回的数据"
#     b = 300
#     print(b)
#     return "尚硅谷"
#
# d = demo()
# r1 = next(d)
# print(r1)
#
# r2 = next(d)
# print(r2)
#
# try:
#     next(d)
# except StopIteration as e:
#     print(e)

# def demo():
#     print("demo函数开始执行了")
#     print(100)
#     yield "我是第一个yield所返回的数据"
#     a=200
#     print(a)
#     yield "我是第二个yield所返回的数据"
#     b = 300
#     print(b)
#     return "尚硅谷"
#
# d = demo()
# print(hasattr(d,"__iter__"))
# print(hasattr(d,"__next__"))

# result = iter(d)
# print(result ==d)

# for item in d:
#     print(item)

# gen = iter(d)
# while True:
#     try:
#         value = next(gen)
#         print(value)
#     except StopIteration:
#         break

# def create_car(total):
#     for index in range(1,total+1):
#         yield f"我是第{index}台车"
#
# cars = create_car(5)
# c1 = next(cars)
# print(c1)
# c2 = next(cars)
# print(c2)
# c3 = next(cars)
# print(c3)

# for car in cars:
#     print(car)

# def demo():
#     nums =[10,29,30,40]
#     yield  from nums
#
# d = demo()
# r1 = next(d)
# print(r1)
# for item in d:
#     print(item)

# def demo():
#     print("demo函数开始执行了")
#     print(100)
#
#     a=yield "我是第一个yield所返回的数据"
#     print(a)
#
#     b = yield "我是第二个yield所返回的数据"
#     print(b)
#     return "尚硅谷"
#
# d = demo()
# r1 = next(d)
# print(r1)
# r2 = d.send(666)
# print(r2)
# try:
#     d.send(888)
# except StopIteration as e:
#     print(e)


# class Person:
#     def __init__(self,name,age,gender,address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#         self.__attr =[name,age,gender,address]
#
#     def __iter__(self):
#         # yield  self.name
#         # yield self.age
#         # yield self.gender
#         # yield self.address
#         yield from self.__attr
# p1 = Person("张三",18,"男","北京昌平")
#
# for i in p1:
#     print(i)

# def fibo(total):
#     pre = 1
#     cur = 1
#
#     for index in range(total):
#         if index < 2:
#             yield 1
#         else:
#             value = pre +  cur
#             pre = cur
#             cur = value
#             yield value
#
# f1 = fibo(10)
#
# # for item in f1:
# #     print(item)
#
# result = list(f1)
# print(result)

nums = [10,20,30,40]

result = [n * 2 for n in nums]
print(result)

result2 = (n * 2 for n in nums)
# print(list(result2))
for item in result2:
    print(item)