# class SayHello:
#     def __call__(self, func):
#         def wrapper(*args,**kwargs):
#             print("你好我要开始计算了")
#             return func(*args,**kwargs)
#         return wrapper

# @SayHello()
# def add(x,y):
#     res = x + y
#     print(f"{x}和{y}相加的结果{res}")
#     return res
#
# result = add(10,20)
# print(result)

# say = SayHello()
# add = say(add)
# result = add(10,20)
# print(result)


# class SayHello:
#     def __init__(self,msg):
#         self.msg = msg
#     def __call__(self, func):
#         def wrapper(*args,**kwargs):
#             print(f"你好我要开始{self.msg}计算了")
#             return func(*args,**kwargs)
#         return wrapper
#
# @SayHello("加法")
# def add(x,y):
#     res = x + y
#     print(f"{x}和{y}相加的结果{res}")
#     return res
# result = add(10,20)
# print(result)


class Test1:
    def __call__(self,func):
        def wrapper(*args,**kwargs):
            print(f"我是test1追加的逻辑")
            return func(*args,**kwargs)
        return wrapper
class Test2:
    def __call__(self,func):
        def wrapper(*args,**kwargs):
            print(f"我是test2追加的逻辑")
            return func(*args,**kwargs)
        return wrapper

@Test1()
@Test2()
def add(x,y):
    res = x+ y
    print(f"{x}和{y}相加的结果是{res}")
    return res

result = add(10,20)
print(result)