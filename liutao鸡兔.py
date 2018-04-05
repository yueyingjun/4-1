'''for a in range(0,35):
    for b in range(0,35):
        if(a*2+b*4==94) and (a+b==35):
            print(str(a),str(b))
'''



def stars(n):
    for a in range(1, n+1):
        b = n - a
        if (a * 2 + b * 4 == 94):
            print(str(a), str(b))

stars(35)
