# 可变位参数 - positional arguments
# 可变关键子参数 - keyword arguments
#定义函数（使用*args去接收：可变位参数）
def test1(*args):
    # args is tuple
    print(args)


test1("张三","男",18,172)

#定义函数（使用**kwargs去接收：可变关键子参数）
def test2(**kwargs):
    # kwargs is dictionary
    print(kwargs)

test2(name="张三",gender="男",age=18,height=172)

#定义函数（同时使用：可变位置参数，可变关键子参数）
def test3(a,b,*args,c="尚硅谷",**kwargs):
    print("@@@@@@@@@@@@")
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

test3("张三","男","抽烟",c= "atguigu",age=18,height=172)


