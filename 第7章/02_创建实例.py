class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


p1 = Person("张三",18,"男")
p2 = Person("李四",22,"女")
# print(p1.name)
# print(p1.age)
# print(p1.gender)
# print("-"*20)
# print(p2.name)
# print(p2.age)
# print(p2.gender)
# p1.name = "阿三"
# print(p1.name)

# print(p1.__dict__)
# print(p2.__dict__)

# p1.address = "北京昌福科技园"
# print(p1.__dict__)

print(type(p1))
print(type(p2))

