# default parameter must after non-default parameter
def greet(name,gender,age, height,msg = "你好"):
    print(f"我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm")
    print(f"我想说： {msg}")

# greet("张三","男",18,172)
# greet("张三","男",18,172,"hello")
# greet("张三","男",18,172,msg="hello")

