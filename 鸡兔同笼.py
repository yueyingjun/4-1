# 用for循环，解决鸡兔同笼问题
def jitu(tou, jiao ):
    for ji in range(1, tou+1):
        tu = tou-ji
        if (ji*2)+(tu*4) == jiao:
            print("鸡有%d只  兔有%d只" % (ji, tu))


tou = int(input("输入头的数量："))
jiao = int(input("输入脚的数量："))
jitu(tou, jiao)

# 用while循环，解决鸡兔同笼问题
'''
def jitu(tou,jiao):
    ji=0
    tu=0
    while ji < tou:
        ji += 1
        tu = tou-ji
        if (ji * 2) + (tu * 4) == jiao:
            print("鸡有%d只  兔有%d只" % (ji, tu))


tou = int(input("输入头的数量："))
jiao = int(input("输入脚的数量："))
jitu(tou, jiao)
'''




