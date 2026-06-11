class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self,msg):
        print(f"我叫{self.name}，年龄是{self.age}，性别是{self.gender},我想说：{msg}")


# print(Person.__dict__)

p1 = Person("张三",18,"男")
p2 = Person("李四",22,"女")

# print(p1.__dict__)
# print(p2.__dict__)

# p1.speak("好好学习")
# p2.speak("天天向上")

def speak():
    print("吧啦")
    print("吧啦")
    print("吧啦")
p1.speak = speak
print(Person.__dict__)
print(p1.__dict__)
print(p2.__dict__)
p1.speak()
