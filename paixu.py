def paixu(list=[63,55,6,7,488,524,595,24,21]):
    n = len(list)
    i=0
    j=0
    for i in range (0,n):
        for j in range (i+1,n):
            if list[i]>=list[j]:
                a=list[j]
                list[j]=list[i]
                list[i]=a
            else:
                continue
    print(list)
paixu()



