'''#while循环
i=1
i+=1
while i<=35:
    j=1
    while j<i:
        j=35-i
        if (2*i+4*j==94):
            print(i,j)
        i+=1
'''

#for循环
for i in range(1,36):
    j=35-i
    if(2*i+4*j==94):
        print(i,j)