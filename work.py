def sort(list):
    for i in range(1, len(list)):
        min = list[i]
        j = i - 1
        while j >= 0 and list[j] > min:
            list[j+1] = list[j]
            j -= 1
            list[j+1] =min
    print(list)
sort(list=[9,5,6,4,8,2])
def chengfabiao(row ):
    for row in range(1, row+1):
        str1 = ''
        for col in range(1, row + 1):
            if (row == 3 and col == 2) or (row == 4 and col == 2):
                space = "  "
            else:
                space = " "
            str1 += (str(row) + "*" + str(col) + "=" + str(row * col) + space)
        print(str1)
chengfabiao(8)
def yanghuisanjiao(rows):
    for row in range(1, rows + 1):
        for space in range(0, rows - row):
            print(" ", end="")
        for con in range(0, row * 2 - 1):
            print("*", end="")
        print("")
yanghuisanjiao(7)
i=100
while 100<=i<=200:
    i+=1
    if i%3==1 and i%4==2 and i%5==3:
         print(i)

for ji in range(1,36):
    tu = 35 - ji
    if ji * 2 + tu * 4 == 94:
        print(str(ji)+"--"+str(tu))
