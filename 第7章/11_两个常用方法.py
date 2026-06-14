from  datetime import datetime
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self,msg):
        print(f"我叫{self.name}，年龄是{self.age}，性别是{self.gender},我想说：{msg}")

class Student(Person):
    def __init__(self,name,age,gender,stu_id,grade):
        super().__init__(name,age,gender)
        self.stu_id = stu_id
        self.grade = grade

p1 = Person("张三",18,"男")
s1 = Student("李华",12,"男","2025001","初二")

# print(isinstance(s1,Student))
# print(isinstance(p1,Person))
#
# print(isinstance(s1,Person))
# print(isinstance(p1,Student))

# print(issubclass(Student,Person))
# print(issubclass(Person,Student))