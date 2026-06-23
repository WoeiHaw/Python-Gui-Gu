# 列表推导式：用一条简洁语句，从可迭代对象中，生成新列表的语法结构
# 备注：列表推导式本质上是对 for 循环 + append() 的一种简写形式
#
# nums = [10,20,30,40]
# result =list( map(lambda n:n*2,nums))
# print(result)
#
# nums = [10,20,30,40]
# result = []
# for n in nums:
#     result.append(n*2)
# print(result)
#
# nums = [10,20,30,40]
# result = [n*2 for n in nums]
# print(result)

# nums = [10,20,30,40]
# result = [n*2 for n in nums if n >20]
# print(result)

# names = ["张三", "李四", "王五"]
# scores = [60, 70, 80]
# result = {names[i]:scores[i]  for i in range(len(names))}
# print(result)

names = ["张三", "李四", "王五"]
result = {n+ "!" for n in names}
print(result)

#python 没有元组推导式

