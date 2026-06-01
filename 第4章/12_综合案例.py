print("欢迎来到：答题闯关挑战赛 （输入q可随时退出 \n")

ques1, ans1 = 'Python中用于输出的函数是？', "print"

ques2, ans2 = 'Python中用于表示逻辑“并且”的关键字是？', "and"

ques3, ans3 = 'Python属于编译型还是解释型', "解释型"

max_tries = 3

total_level = 3

is_playing = True

for level in range(1, total_level + 1):
    print(f"*************第{level}关*************")

    if level == 1:
        question, answer = ques1, ans1
    elif level == 2:
        question, answer = ques2, ans2
    else:
        question, answer = ques3, ans3
    tries = 1
    while tries <= max_tries:
        user_input = input(question)

        if user_input == answer:
            print("回答正确！\n")
            break
        elif user_input == "":
            print("你的输入为空， 请重新做答")
            continue
        elif user_input == "q":
            print("你已退出游戏！\n")
            is_playing = False
            break
        else:
            leave = max_tries - tries
            if leave > 0:
                print(f"回答错误，你还有{leave}机会")
                tries += 1
                continue
            else:
                print(f"挑战失败，本题正确答案是：{answer},游戏结束")
                is_playing = False
                break
    # 每次进入下一关时，就要看一下 is_playing
    if not is_playing:
        break
# 如果到了这里，is_playing == True, 那就意味着已通贯
if is_playing:
    print("恭喜您！！，全部通过")
