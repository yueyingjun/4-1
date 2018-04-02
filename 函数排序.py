#冒泡排序
def list(a):
    for i in range(len(a)-1):#len()字符串长度*
        for j in range(len(a)-1-i):#n-1、n-2、n-3...
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    print(a)

list([34,65,35,675])

