def caochang(m,n):#人数范围
    for x in range (m,n):
        if x % 3==1 and x%4==2 and x%5==3:
            print(x)
caochang(50,150)
