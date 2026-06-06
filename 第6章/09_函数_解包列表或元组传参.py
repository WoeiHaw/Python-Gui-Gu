def test(*args):
     print(f"我是test函数，我收到的参数是:{args},参数的类型是：{type(args)}")

list1 =[100,200,300,400]
tuple1 = ("你好","北京","尚硅谷")

# test(list1)
# test(tuple1)

test(*list1) # equivalent : test(100,200,300,400)
test(*tuple1) # equivalent : test(你好","北京","尚硅谷")