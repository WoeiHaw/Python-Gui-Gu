# 一，函数多返回值
# def calculate(x,y):
#     res1 = x+ y
#     res2 = x - y
#     return res1,res2
#
# result = calculate(30,10)
# print(result)
#
# r1,r2 = calculate(30,10)
# print(r1,r2)

#二，参数的打包与解包
# def show_info(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# show_info(10,20,30,name="张三",age=18,gender="男")

# def show_info(num1,num2,num3,name,age,gender):
#     print(num1,num2,num3)
#     print(name,age,gender)
# nums =(10,20,30)
# person={"name":"张三","age":18,"gender":"男"}
# show_info(*nums,**person)



def show_info(*args,**kwargs):
    print(args)
    print(kwargs)
nums =(10,20,30)
person={"name":"张三","age":18,"gender":"男"}
show_info(*nums,**person)