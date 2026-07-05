num: int = 100
price: float = 12.5
message: str = "你好啊"
is_vip: bool = True
result: None = None  # 语法上没有问题。但这么写没有意义

school: str
print("***********")
school = "尚硅谷"

hobby: list[str] = ["抽烟", "喝酒", "烫头"]
hobby.append("学习")

hobby: list[str | int] = ["抽烟", "喝酒", "烫头"]
hobby.append("学习")
hobby.append(100)
from typing import Union

hobby: list[Union[str, int]] = ["抽烟", "喝酒", "烫头"]

cities: set[str] = {"北京", "上海", "深圳"}

cities: set[str | float | bool] = {"北京", "上海", "深圳"}
cities.add(12.5)
cities.add(True)

persons: dict[str, int] = {"张三": 18, "李四": 19, "王五": 20}

persons: dict[str | int, int] = {"张三": 18, "李四": 19, "王五": 20}
persons[250] = 21

scores: tuple[int, int, int] = (60, 60, 70)
scores: tuple[int, ...] = (60, 60, 70, 100, 34, 67)
scores: tuple[int | str, ...] = (60, 60, "70", 100, 34, "67")

y = [10, 20, 30]
y.append("40")
y = 100
