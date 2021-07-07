# 用冒泡法处理列表排序问题
def sort(list):
    print("原列表:",list)
    for i in range(1,len(list)+1):
        for j in range(1,(len(list)+1)-i):
            if (list[j-1] > list[j]):
                temp = list[j-1];
                list[j-1] = list[j];
                list[j] = temp;
    print("递增排序后的列表:",list)

sort([45,12,9,67,24,103,45,17,5])
