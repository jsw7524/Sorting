def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = mergeSort(arr[:mid])
    right_half = mergeSort(arr[mid:])

    return merge(left_half, right_half)

def merge(left_half, right_half):
    result=[]
    leftIndex, rightIndex = 0, 0
    while leftIndex < len(left_half) and rightIndex < len(right_half):
        if left_half[leftIndex] < right_half[rightIndex]:
            result.append(left_half[leftIndex])
            leftIndex += 1
        else:
            result.append(right_half[rightIndex])
            rightIndex += 1
    if leftIndex < len(left_half):
        result.extend(left_half[leftIndex:])
    if rightIndex < len(right_half):
        result.extend(right_half[rightIndex:])
    return result
