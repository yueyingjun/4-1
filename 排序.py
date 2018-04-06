list=[12,3,18,27,4,9,23,16,8,13];#ÅÅĞòÎÊÌâ
t=0
for i in range(0,10):
    for j in range(0,9-i):
        if(list[j]>list[j+1]):
            t=list[j]
            list[j]=list[j+1]
            list[j+1]=t
for a in range(0,10):
    print(list[a],end=" ")