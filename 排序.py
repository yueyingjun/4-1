l=[25,6,34,98,33]
for x in range(1,len(l)+1):
    for y in range(1,(len(l)+1)-x):
        if l[y-1]>l[y]:
            t=l[y-1]
            l[y-1]=l[y]
            l[y]=t;
    print(l)
