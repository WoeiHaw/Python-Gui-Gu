# def outer():
#     num = 10
#     num +=1
#     print(num)
# outer()

# def outer():
#     num = 10
#     def inner():
#         nonlocal  num
#         num = 99
#         print(1,num)
#     inner()
#     print(2,num)
# outer()

# 什么是闭包？ ---闭包 = 内层函数 + 被内层函数所引用的外层变量
# def outer():
#     num = 10
#     print(hex(id(num)))
#
#     def inner():
#         nonlocal num
#         num +=1
#         print(num)
#     return inner
#
# f = outer()
# f()
# f()
# f()
# 1. outer 函数中，被inner所使用到的变量，会被封存到【闭包单元（cell）】中。
# 2. 这些 cell 会组成一个__closure__元组，最终放在了inner函数身上
# print(f.__closure__)
#
# print(f.__closure__[0])
# print(f.__closure__[0].cell_contents)

# 1. 调用n次外层函数，就会得到n个不同的闭包，并且这些闭包之间互不影响
# def outer():
#     num = 10
#     def inner():
#         nonlocal num
#         num +=1
#         print(num)
#     return inner
#
# f1 = outer()
# f1()
# f1()
# f1()
# print("****************")
# f2 = outer()
# f2()

# 2. 内层函数中用到的外层变量是可变对象，多个闭包之间依然互不影响
# def outer():
#     nums = []
#
#     def inner(value):
#         nums.append(value)
#         print(nums)
#     return inner
# f1 = outer()
# f1(10)
# f1(20)
# f1(30)
# print("****************")
# f2 = outer()
# f2(666)
# def beauty(char, n):
#     def show_msg(msg):
#         print(char * n + msg + char * n)
#     return show_msg
#
# show = beauty("*",2)
# show("你好啊")
# show("尚硅谷")

class Beauty:
    def __init__(self,char,n):
        self.char = char
        self.n = n
    def show_msg (self,msg):
        print(self.char*self.n + msg + self.char*self.n)
b1 = Beauty("*",3)
b1.show_msg("你好啊")
b1.show_msg("尚硅谷")