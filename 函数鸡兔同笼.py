def jitu(i,j):#i为鸡和兔的总个数，j为鸡兔的足数
    for ji in range(1, i+1):
        tu = i - ji
        if ji * 2 + tu * 4 == j:
            print(str(ji) + "--" + str(tu))


jitu(35,94)