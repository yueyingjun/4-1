def jitutonglong(m=35,n=94):
    for x in range(0,m):
        if x*2+(m-x)*4==n:
            print("鸡有"+str(x)+"只，兔有"+str(m-x)+"只")

jitutonglong(2,6)