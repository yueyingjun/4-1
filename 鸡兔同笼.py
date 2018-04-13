def jitu(tou,jiao):
    for x in range(0,tou+1):
        for y in range(0, tou+1):
            if (2 * x + 4 * y == jiao and x + y == tou):
                print("鸡有：%d只  兔有:%d只" %(x,y))
jitu(35,94)