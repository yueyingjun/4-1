# 操场上有100-200人，3余1,4余2，5余3，问操场上人数
def caochang(i, j):  # i,j为操场上人数的限制数量
    for i in range(i, j + 1):
        if i % 3 == 1 and i % 4 == 2 and i % 5 == 3:
            print(i)


caochang(200, 300)