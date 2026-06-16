# 概念：以 __xxx__ 命名的特殊方法（双下化线开头）。
# 特点：不需要我们手动调，我们只要准备好这些方法，Python会在特定场景下，去自动调用
class Person:
    def __init__(self, name, age, gender):
        self.name = name  # 公有属性：当前类中，子类中，类外部，都可以访问
        self.age = age  # 受保护的属性：当前类中，子类中，都可访问
        self.gender = gender  # 私有属性：仅能在当前类中访问

    def __str__(self):
        return f"{self.name}-{self.age}-{self.gender}"

    def __len__(self):
        return len(p1.__dict__)

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __getattr__(self, item):
        return f"您方法的{item}属性不存在"
p1 = Person("张三", 18, "男")
p2 = Person("张三", 18, "男")
# print(p1)
# print(p2)
#
# res = len(p1)
# print(res)

# print(p1 > p2)

# print(p1 == p2)

print(p1.address)