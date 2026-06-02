def greet(name,/,gender,*,age, height):
    print(f"我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm")

#正确示例
# before / use positional argument
# after * user keyword argument
#/ must before *
greet("张三","男",age = 18,height=172)
greet("张三",gender="男",age = 18,height=172)

#错误示例
# greet("张三","男",18,height=172)
