# res1 = list(range(8))
# res2 = list("欢迎来电尚硅谷")
# res3 = list({10,20,30,40,50})
# res4 = list({"张三":72,"李四":60,"王五":85}.items())
# print(type(res1),res1)
# print(type(res2),res2)
# print(type(res3),res3)
# print(type(res4),res4)


# res1 = tuple(range(8))
# res2 = tuple("欢迎来电尚硅谷")
# res3 = tuple({10,20,30,40,50})
# res4 = tuple({"张三":72,"李四":60,"王五":85}.items())
# print(type(res1),res1)
# print(type(res2),res2)
# print(type(res3),res3)
# print(type(res4),res4)

# res1 = set(range(8))
# res2 = set("欢迎来电尚硅谷")
# res3 = set({10,20,30,40,50})
# res4 = set({"张三":72,"李四":60,"王五":85}.items())
# print(type(res1),res1)
# print(type(res2),res2)
# print(type(res3),res3)
# print(type(res4),res4)

# res1 = str(range(8))
# res2 = str("欢迎来电尚硅谷")
# res3 = str({10,20,30,40,50})
# res4 = str({"张三":72,"李四":60,"王五":85}.items())
# res5 = str(False)
# res6 = str(None)
# res7 = str(100)
# print(type(res1),res1)
# print(type(res2),res2)
# print(type(res3),res3)
# print(type(res4),res4)
# print(type(res5),res5)
# print(type(res6),res6)
# print(type(res7),res7)


# dict content must be key value pair
# res1 = dict({"张三":72,"李四":60,"王五":85})
# res2 = dict([("张三",72),("李四",60),("王五",85)])
# res3 = dict((("张三",72),("李四",60),("王五",85)))
# res4 = dict({("张三",72),("李四",60),("王五",85)})
# print(type(res1),res1)
# print(type(res2),res2)
# print(type(res3),res3)
# print(type(res4),res4)

hobby =["抽烟","喝酒","烫头"]
nums = (10,20,30,40,50)
message = "hello,atguigu"
city = {"北京","上海","天津","重庆"}
score = {"张三":72,"李四":60,"王五":85}

print("喝酒" in hobby)
print(20 in nums)
print("hel" in message)
print("上海" in city)
print("李华" in score)