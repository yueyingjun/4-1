def jiujiuchengfabiao():
    for h in range(1,10):
         for l in range(1,h+1):
            print("%s*%s=%s " % (l, h, l * h), end="\t")
         print()
jiujiuchengfabiao()