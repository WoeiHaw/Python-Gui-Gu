# file = open(file="a.txt",mode="rt",encoding="utf-8")
file = open("a.txt","rt",encoding="utf-8")

result = file.read()

print(result)
file.close()