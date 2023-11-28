"""
if 表达式1:
    语句1:
    语句2:
elif 表达式2：
    语句3:
    语句4:
elif 表达式3：
    语句5:
    语句6:
else:
    语句7:
    语句8:
"""

height = float(input("请输入你的身高："))
weight = float(input("请输入你的体重："))

BMI = weight / height ** 2
print(f"您的BMI是{BMI}")

if BMI < 18.5:
    print("偏瘦")
elif 18.5 < BMI < 24:
    print("正常")
elif 24 < BMI < 28:
    print("超重")
else:
    print("肥胖")
