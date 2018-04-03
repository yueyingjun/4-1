def cfb(i):# 九九乘法表
    for i in range(1, i):
        for j in range(1, i + 1):
            d = i * j
            if (i < 10):
                print('%d*%d=%-4d' % (j, i, d), end=' ')
            else:
                print('%d*%d=%-3d' % (j, i, d), end=' ')
        print()
cfb(6)

def star(rows=5):   #形参 参数默认值   杨辉三角
    row = 0
    while row < rows:
        row += 1
        space = 0
        while space < rows - row:
            space += 1
            print(" ", end="")
        star = 0
        while star < 2 * row - 1:
            print("*", end="")
            star += 1
        print("")
star()
star(3)
star(6)
star(10)

for num in range(100, 201): #操场人数
    if (num % 3 == 1 and num % 4 == 2 and num % 5 == 3):
        print(str(num))

for ji in range(1, 36):#鸡兔同笼
    tu=35-ji
    if (  2 * ji + 4 * tu == 94):
        print(str(ji),str(tu))

def px(list2):    #列表排序
    for i in range(0,len(list2)):
        for j in range(i+1,len(list2)):
            if list2[j]<list2[i]:
                t=list2[i]
                list2[i]=list2[j]
                list2[j]=t
    print(list2)
px([3,4,1])
px([6,8,3,2])
px([11,99,5,76,30])
px([3,1,6,48,9,11,4])

