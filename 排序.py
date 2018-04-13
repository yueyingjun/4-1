def paixu(shuzu):
    n=len(shuzu);
    for i in range(0,n):
        for j in range(i+1,n):
            if shuzu[i]>shuzu[j]:
                temp=shuzu[i]
                shuzu[i]=shuzu[j]
                shuzu[j]=temp
    print("排列后的数组："+str(shuzu))
paixu([45,67,12,5,100,56,88,3])