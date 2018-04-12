def caochangwenti(start,end):
    for num in range(start,end+1):
        if (num%3)==1and(num%4)==2and(num%5)==3:
            print(num)

caochangwenti(120,200)