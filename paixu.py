def paixu(a):
    i = 0
    for i in range(0,len(a)):
        for j in range(i,len(a)):
            if a[i] <= a[j]:
                j += 1
            else:
                k = a[i]
                a[i] = a[j]
                a[j] = k
        i += 1
    print(a)

paixu([3,5,1,8,6,7,2])