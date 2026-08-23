import asyncio
async def work():
    print("work开始")
    print("work执行中。。。。。。")
    print("work结束")
    return "工作结果"

coroutine_object = work()

result = asyncio.run(coroutine_object)
print(result)
