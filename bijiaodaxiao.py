a=[11,51,48,95,2,78,29,84,56,79,54]
h=len(a)
for x in range(0,h):
    for y in range(x,h):
        if a[x]>a[y]:
            m=a[x]
            a[x]=a[y]
            a[y]=m


print(a)