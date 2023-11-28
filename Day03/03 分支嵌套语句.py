pid = input("请输入你的身份证号：")

# 身份证号位数是否是18位置
if len(pid) == 18:
    print("打印个人基本信息")
    # (1）打印性别，身份证号倒数第二位如果是偶数代表女生，否则男生
    print(pid)
    num = int(pid[16])
    if num % 2 == 0:
        print("性别：女")
    else:
        print("性别：男")
    # （2）打印籍贯
    jiGuanCode = pid[:6]
    print("jiGuanCode", jiGuanCode)
    if jiGuanCode == "100000":
        print("籍贯：北京市")
    elif jiGuanCode == "120000":
        print("籍贯：天津市")
    elif jiGuanCode == "340210":
        print("籍贯： 芜湖市")
    else:
        print("无匹配")
else:
    print("输入位数有误")
print("程序结束")
