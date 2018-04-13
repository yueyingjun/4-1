def jitu(h = 35, t = 94):
    ji = 0
    tu= 35
    while(ji <= h):
        if ji*2+tu*4 == t:
            print("ji:",ji)
            print("tu:",tu)
            break
        else:
            ji = ji+1
            tu = tu-1
jitu()