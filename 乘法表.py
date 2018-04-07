def cheng(m):
    x=1;
    while x>0 and x<m+1:
        str1=""
        y=1;
        space=""
        while y>=1 and y<x+1:
            if (x==3 and y==2) or (x==4 and y==2):
                space="  "
            else:
                space=" "
            str1+=(str(x)+"*"+str(y)+"="+str(x*y)+space)
            y+=1
        print(str1)
        x+=1
cheng(5)
