def stars(n):
    a=[1,3,2,5,7]
    t=0
    for i in range (0,n):
        for j in range (0,n-i-1):
            if a[j]>a[j+1]:
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
    print(a)
stars(5)