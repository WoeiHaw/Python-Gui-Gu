name = '张三'
gender = '男'
weight = 65.2
age = 12

info1 = '我叫' + name + ',我是' + gender + '生'

# %s占位字符串， %f占位浮点数，%i占位整数，%d占位十进制， %s是万能
info2 = '我叫%s,我是%s生, 我的体重是%s,年龄是%s' % (name, gender, weight, age)
print(info2)

#使用 f string
info3 = f'我叫{name}，我是{gender}，我体重量是，{weight},年龄{age}'
print(info3)
