def s(n):
    for x in range(1,n+1):
        for y in range(1,n+x):
            if y>n-x:
                print("1",end="")
            else:
                print(" ",end="")
        print("")
s(8)
s(5)
