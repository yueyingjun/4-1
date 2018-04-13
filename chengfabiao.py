def chengfbiao(rows=12):
    for row in range(1, rows):
        str1 = ""
        space = ""
        for col in range(1, row + 1):
            if (row == 3 and col == 2) or (row == 4 and col == 2):
                space = "  "
            else:
                space = " "
            str1 += (str(row) + "*" + str(col) + "=" + str(row * col) + space)
        print(str1);
chengfbiao()