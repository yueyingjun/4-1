#for 循环
def jiujiu(row):
    for i in range(1,row+1):
        for j in range(1,i+1):
            print('%d*%d=%d'%(j,i,j*i),end='\t')
        print()
jiujiu(11)


#while循环
def jiujiu(y):
    i=1
    d = ""
    while i<=y:
        j=1
        while j<=i:
            print('%d*%d=%d'%(j,i,i*j),end='\t')
            j+=1
        print()
        i+=1
jiujiu(6)
