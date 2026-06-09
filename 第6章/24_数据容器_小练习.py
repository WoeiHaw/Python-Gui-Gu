# fruits ={
#     "苹果":4.5,
#     "香蕉":3.2,
#     "橙子":5.8,
#     "草莓":12.0,
#     "哈密瓜":8.8
# }
#
# for key in fruits:
#     print(f"{key}:{fruits[key]}元/斤")
# key = max(fruits,key=fruits.get)
# print(f"最贵的水果是{key}，价格是{fruits[key]} 元/斤")

students = [
    {
        "name": "李四",
        "scores": {"语文": 75, "数学": 83, "英语": 80}
    },
    {
        "name": "张三",
        "scores": {"语文": 88, "数学": 92, "英语": 95}
    },

    {
        "name": "王五",
        "scores": {"语文": 92, "数学": 95, "英语": 88}
    },
]


# for student in students:
#    score_list =  student['scores'].values()
#    avg = sum(score_list)/len(score_list)
#    print(f"{student["name"]}平均成绩是：{avg:.2f}")

# def find_best():
#     best_students = []
#     best_score = 0
#     for stu in students:
#         total = sum(stu["scores"].values())
#         if total > best_score:
#             best_students = [stu["name"]]
#             best_score = total
#         elif total == best_score:
#             best_students.append(stu["name"])
#     print(f"最高分为{best_score}，取得最高分的学生有{best_students}")
#
#
# find_best()

comment = "这家奶茶真好喝，环境也不错，就是价格有点贵，好喝好喝好喝！强烈推荐！"
print(comment.count("好喝"))
comment2 = comment.replace("贵","略高")
print(comment2)

print("推荐" in comment)