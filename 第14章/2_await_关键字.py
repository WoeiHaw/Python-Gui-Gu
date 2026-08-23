import asyncio
async def work():
    print("work开始")
    print("work执行中。。。。。。")
    res = await asyncio.sleep(2)
    print(res)
    print("work结束")
    return "工作结果"
async def main():
    print("main开始")
    res = await work()
    print(res)
    print("main结束")
    return "main的返回值"

result = asyncio.run(main())
print(result)