# -*- coding=utf-8 -*-
f = open("文件模板.txt", mode="r+")
# 1.将文件写入内存
date = f.read()
new_date = date.replace("黄忠", "刘备")
# 2.清除文件内容
f.seek(0)
f.truncate()
# 3.新写入文件内容
f.write(new_date)
f.close()

