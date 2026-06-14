from  datetime import datetime
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self,msg):
        print(f"我叫{self.name}，年龄是{self.age}，性别是{self.gender},我想说：{msg}")


#定义一个student类，继承自Person类
class Student(Person):
    def __init__(self,name,age,gender,stu_id,grade):

        #方式1(更推荐)
        super().__init__(name,age,gender)

        #方式2
        #Person.__init__(self,name,age,gender)
        self.stu_id = stu_id
        self.grade = grade

    def study(self):
        print(f"我叫{self.name}，我在努力的学习，争取做到{self.grade}的第一名")


#创建Student类的实例的对象
s1 = Student("李华",16,"男","2025001","初二")
# print(s1.__dict__)
# print(type(s1))

# def speak(data):
#     print("我是s1自身的speak方法",data)
# s1.speak = speak
#查找speak方法的过程：1.实例自身（s1) => 2.Student类 => 3.Person 类
# s1.speak("你好")

# print(s1.__dict__)
# s1.study()