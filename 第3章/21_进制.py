# 0b开头表示二进制
num1 = 0b11001
# 0o 开头表示八进制
num2 = 0o1034
# ox开头表示十六进制
num3 = 0x1cf

print(num1, num2, num3)
print(num1 + 1)
print(str(num2))
print(num3 > 400)

result1 = bin(25)
result2 = oct(540)
result3 = hex(463)
print(result1,result2,result3)
print(type(result1),type(result2),type(result3))

value1=int('0b11001',2)
value2 = int('0o1034',8)
value3 = int('0x1cf',16)
print(value1,value2,value3)
print(type(value1),type(value2),type(value3))
