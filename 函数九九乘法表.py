#while语句的九九乘法表
# def chengfabiao(rows):
#     row=1
#     while row<=rows:
#         col=1
#         while col<=row:
#             print("%d*%d=%d" %(col,row,col*row), end="\t")
#             col+=1
#         print("")
#         row+=1
#
# chengfabiao(9)
# chengfabiao(10)


#for语句的九九乘法表
def stars(rows):
    start = 1;
    for row in range(start, rows):
        str1 = " "
        space = " "
        for col in range(1, row + 1):
            if (row == 3 and col == 2) or (row == 4 and col == 2):
                space = "  "
            else:
                space = " "
            str1 += (str(row) + "+" + str(col) + "=" + str(row * col) + space)
        print(str1);


stars(9)
stars(10)