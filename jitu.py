def jitu(x,y,z):
    for a in range(1, x):
        b = y - a
        if (2 * a + 4 * b == z):
            print("鸡有" + str(a) + "只", "兔有" + str(b) + "只");

jitu(36,35,94)
