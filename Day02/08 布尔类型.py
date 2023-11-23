# 1.比较表达式
x = 10
y = 3.14

print(x == y)
print(x > y)
print(x <= y)

age = 23
if age > 18:
    print("成人电影")
else:
    print("未成年电影")

# 2.直接使用布尔值
b1 = True
print(b1)
print(type(b1))

# 3.所有数据都有自己的布尔值
print(2 > 1)
print(bool(2 > 1))
# 零值： 所有的数据类型中都有且只有一个值的布尔状态是False，该值成为此类型的零值

# 整型和浮点型的零值是0
print(bool(1))
print(bool(-1))
print(bool(-11))
print(bool(0))

# 字符串的零值是“” 列表的零值是【】字典的零值是{}
print(bool(""))
print(bool("0"))
print(bool("-1"))
print(bool("False"))
print(bool([]))
print(bool({}))
