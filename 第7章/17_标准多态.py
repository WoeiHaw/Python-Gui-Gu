class Animal:
    def speak(self):
        print("动物正在发出声音")

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")
class Pig:
    def speak(self):
        print("哼哼哼")

def make_sound(animal:Animal):#类型注解
    animal.speak()

a1 = Animal()
d1 = Dog()
c1 = Cat()
p1 = Pig()
make_sound(a1)
make_sound(d1)
make_sound(c1)
make_sound(p1) #不推荐这样写