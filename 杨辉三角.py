def aas ():
    rows = int(input("������������ǵ�����"))
    a = rows + 1;
    start = 1;
    for row in range(start, a):
        for var in range(start, rows + row):
            if (var > rows - row):
                print(1, end="  ")
            else:
                print(" ", end="  ")
        print("")
aas()