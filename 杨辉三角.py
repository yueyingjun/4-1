def yanghuisanjiao(rows):
    row = 0;

    while row < rows:
        row += 1
        space = 0
        while space < rows - row:
            space += 1
            print(" ", end="")
        star = 0
        while star < row * 2 - 1:
            print("*", end="")
            star += 1
        print("")

yanghuisanjiao(8)