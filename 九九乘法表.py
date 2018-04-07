def jiujiu(n):
    for i in range (1,n+1):
        for j in range (1,i+1):
            print("%d*%d=%2d" % (i,j,i*j),end="  ")
        print("  ")
jiujiu(5)
'''
i = 1
while i < 10:

    j=1
    while j <= i:
        print("%d*%d=%2d" % (i,j,i*j),end="  ")
        j+=1
    i+=1
    print(" ")

'''