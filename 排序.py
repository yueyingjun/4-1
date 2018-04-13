def paixu(lists):
    m=len(lists)
    for i in range(0,m):
         for j in range(i+1,m):
            if lists[i]>lists[j]:
              lists[i],lists[j] = lists[j],lists[i]
    print (lists)

paixu([2,5,1,3,8])