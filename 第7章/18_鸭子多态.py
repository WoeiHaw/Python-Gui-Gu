class Dog:
    def speak(self):
        print("汪汪汪")


class Cat:
    def speak(self):
        print("喵喵喵")


class Pig:
    def speak(self):
        print("哼哼哼")


class Fish:
    def speak(self):
        print("咕噜噜")


def make_sound(animaa):
    animaa.speak()

d1 = Dog()
c1 = Cat()
p1 = Pig()
f1 = Fish()

make_sound(d1)
make_sound(c1)
make_sound(p1)
make_sound(f1)