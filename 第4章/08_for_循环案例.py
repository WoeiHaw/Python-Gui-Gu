# 加密代码
# text = input('请输入要加密文件:')
# secret = ''
#
# for t in text:
#     unicode = ord(t)
#     secret += chr(unicode+1)
# print(f'经过加密后的内容为:{secret}')

# 解密代码
secret = input('请输入要解密文字:')
text = ''

for s in secret:
    unicode = ord(s)-1
    text += chr(unicode)
print(f'经过解密后的内容为:{text}')