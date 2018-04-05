def stars(n):
    for row in range(1, n+1):
        space=" "
        for col in range(1, row + 1):
            print("%2d*%d=%2d" % (row, col, row * col), end=space)
        print("")

stars(11)