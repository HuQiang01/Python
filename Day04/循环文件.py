# -*- coding=utf-8 -*-
f = open("循环文件")
for line in f:
    line = line.split()
    weight = int(line[3])
    height = int(line[2])
    if weight >= 70 and height >= 160:
        print(line)
