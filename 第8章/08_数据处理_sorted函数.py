# nums = [30,40,20,10]
# result = sorted(nums,reverse=True)
# print(result)

# 按照字符串的长度去排序
# names = ["python","sql","java"]
# result = sorted(names,key=len,reverse=True)
# print(result)

# 根据字典中的某个字段进行排序
person = [
    {"name": "张三", "age": 15, "gender": "男"},
    {"name": "李四", "age": 17, "gender": "女"},
    {"name": "王五", "age": 19, "gender": "男"},
    {"name": "李华", "age": 20, "gender": "女"},
    {"name": "赵六", "age": 18, "gender": "女"},
    {"name": "孙七", "age": 16, "gender": "男"},
]

result = sorted(person,key=lambda p:p["age"])
print(result)

#max,min 也可传递key参数
nums = [10, 20, 30, 40, 50]
result1 = max(person,key=lambda p:p["age"])
result2 = min(person,key=lambda p:p["age"])

print(result1)
print(result2)