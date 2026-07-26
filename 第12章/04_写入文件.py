# with open("b.txt","wt",encoding="utf-8") as file:
#     file.write("你好")
import time

# with open("demo.txt","xt",encoding="utf-8") as file:
#     file.write("你好")


# with open("a.txt","at",encoding="utf-8") as file:
#     file.write("你好")

# with open("demo.txt","at",encoding="utf-8") as file:
#     file.write("你好1")
#     file.write("你好2")
#     file.flush()
#     time.sleep(1000)
#     file.write("你好3")
#     file.write("你好4")

with open("a.txt","rt+",encoding="utf-8") as file:
    file.seek(0,0)
    file.write("你好23grgfgf")