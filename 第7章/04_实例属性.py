class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


p1 = Person("张三",18,"男")
p2 = Person("李四",22,"女")
# print(p1.name)
# print(Person.name)

p1.name = "阿三"
print(p1.name)
print(p2.name)