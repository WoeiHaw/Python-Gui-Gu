name = '张三'
gender = '男'
weight = 65.55
age = 12

info2 = '我叫%-4.1s,我是%3.2s生, 我的体重是%-9.3f,年龄是%6.4d' % (name, gender, weight, age)
print(info2)