#for语句的杨辉三角
def yhsj(row,rows):
    print("for语句的杨辉三角：")
    for row in range(1, rows + 1):
        for space in range(0, rows - row):
            print(" ", end="")
        for con in range(0, row * 2 - 1):
            print("*", end="")
        print("")
yhsj(1,5)
#while语句的杨辉三角
def yhsj1(row,rows):
    print("")
    print("while语句的杨辉三角：")
    while row < rows:
        row += 1
        space = 0
        while space < rows - row:
            space += 1
            print(" ", end="")
        star = 0
        while star < 2 * row - 1:
            print("*", end="")
            star += 1
        print("")
yhsj1(0,5)