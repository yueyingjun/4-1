def paixu(l):
    x=0
    c=0
    t=len(l)
    for i in range(0,t):
        x=l[i]
        for j in range(i+1,t):
            c=l[j]
            if x>=c:
                l[i] = l[j]
                l[j]=x
                x=c
        print(str(x)+"  ",end="")

paixu(l=[0,2,3,5,9,0])
