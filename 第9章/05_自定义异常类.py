class SchoolNameError(Exception):
    def __init__(self,msg):
        super().__init__("【校名异常】"+ msg)


def check_school_name(name):
    if len(name) > 18:
        raise SchoolNameError("学校名过长")
    else:
        print("学校名是合法的")

# raise SchoolNameError("学校名过长")
# raise SchoolNameError("学校名包含敏感词汇")

try:
    check_school_name("xrtcdhgsvdjksfbjfbdkjfbdjkbfkdbf")
except SchoolNameError as e:
    print(f"程序异常：{e}")
