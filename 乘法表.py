# 用for循环,输出给定级数的乘法表
def chengfabiao(jishu):
    for hang in range(1, jishu+1):
        for lie in range(1,hang+1):
            if (hang == 3 and lie == 3) or (hang == 4 and lie == 3):
                print("  ", end="")
            else:
                print(" ", end="")
            print("%d*%d=%d" % (hang, lie, hang*lie), end=" ")
        print("")

jishu = int(input("请输入级数："))
chengfabiao(jishu)

# 用while循环,输出给定级数的乘法表
'''
def changfa(i):
    row = 1
    while row < i:
        col = 1
        while col <= row:
            if(row == 3 and col == 3) or (row == 4 and col == 3):
                print("  ",end="")
            else:
                print(" ",end="")
            print("%d*%d=%d" % (row, col, row*col), end=" ")
            col += 1;
        print("")
        row += 1

jishu = int(input("请输入级数："))
chengfabiao(jishu)
'''