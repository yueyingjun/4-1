def chengfabiao(start,end):
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
chengfabiao(1,10)