score_list = [62,50,60,48,80,20,95]

# index = 0
# while index < len(score_list):
#     print(score_list[index])
#     index+=1

# for item in score_list:
#     print(item)

# for index in range(len(score_list)):
#     print(score_list[index])

for index, item in enumerate(score_list,start=5):
    print(index,item,score_list[0])
print("最后的打印",score_list[0])

