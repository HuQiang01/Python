# 5.split,将字符串切片成列表
s5 = "北京 南京 东京 西京"
print(s5.split())

# 6.join,将字符串或者列表用某种符号切片
s6 = ["东海", "西海", "南海", "北海"]
s66 = ",".join(s6)
s666 = "".join(s6)
print(s66)
print(s666)

# 7.find,查找字符串是否有此字符，有则返回第一索引位，无则返回-1
s7 = "Hello World"
print(s7.find("H"))
print(s7.find("h"))

# 8.index,查找字符串是否有此字符，有则返回第一索引位，无则报错
s8 = "Hello World"
print(s8.index("W"))
# print(s8.index("w"))

