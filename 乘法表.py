def chengfabiao(rows):
    start = 1;

    for row in range(start, rows):
        str1 = ""
        space = " "
        for col in range(1, row + 1):
            if (row == 3 and col == 2) or (row == 4 and col == 2):
                space = "  "
            else:

                space = " "
            str1 += (str(row) + "*" + str(col) + "=" + str(row * col) + space)
        print(str1)
chengfabiao(20)