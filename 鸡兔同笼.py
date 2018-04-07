def number(n):
    for i in range (1,n+1):
        j=n-i
        if (2*i+4*j==94):
            print("鸡有%d ,兔子有%d" %(i,j))
    print("")
number(47)