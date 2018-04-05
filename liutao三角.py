def stars(n):
    #n = int(input("请输入杨惠三角的行数"))
    row = 0
    while row < n:
        row += 1
        col = 0
        while col <= n - row:
            col += 1
            print(" ", end=" ")
        abc = 0
        while abc <= 2 * row - 2:
            abc += 1
            print("1", end=" ")
        print("")


stars(5)

