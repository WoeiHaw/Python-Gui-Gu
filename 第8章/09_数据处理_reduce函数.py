# reduce 函数：将一组数据不断合并，最终归并成一个结果

#从 functools 模块中引入 reduce
from functools import reduce

# nums = [1,2,3,4,5]
# result = reduce(lambda a,b:a+b,nums,10)
# print(result)

#字符串拼接
str_list = ["ab","cd","ef"]
result = reduce(lambda a,b:a+b,str_list)
print(result)
