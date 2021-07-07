# 用for循环,统计给定范围的人数
def tongji(xia, shang):
    for i in range(xia, shang):
        if (i%3 == 1) and (i%4 == 2) and (i%5 == 3):
            print("操场上的人数为：", i, "人")


xia = int(input("输入操场上人数的下限："))
shang = int(input("输入操场上人数的上限："))
tongji(xia, shang)

# 用while循环，统计给定范围的人数
'''
def tongji(xia, shang):
    i = xia
    while i <= shang:
        i += 1
        if (i%3 == 1) and (i%4 == 2) and (i%5 == 3):
            print("操场上的人数为：", i, "人")


xia = int(input("输入操场上人数的下限："))
shang = int(input("输入操场上人数的上限："))
tongji(xia, shang)
'''