#for语句的操场人数问题
def paidui(min,max):
    for num in range(min, max+1):
        if (num % 3 == 1 and num % 4 == 2 and num % 5 == 3):
            print("操场人数为："+str(num))
paidui(100,200)
#while语句的操场人数问题
def paidui1(num):
    while (num>100 and num<200 ):
        num+=1
        if (num % 3 == 1 and num % 4 == 2 and num % 5 == 3):
            print("操场人数为："+str(num))
paidui1(101)
