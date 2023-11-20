# 导入一个random模块，获取随机数
import random
# 导入datetime模块，获取时间
import datetime

# 获取1-100的随机数
print(round(random.random() * 100))

# 打印当前时间，格式是年-月-日_时:分:秒
print(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
print(datetime.datetime.now().strftime("%Y-%m-%d_%X"))
