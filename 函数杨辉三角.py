#for语句实现
def stars(rows):
    for row in range(1, rows + 1):
        for space in range(0, rows - row):
            print(" ", end="")
        for can in range(0, row * 2 - 1):
            print("*", end="")
        print("")

stars(8)


#while语句实现
# def yanghui(j):
#     i=1
#     j=10
#     while i<=j:
#         print(" "*(j-i),"*"*(2*i-1))
#         i+=1
#
# yanghui(8)