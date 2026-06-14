from  datetime import datetime
class Person:

    max_age = 120
    planet = "地球"
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self,msg):
        print(f"我叫{self.name}，年龄是{self.age}，性别是{self.gender},我想说：{msg}")

    def run(self,distance):
        print(f"{self.name}疯狂的奔跑了{distance}米")

    # 使用@ classmethod 装饰过的方法，就叫：类方法
    @classmethod
    def test1(cls,data):
        print("我是test1",cls,data)

    @classmethod
    def change_planet(cls, value):
        cls.planet = value

    @classmethod
    def test2(cls):
        print("我是test2")

    @classmethod
    def create(cls,info_str):
        #从info_str中获取到有效的信息
        name,year,gender = info_str.split("-")
        #获取当前的年份
        current_year = datetime.now().year
        age = current_year - int(year)
        #创建并返回Person类的实例对象
        return cls(name,age,gender)


# 验证一下：类方法保存在类身上
# print(Person.__dict__)

# 类方法需要通过类调用
Person.change_planet("月球")
print(Person.__dict__)

# 创建Person实例
# p1 = Person("张三",18,"男")
# p2 = Person("李四",22,"女")

# 验证一下：类属性planet已改了
# print(p1.planet)
# print(p2.planet)

p3 = Person.create("李华-2003-女")
print(p3.__dict__)

