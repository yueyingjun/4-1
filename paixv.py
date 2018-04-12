def maopao(a):
    for i in range(0,len(a)-1):
        for j in range(0,len(a)-1-i):
            if a[j]>a[j+1]:
                temp=a[j+1];
                a[j+1]=a[j];
                a[j]=temp;
    print(a)
maopao([8,4,5,2,1])