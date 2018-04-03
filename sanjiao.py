def yang(b):
    a = "*"
    space = " "
    for row in range(1, b):
        str1 = str(space) * (b - row) + str(a) * (2 * row - 1)
        print(str1);
yang(10)