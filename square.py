def renshu(n1):
    for n in range (100,n1):
        if (n%3==1 and n%4==2 and n%5==3):
            print ("n=",n)
renshu(150)