def paidui(x,y):
    for a in range(x,y):
        if a%3==1 and a%4==2 and a%5==3:
            print("操场可能有"+str(a)+"人")


paidui(100,200)