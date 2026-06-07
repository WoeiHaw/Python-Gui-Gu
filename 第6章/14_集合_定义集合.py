# s1 = {10,20,20,30,40,40,50,60,60,70,80,90,100}
# s2 = {"你好","hello","你好","atguigu","北京"}
# s3 = {10,"你好",1,True,12.4}
#
# print(type(s1),s1)
# print(type(s2),s2)
# print(type(s3),s3)

# s1 = frozenset({10,20,20,30,40,40,50,60,60,70,80,90,100})
# s2 = frozenset({"你好","hello","你好","atguigu","北京"})
# s3 = frozenset({10,"你好",1,True,12.4})
#
# print(type(s1),s1)
# print(type(s2),s2)
#  print(type(s3),s3)
# s1 = frozenset([10,20,30,40,50])
# s2 = frozenset([10,20,30,40,50])
# s3 = frozenset("hello")
# print(type(s1),s1)
# print(type(s2),s2)
# print(type(s3),s3)

# s1 = set()
# print(type(s1),s1)

# s2 = {}
# print(type(s2),s2)

# s3 = frozenset()
# print(type(s3),s3)

# only immutable object can insert into set
s1 = {10,20,30,40,50}
s2 = frozenset({100,200,300,400,500})
l1 = [666,777,888]
t1 = (666,777,888)

# error, s1 is mutable
# s3 = {11,22,33,s1}
# print(s3)

# s2 is immutable
# s3 = {11,22,33,s2}
# print(s3)

# error,l1 is mutable
# s3 = {11,22,33,l1}
# print(s3)

#t1 is immutable
s3 = {11,22,33,t1}
print(s3)