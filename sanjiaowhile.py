def saojiaowhile(rows=3):
    row = 1
    while row < rows + 1:
        space = 0
        while space < rows - row:
            space += 1
            print(" ", end="")
        star = 0
        while star < 2 * row - 1:
            print("*", end="")
            star += 1
        print("")
        row += 1
saojiaowhile(10)