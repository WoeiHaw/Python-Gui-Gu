# a= 100
# b = 100
#
# def test():
#     c ="尚硅谷"
#     d = "你好啊"
#     global a
#     a=300
#     print("函数中的打印(a)",a)
#     print("函数中的打印(b)",b)
#     print("函数中的打印(c)",c)
#     print("函数中的打印(d)",d)
#
# test()
# print("********************")
# print("全局的打印(a)",a)
# print("全局的打印(b)",b)
# print(c)
# print(d)

#
# def test2():
#     m= 100
#     m+=11
#     print(f"我是test2函数中打印的m：{m}")
# test2()
# test2()

n = 100

def test3():
    global n
    n +=1
    print(f"我是test3函数中打印的n：{n}")
test3()
test3()
test3()
print(n)