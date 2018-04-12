def jitutonglong(tou,jiao):
    ji=1
    for ji in range(1,tou+1):
        if ji*2+(tou-ji)*4==jiao:
            print("鸡有:%d只,兔有:%d只"%(ji,tou-ji));
            break

jitutonglong(35,116)