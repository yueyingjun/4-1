a=[5,3,1,9,6]
t=0
for i in range(0,4):
    for j in range(0,5-i-1):
        if (a[j]>a[j+1]):
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
print(a)