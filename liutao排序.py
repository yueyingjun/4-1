def stars(lb):
    print("列表:",lb)
    for i in range(1,len(lb)+1):
        for j in range(1,(len(lb)+1)-i):
            if (lb[j-1] > lb[j]):
                n = lb[j-1];
                lb[j-1] = lb[j];
                lb[j] = n;
    print("排序后的列表:",lb)

stars([58,27,56,16,89,77,66])