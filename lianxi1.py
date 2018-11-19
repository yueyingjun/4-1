# 1.有0~1000的a,b,c三个值，如果这三个值的和等于1000同时满足a的平方+b的平方=c的平方，求a,b,c分别是多少
def abc():
    for a in range(0,1001):
        for b in range(0,1001):
            c=1000-a-b
            if (a**2+b**2==c**2 and a+b+c==1000):
                print(a,b,c)
abc()
# 2.鸡兔同笼，共35只头，足有94只，鸡兔分别多少只？
def jitu(tou,jiao):
    ji=0
    while ji<=tou:
        tu = tou - ji
        if (ji+tu==tou and ji*2+tu*4==jiao):
            print(("鸡有%d只,兔有%d只")%(ji,tu))
        ji += 1
jitu(35,94)
# 3.求指定数字以内的素数
def sushu(num):
    i = 2
    c = []
    while i <= num:
        j = 2
        while j <= i:
            if i % j == 0:
                if i == j:
                    c.append(i)
                break
            j += 1
        i += 1
    print("%d以内的素数有:"%(num),c)
sushu(100)
# 4.求指定数字个数的斐波拉契数列
def feibo(num):
    a=0
    b=1
    arr=[]
    for i in range(num):
        arr.append(b)
        a, b = b, a + b
    print("%d个斐波拉契数:"%(num),arr)
feibo(20)
print(6765/4181)
