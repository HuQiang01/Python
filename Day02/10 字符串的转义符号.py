# 转义符 \
# 1.将某些普通符号给予特殊功能
# 2.将特殊功能的符号普通话
# \n 换行
# \t 制表位
s = "i am panghu\nmy age is 18 years old"
print(s)
s1 = "i am panghu\t\tmy age is 18 years old"
print(s1)

s2 = "let's go!"
s3 = 'let\'s go!'
print(s2)
print(s3)

path = "/user/local/bin/a.py"
path1 = "\\user\\local\\bin\\b.py"
print(path)
print(path1)
