#降序排列
def paixu(shuzu):
    n=len(shuzu);
    for i in range(0,n):
        for j in range(i+1,n):
            if shuzu[i]<shuzu[j]:          #升序排列将大于号转变为小于号
                temp=shuzu[i]
                shuzu[i]=shuzu[j]
                shuzu[j]=temp
    print("排列后的数组："+str(shuzu))
paixu([9,8,7,6,5,4,0,1,2,3])