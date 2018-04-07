def caochang(x,y):
    for ren in range(x,y):
        if ren%3==1 and ren%4==2 and ren%5==3:
            print("有%d人" %ren)
caochang(200,300)