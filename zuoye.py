def px(a):
    n=len(a)
    for i in range (1,n):
        for j in range (0,n-i):
            if a[j]>a[j+1]:
                min=a[j]
                a[j]=a[j+1]
                a[j+1]=min
    print(a)
px(a=[3,5,1,4])