'''n1=8
for n in range (1,n1+1):
    for b in range (0,n1-n):
        print(" ",end=" ")
    for a in range (0,2*n-1):

    print("")
'''
def yanghui(n1):
    i=1
    while (i<n1+1):
        j=0
        space=0
        while (space<n1-i):
            print(" ", end="")
            space+=1
        while (j<2*i-1):
            print("j",end="")
            j+=1
        i+=1
        print("")
yanghui(5)