# t1 = (28,67,21,67,11)
# t2 = ("北京","尚硅谷","你好")
# t3 = (100,True,"你好",None)
# t4 = (100,True,"你好",None,(50,60,70))
#
# print(type(t1),t1)
# print(type(t2),t2)
# print(type(t3),t3)
# print(type(t4),t4)
#
# t1 = (28,67,21,67,11)
# print(t1[3])
# print(t1[-1])

# t1 = (28,67,21,67,11)
# t1[0] = 100
#
# t2 = (28,67,21,67,11,[100,200,300,("你好","尚硅谷")])
# t2[5][2] = 400
# t2[5][3][0] = "你好"
#
# print(t2)

# t1 = ()
# t2 = tuple()
# print(type(t1),t1)
# print(type(t2),t2)

# t1 = ("你好", )
# t2 = (18, )
#
# print(type(18),18)

# t1 = (28,67,21,67,11)
# result = t1.index(67)
# print(result)

# t1 = (28,67,21,67,11)
# result = t1.count(67)
# print(result)

# t1 = (23,11,32,30,17)
# result = max(t1)
# print(result)

# t1 = (23,11,32,30,17)
# result = min(t1)
# print(result)

# t1 = (23,11,32,30,17)
# result = len(t1)
# print(result)

# t1 = (23,11,32,30,17)
# result = sorted(t1,reverse=True)
# print(result)

# t1 = (23,11,32,30,17)
# result = sum(t1)
# print(result)

# def demo(*args):
#     print(args)
#     return sum(args)
# result = demo(100,200,300)
# print(result)

t1 = (23,11,32,30,17)
# index = 0
# while index < len(t1):
#     print(t1[index])
#     index +=1

for item in t1:
    print(item)