from abc import ABC, abstractmethod


# MustRUn类一旦继承了ABC类，那么MustRun类就是抽象类
class MustRun(ABC):
    @abstractmethod
    def run(self):
        pass
    def speak(self):
        print(f"你好，我叫{self.name}")


class Person(MustRun):
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def run(self):
        print(f"我叫{self.name}，我在努力的奔跑")

p1 = Person("张三",18,"男")
p1.run()
p1.speak()
