from datetime import  datetime
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    #静态方法
    #静态方法保存在类上的
    #它不会收到：self，cls参数。它收到参数都是自定义参数
    #通常用于定义：与类相关的工具方法
    @staticmethod
    def is_adult(year):
        current_year = datetime.now().year
        age = current_year - year
        return age>= 18

    @staticmethod
    def mas_idcard(idcard):
        return idcard[:6] + "*"*8 + idcard[-4:]


#验证一下：静态方法保存在类上的
# print(Person.__dict__)

# 静态方法需要通过类调用
# result = Person.is_adult(1983)
# print(result)

result2 = Person.mas_idcard("12345678-098763456")
print(result2)