def jitutonglong(m,n): #头和脚 #
    for x in range(0,m+1):
         y = m - x;
         if x * 2 + y * 4 == n:
             print(x)
             print(y)
jitutonglong(35,94)


