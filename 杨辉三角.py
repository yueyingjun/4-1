#for循环
def yanghui(rows):
    for row in range(1,rows+1):
        for space in range(0,rows-row):
            print(" ",end="")
        for star in range(0,row):
            print("*",end=" ")
        print()
yanghui(8)



#while循环
def yanghui(rows):
    row=0
    while row<rows:
        row += 1
        space=0
        while space<rows-row:
            space+=1
            print(" ",end="")
        star=0
        while star<2*row-1:
            print("*",end="")
            star+=1
        print("")
yanghui(7)
