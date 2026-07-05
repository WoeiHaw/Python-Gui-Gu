# print("欢迎使用本程序")
# a = int(input("请输入第一个数："))
# b = int(input("请输入第二个数："))
# result = a/b
# print(f"{a}除以{b}的结果是：{result}")
# print("***************我是后续的其他逻辑1***************")
# print("***************我是后续的其他逻辑2***************")


# print("欢迎使用本程序")
# try:
#     a = int(input("请输入第一个数："))
#     b = int(input("请输入第二个数："))
#     result = a/b
#     print(f"{a}除以{b}的结果是：{result}")
# except:
#     print("抱歉程序出现了异常")
# print("***************我是后续的其他逻辑1***************")
# print("***************我是后续的其他逻辑2***************")


# print("欢迎使用本程序")
# try:
#     a = int(input("请输入第一个数："))
#     b = int(input("请输入第二个数："))
#     result = a/b
#     print(f"{a}除以{b}的结果是：{result}")
# except ZeroDivisionError:
#     print("程序异常：0不能作为除数")
# except ValueError:
#     print("程序异常：你输入的必须是数字")
# print("***************我是后续的其他逻辑1***************")
# print("***************我是后续的其他逻辑2***************")


# print(issubclass(ZeroDivisionError,ArithmeticError))
# print(issubclass(ZeroDivisionError,Exception))
# print(issubclass(ValueError,Exception))
# print(issubclass(KeyboardInterrupt,Exception))
# print(issubclass(KeyboardInterrupt,BaseException))

# print("欢迎使用本程序")
# try:
#     a = int(input("请输入第一个数："))
#     b = int(input("请输入第二个数："))
#     print(x)
#     result = a/b
#     print(f"{a}除以{b}的结果是：{result}")
# except ZeroDivisionError:
#     print("程序异常：0不能作为除数")
# except ValueError:
#     print("程序异常：你输入的必须是数字")
# except Exception:
#     print("程序异常")
# print("***************我是后续的其他逻辑1***************")
# print("***************我是后续的其他逻辑2***************")

# print("欢迎使用本程序")
# try:
#     a = int(input("请输入第一个数："))
#     b = int(input("请输入第二个数："))
#     print(x)
#     result = a/b
#     print(f"{a}除以{b}的结果是：{result}")
# except ZeroDivisionError as e:
#     print("程序异常：0不能作为除数")
# except ValueError as e:
#     print("程序异常：你输入的必须是数字")
#
# except Exception as e:
#     print(f"程序异常.异常信息：{e}")
#     print(f"程序异常.异常类型：{type(e)}")
#     print(f"程序异常.异常参数：{e.args}")
#     print(f"程序异常.异常文件：{e.__traceback__.tb_frame.f_code.co_filename}")
#     print(f"程序异常.异常的具体行数：{e.__traceback__.tb_lineno}")
    # import traceback
    # print(traceback.format_exc())


# print("欢迎使用本程序")
# try:
#     a = int(input("请输入第一个数："))
#     b = int(input("请输入第二个数："))
#     result = a/b
#     print(f"{a}除以{b}的结果是：{result}")
# except(ZeroDivisionError,ValueError,Exception) as e:
#     if isinstance(e,ZeroDivisionError):
#         print("程序异常：0不能作为除数")
#     elif isinstance(e,ValueError):
#         print("程序异常：你输入的必须是数字")
#     else:
#         print(f"程序异常：{e}")
#
# print("***************我是后续的其他逻辑1***************")
# print("***************我是后续的其他逻辑2***************")

print("欢迎使用本程序")
try:
    a = int(input("请输入第一个数："))
    b = int(input("请输入第二个数："))
    result = a/b
    print(f"{a}除以{b}的结果是：{result}")
except(ZeroDivisionError,ValueError,Exception) as e:
    if isinstance(e,ZeroDivisionError):
        print("程序异常：0不能作为除数")
    elif isinstance(e,ValueError):
        print("程序异常：你输入的必须是数字")
    else:
        print(f"程序异常：{e}")
else:
    print("挺好的，try中的代码没有任何的异常")
finally:
    print("无论有没有异常，我的计算都结束了")

print("***************我是后续的其他逻辑1***************")
print("***************我是后续的其他逻辑2***************")