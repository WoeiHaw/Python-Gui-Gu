# names = ["张三","李四","王五"]
# cities = ("北京","上海","深圳")
# msg = "hello"
# age = 10
#
# def test():
#     pass
#
# for item in msg:
#     print(item)

# names = ["张三","李四","王五"]
# cities = ("北京","上海","深圳")
# msg = "hello"
# age = 10
#
# def test():
#     pass

# names.__iter__()
# cities.__iter__()
# msg.__iter__()

# print(hasattr(names,"__iter__"))
# print(hasattr(cities,"__iter__"))
# print(hasattr(msg,"__iter__"))
# print(hasattr(age,"__iter__"))
# print(hasattr(test,"__iter__"))

# names = ["张三","李四","王五"]
# cities = ("北京","上海","深圳")
# msg = "hello"
# print(names.__iter__())
# print(cities.__iter__())
# print(msg.__iter__())
#
# print(iter(names))
# print(iter(cities))
# print(iter(msg))

# names = ["张三","李四","王五"]
# it = iter(names)
# # print(it.__next__())
# # print(it.__next__())
# # print(it.__next__())
# # print(it.__next__())
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# names = ["张三","李四","王五"]

# for item in names:
#     print(item)

# it = iter(names)
# while True:
#     try:
#         item = next(it)
#         print(item)
#     except StopIteration:
#         break

# names = ["张三","李四","王五"]
# it = iter(names)
# print(it)
# result = iter(it)
# x = iter(result)
# print(x)
# print(result)

# for item in it:
#     print(item)