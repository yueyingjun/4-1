def tongji(x):
    for num in range(100,x):
        if num%3 == 1 and num%4 == 2 and num%5 == 3:
            print("操场上的人数：",num)

tongji(200)