# 冒泡排序
arr1 = [23, 1, 12, 5, 33, 78, 45, 21, 11, 101, 66, 8]
def maopao(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
print("冒泡  排序:",maopao(arr1))
# 选择排序
arr2 = [23, 1, 12, 5, 33, 78, 45, 21, 11, 101, 66, 8]
def xuanze(arr):
    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
            temp = arr[i]
            arr[i] = arr[minIndex]
            arr[minIndex] = temp
    return arr
print("选择  排序:",xuanze(arr2))
# 插入排序
arr3 = [23, 1, 12, 5, 33, 78, 45, 21, 11, 101, 66, 8]
def charu(arr):
    for i in range(1, len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and current < arr[preIndex]:
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex+1] = current
    return arr
print("插入  排序:",charu(arr3))
# 希尔排序
arr4 = [23, 1, 12, 5, 33, 78, 45, 21, 11, 101, 66, 8]
def xier(arr):
    leng = len(arr)
    val = leng//2
    while val > 0:
        for i in range(val, leng):
            preIndex = i-1
            current = arr[i]
            while preIndex >= 0 and current < arr[preIndex]:
                arr[preIndex+1] = arr[preIndex]
                preIndex -= 1
            arr[preIndex+1] = current
        val = val//2
    return arr
print("希尔  排序:",xier(arr4))
# 快速排序
arr5 = [23, 1, 12, 5, 33, 78, 45, 21, 11, 101, 66, 8]
def kuaisu(arr,start,end):
    if start >= end:
        return
    left = start
    right = end
    temp = arr[left]
    while left < right:
        while left < right and temp < arr[right]:
            right -= 1
        arr[left] = arr[right]
        while left < right and temp > arr[left]:
            left += 1
        arr[right] = arr[left]
    arr[left] = temp
    kuaisu(arr, start, left-1)
    kuaisu(arr, left+1, end)
    return arr
print("快速  排序:",kuaisu(arr5,0,len(arr5)-1))
# 桶排序
arr6 = [23, 1, 12, 5, 33, 78, 45, 21, 11, 101, 66, 8]
def tong(arr):
    big = max(arr)
    bucket = [0]*(big+1)
    for i in arr:
        bucket[i] += 1
    newarr = []
    for index in range(len(bucket)):
        if bucket[index] != 0:
            for item in range(bucket[index]):
                newarr.append(index)
    return newarr
print("木桶  排序:",tong(arr6))

# 堆排序
arr7 = [23, 1, 12, 5, 33, 78, 45, 21, 11, 101, 66, 8]
def big(arr7,start,length):
    next = start * 2 + 1
    while next < length:
        if next+1 < length and arr7[next] < arr7[next+1]:
            next += 1
        if arr7[start] < arr7[next]:
            arr7[start], arr7[next] = arr7[next], arr7[start]
            start = next
        else:
            break
        next = next*2+1
for i in range(len(arr7)//2-1, -1, -1):
    big(arr7, i, len(arr7))
for i in range(len(arr7)-1, -1, -1):
    temp = arr7[i]
    arr7[i] = arr7[0]
    arr7[0] = temp
    big(arr7, 0, i)
print("大顶堆排序:", arr7)
