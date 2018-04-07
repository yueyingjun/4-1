def tonglong(x,y):
    for ji in range(0,x):
        tu=x-ji
        if ji*2+tu*4==y:
            print("鸡有:%d只,兔有:%d只" %(ji,tu))
tonglong(35,94)

