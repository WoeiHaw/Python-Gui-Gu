
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

#验证一下：Person继承了object类
# print(issubclass(Person,object))
# print(issubclass(int,object))
# print(issubclass(str,object))
# print(issubclass(list,object))
# print(issubclass(bool,object))
# print(issubclass(tuple,object))


# p1 = Person("张三",18,"男")
# print(isinstance(p1,object))
#
# print(isinstance(100,object))
# print(isinstance("hello",object))
# print(isinstance(True,object))
# print(isinstance(None,object))
# print(isinstance([10,20,30],object))
# print(isinstance({"吃饭","睡觉"},object))

# for key in object.__dict__:
#     print(key)

p1 = Person("张三",18,"男")
print(p1.__dict__) #对象身上自己的东西
print(dir(p1)) #对象可以访问到的东西

print(p1)