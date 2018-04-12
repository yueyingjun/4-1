#for语句的9*9乘法表
def chengfa(start,end):
    print("for语句的九九乘法表：")
    for row in range(start, end):
        str1 = "";
        for col in range(start, row + start):
            if row >= col:
                if (row == 3 and col == 2) or (row == 4 and col == 2):
                    space = "    "
                else:
                    space = "   "
                str1 += (str(col) + "*" + str(row) + "=" + str(row * col) + space)
        print(str1)
chengfa(1,10)
#while语句的9*9乘法表
def chengfa1(n):
    print("")
    print("while语句的九九乘法表：")
    hang = 0;
    while hang < n:
        hang += 1;
        lie = 1
        while hang >= lie:
            if (hang == 3 and lie == 2) or (hang == 4 and lie == 2):
                space = "    "
            else:
                space = "   "
            print("%d*%d=%d" % (lie, hang, hang * lie)+space, end=" ")
            lie += 1;
        print("  ")
chengfa1(9)