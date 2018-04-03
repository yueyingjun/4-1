def chenfabiao(b):
    for row in range(1,b):
        str1=""
        space=""
        for col in range(1,row+1):
            if (row==3 and col==2) or (row==4 and col==2):
                space="  "
            else:
                space=" "
            str1+=(str(col)+"*"+str(row)+"="+str(row*col)+str(space))
        print(str1);

chenfabiao(15)

