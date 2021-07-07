# 从已排好序的数组中查找给定的元素，找到返回True,找不到返回False
arr = [i for i in range(1001)]
# 折半查找法  ---递归实现查找
def find1(arr,item):
    if arr == []:
        return False
    middle = len(arr)//2
    if arr[middle] == item:
        return True
    if item < arr[middle]:
        return find1(arr[:middle], item)
    else:
        return find1(arr[middle+1:], item)
print(find1(arr,101))
# 折半查找法  ---双游标循环查找
def find2(arr,item):
    if arr == []:
        return False
    left = 0
    right = len(arr)-1
    while left <= right:
        middle = (left+right) // 2
        if arr[middle] == item:
            return True
        elif item < arr[middle]:
            right = middle-1
        else:
            left = middle+1
    return False
print(find2(arr,1002))
