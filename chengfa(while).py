def jiujiuchengfabiao(hangshu=9):
    hang=1
    while hang<=hangshu:
        lie=1
        while lie<=hang:
            print("%d*%d=%d"%(lie,hang,hang*lie),end="\t")
            lie+=1
        print("")
        hang+=1

jiujiuchengfabiao(6)