s = "hello world"

# 1.索引操作： 字符串[索引] 查询字符
print(s[6])
print(s[0])
print(s[9])
print(s[-1])
print(s[-2])

# 2.切片操作： 字符串[开始索引：结束索引] 包头不包尾
print(s[0:6])
print(s[6:9])
print(s[6:-1])
print(s[6:])  # 缺省，取到最后一个值
print(s[:5])  # 缺省，从0开始取值
print(s[:])
print(s[::2])
print(s[::-1])  # 字符串翻转
print(s[-5:-10:-1])
print(s[5:0:-1])

# 3.拼接 +
s1 = "hello"
s2 = " world"
print(s1 + s2)

name = "乔沃德"
age = "18"
s3 = f"我的名字是{name}， 我的年龄是{age}"
print(s3)
print("我的名字是" + name + "我的年龄是" + age)

print("**************************************")
print("*" * 20)

# 4.计算字符串对象的长度： 元素的个数 解释器内置函数 len
s4 = "hello world"
print(len(s4))

# 5.针对容器类型： in判断 判断某个成员是否存在
s6 = "rain cats and dogs "
print("rain" in s6)
print("rai" in s6)
print("s a" in s6)
print("ri" in s6)



