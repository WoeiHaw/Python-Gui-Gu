# def say_hello(func):
#     def wrapper(*args,**kwargs):
#         print("你好，我要开始计算了")
#         return func(*args,**kwargs)
#     return wrapper
#
# @say_hello
# def add(x,y,z):
#     res = x + y + z
#     print(f"{x}和{y}和{z}相加的结果是：{res}")
#     return  res
#
# result = add(10,20,30)
# print(result)

# add = say_hello(add)
# result = add(10,20,30)
# print(result)


#进阶：带参数的装饰器（三层嵌套，外层接收配置，中间层接收函数，内层接收具体参数）
# def say_hello(msg):
#     def outer(func):
#         def wrapper(*args,**kwargs):
#             print(f"你好，我要开始{msg}计算了")
#             return func(*args,**kwargs)
#         return wrapper
#     return outer
#
# @say_hello("加法")
# def add(x,y,z):
#     res = x + y + z
#     print(f"{x}和{y}和{z}相加的结果是：{res}")
#     return  res
#
# @say_hello("减法")
# def sub(x,y):
#     res = x - y
#     print(f"{x}和{y}相减的结果是：{res}")
#     return  res
#
# result = add(10,20,30)
# print(result)
#
# result = sub(20,10)
# print(result)

# 进阶：多个装饰器一起使用
# add = test1(test2(add))
def test1(func):
    print("我是test1装饰器")
    def wrapper(*args,**kwargs):
        res =  func(*args,**kwargs)
        print("test1追加的逻辑")
        return res
    return wrapper

def test2(func):
    print("我是test2装饰器")
    def wrapper(*args,**kwargs):
        res =  func(*args,**kwargs)
        print("test2追加的逻辑")
        return res
    return wrapper

@test1
@test2
def add(x,y):
    res = x + y
    print(f"{x}和{y}相加的结果是{res}")
    return res

result = add(10,20)
print(result)