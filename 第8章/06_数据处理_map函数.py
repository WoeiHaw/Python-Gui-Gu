# nums = [10,20,30,40,50]

#map函数的返回值是一个迭代对象，需要我们自己去手动遍历，或者手动转换类型
# result = map(lambda x:x*2,nums)
# print(result)
# print(list(result))
# print(nums)

#字符串转换
# names = ("python","java","js")
# result = map(lambda x:x.upper(),names)
# print(result)
# print(tuple(result))
# print(names)

#类型转换
# str_number = {"1","2","3"}
# result = map(int,str_number)
# print(str_number)
# print(set(result))

#注意点
# 1. 延迟执行：map 不会离开计算，只有在“需要结果”式才执行
# 2. 返回值是迭代器对象，且一旦遍历完成，就会被“耗尽”。
# 3. map 不影响元素量

nums = [10,20,30,40,50]
result =list(map(lambda x:x*2,nums))
print(result)
