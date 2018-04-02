def sort(a):
    for i in range(0,len(a)):
        for j in range(1,len(a)-i):
            if (a[j-1]>a[j]):
                a[j-1],a[j] = a[j],a[j-1]
    print(a)
sort([6,8,3,2,11,4,10])
