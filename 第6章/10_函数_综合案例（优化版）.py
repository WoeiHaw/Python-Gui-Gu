def calc_total(*args):
    """
    计算总运动量
    :param args:每一天的运动量
    :return:总运动量
    """
    return sum(args)

def cal_avg(total,days=7):
    """
    计算平均值
    :param total:总运动量（个）
    :param days: 天数（默认值是7）
    :return: 平均值
    """
    return total/days

def check_success(total,goal=120):
    """
    判断本次挑战是否成功
    :param total: 总运动量
    :param goal: 成功数量（默认值为120）
    :return: 成功或失败的具体信息
    """
    if total >= goal:
        return "恭喜！挑战成功"
    else:
        return "抱歉挑战失败"

def main(title, duration,goal):
    print(f"【{title}】【{duration}天】挑战赛（请输入每天的数量）")
    nums =[]

    for index in range(duration):
        nums.append(int(input(f"请输入第{index+1}天的数据:")))

    total = calc_total(*nums)
    avg = cal_avg(total)
    result = check_success(total,goal)
    print(f"【{title}】【{duration}天】健身总结")
    print(f"总数：{total}，平均值：{avg:.1f}")
    print(result)

main("仰卧起坐",7,40)

