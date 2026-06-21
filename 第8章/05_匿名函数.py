# def add(x, y):
#     return x + y
#
#
# def sub(x, y):
#     return x - y
#
#
# def calculate(fun, a, b):
#     print(f"计算结果为：{fun(a,b)}")
#
# calculate(add,30,10)
# calculate(sub,30,10)

# 匿名函数
# add1 = lambda x, y: x + y
# add2 = lambda x: x + x
# add3 = lambda: "我是add3函数"
#
# result1 = add1(30,10)
# result2= add2(30)
# result3 = add3()


# print(result1,result2,result3)

# def calculate(fun, a, b):
#     print(f"计算结果为：{fun(a,b)}")
#
# calculate(lambda x,y:x+y,30,10)
# calculate(lambda x,y:x-y,30,10)

is_adult = lambda age: "成年" if age >= 18 else "未成年"
print(is_adult(18))
print(is_adult(13))
