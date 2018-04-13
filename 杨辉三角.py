
'''rows=6
for row in range (0,rows):
    for space in range(0,rows-row-1):
        print(" ",end="")
    for star in range(0,(row+1)*2-1):
        print("*",end="")
    print("  ")
'''
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

yanghuisanjiao(3)
yanghuisanjiao(5)
