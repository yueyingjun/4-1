def sort(L):
    for i in range(0,len(L)):
        for j in range(i,len(L)):
            if(L[i]>L[j]):
                t=L[i]
                L[i]=L[j]
                L[j]=t
        print(L)
sort([12,87,4,7,2])