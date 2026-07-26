class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"我叫{self.name},年龄是{self.age}")


    def __enter__(self):
        print("------我是进入的逻辑-----")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("------我是离开的逻辑-----")
            print(exc_type)
            print(exc_val)
            print(exc_tb)
        return True

with Person("张三",18) as p1,Person("李四",18) as p2:
    p1.speak()
    # p1.study()
    print(666)