# 用while循环输出杨辉三角
'''
def yang(rows):
	row=0
	while row < rows:
		col = 1
		row += 1
		space = 1
		while space <= rows-row:
			space += 1
			print(" ", end="")
		while col <= (row*2-1):
			print("*", end="")
			col+=1
		print("")

rows = int(input("输入杨辉三角的级数:"))
yang(rows)
'''

# 用for循环输出杨辉三角
def yang(rows):
	for row in range(1,rows+1):
		for space in range(0,rows-row):
			print(" ",end="")
		for col in range(0,row*2-1):
			print("*", end="")
		print("")

rows = int(input("输入杨辉三角的级数:"))
yang(rows)
