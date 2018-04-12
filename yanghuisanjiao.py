rows=5
for row in range(1,rows+1):
    for space in range(0,rows-row):
        print(" ",end="")
    for con in range(0,row*2-1):
        print("*",end="")
    print("")