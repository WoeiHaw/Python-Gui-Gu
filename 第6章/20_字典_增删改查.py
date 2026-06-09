# d1 = {"张三":72,"李四":60,"王五":85}
# result = d1["张三"]

# if no exist, return default value.(if no default value return none)
# result = d1.get("奥特曼","抱歉，key不存在")
# print(result)

# d1 = {"张三":72,"李四":60,"王五":85}
# d1["赵六"] = 100
# print(d1)

# d1 = {"张三":72,"李四":60,"王五":85}
# d1["张三"] = 97
# print(d1)

# d1.update({"李四":40,"王五":67})
# print(d1)

d1 = {"张三":72,"李四":60,"王五":85}
# del d1["张三"]
# print(d1)

# result = d1.pop("张三")
# print(d1)
# print(result)

# result = d1.pop("奥特曼","删除失败")
# print(d1)
# print(result)

d1.clear()
print(d1)


