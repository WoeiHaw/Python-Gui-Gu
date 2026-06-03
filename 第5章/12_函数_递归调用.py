#从大到下
# def welcome(n):
#     print(f"你好啊{n}")
#     if n>1:
#         welcome(n-1)
# welcome(5)

#从小到大
def welcome(n):
    if n>1:
        welcome(n-1)
    print(f"你好啊{n}")


welcome(5)
