# 错误：代码本身有语法错误，解释器无法执行代码。--无法通过异常处理机制解决
# age = 18
# if age >=18
#     print("成年人")
# 异常：代码语法上没问题，但执行过着出现了问题。--可以通过异常处理机制解决
# 1.zeroDivisionError:
# num1 = 100
# num2 = 0
# result = num1/num2

# 2. TypeError
# result = "10" + 5

# 3.AttributeError
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# p1 = Person("张三",18)
# print(p1.name)
# print(p1.age)
# print(p1.gender)

# nums = [10, 20, 30]
# nums.add(40)

# 4. indexError
# nums = [10,20,30,40]
# print(nums[5])

#5. NameError:
# print(school)

#6.KeyError:
# person = {"name":"张三","age":18}
# print(person["gender"])

#7.ValueError
int("hello")