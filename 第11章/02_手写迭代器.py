# names = ["张三","李四","王五"]
# it = iter(names)
# print(next(it))
# print(next(it))
# print(next(it))

# for item in it:
#     print(item)
#
# for item in it:
#     print(item)

# class Person:
#     def __init__(self,name,age,gender,address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#     def __iter__(self):
#         return PersonIterator(self)
#
# class PersonIterator:
#     def __init__(self,p):
#         self.p = p
#         self.index = 0
#         self.attrs = [p.name,p.age,p.gender,p.address]
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.attrs):
#             raise StopIteration
#         value = self.attrs[self.index]
#         self.index +=1
#         return value
#
# p1 = Person("张三",18,"男","北京昌平")
# for item in p1:
#     print(item)


# class Person:
#     def __init__(self,name,age,gender,address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#         self.__index = 0
#         self.__attrs = [name,age,gender,address]
#
#     def __iter__(self):
#         self.__index=0
#         return self
#
#     def __next__(self):
#         if self.__index >= len(self.__attrs):
#             raise StopIteration
#         value = self.__attrs[self.__index]
#         self.__index +=1
#         return value
#
#
#
# p1 = Person("张三",18,"男","北京昌平")
# it = iter(p1)
# for item in it:
#     print(item)
#
# for item in it:
#     print(item)

from cn2an import an2cn
class Person:
    def __init__(self,name,age,gender,address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.__index = 0
        self.__attrs = [name,age,gender,address]

    def __iter__(self):
        self.__index=0
        return self

    def __next__(self):
        if self.__index >= len(self.__attrs):
            raise StopIteration
        value = self.__attrs[self.__index]

        if isinstance(value,str):
            value = value.upper()
        if isinstance(value,int):
            value = an2cn(value)
        self.__index +=1
        return value


p1 = Person("zhangsan",18,"男","北京昌平")
it = iter(p1)
for item in it:
    print(item)

for item in it:
    print(item)