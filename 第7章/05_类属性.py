class Person:
    # max_age, planet 他们都是类属性，类属性是保存在类身上的
    max_age = 120
    planet = "地球"
    def __init__(self, name, age, gender):
        self.name = name
        self.gender = gender
        if age <= Person.max_age:
            self.age = age
        else:
            print(f"年龄超出范围了，已经将年龄设置为最大值:{Person.max_age}")
            self.age = Person.max_age

# print(Person.__dict__)

p1 = Person("张三",18,"男")
p2 = Person("李四",22,"女")

# 实例身上是没有类属性的
# print(p1.__dict__)
# print(p2.__dict__)

# print(Person.max_age)
# print(p1.max_age)
# print(p2.max_age)

# p3 = Person("王五",170,"女")
# print(p3.__dict__)

p1.planet="火星"
print(Person.__dict__)
print(p1.__dict__)
print(p2.__dict__)

print(p1.planet)
print(p2.planet)