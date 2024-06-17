"""
def mergeThoseTwoArrays(nums, left, mid, right):
    # left subarray --> [left, mid]
    # right subarray --> [mid + 1, right]
    temp = []
    index1 = left 
    index2 = mid + 1 
 
    while index1 <= mid and index2 <= right:
        if nums[index1] > nums[index2]:
            temp.append(nums[index2])
            index2 += 1 
        else:
            temp.append(nums[index1])
            index1 += 1 
 
    while index1 <= mid:
        temp.append(nums[index1])
        index1 += 1 
 
    while index2 <= right:
        temp.append(nums[index2])
        index2 += 1 
 
 
    position = 0 
    for index in range(left, right + 1):
        nums[index] = temp[position]
        position += 1 
 
 
 
 
 
 
def divideAndMerge(nums, left, right):
    if left >= right:
        return 
 
    mid = (left + right) // 2 
    # left subarray --> [left, mid]
    # right subarray --> [mid + 1, right]
 
    divideAndMerge(nums, left, mid)
    divideAndMerge(nums, mid + 1, right)
    mergeThoseTwoArrays(nums, left, mid, right)
 
 
 
 
 
def performMergeSort(nums):
    n = len(nums)
    divideAndMerge(nums, 0, n - 1)
 
 
 
 
nums = [8, 1, 7, 6, 5, 4, 3, 2, 10, 20, -1, -5]
 
print("Before sorting:", nums)
performMergeSort(nums)
print("After sorting:", nums)
"""
#pivot
def getPivotIndex(nums, left, right):
    pivot = nums[right]
    # [18, 12, 22, 23, 10, 7, 20]
     # [18, 12, 10, 23, 22, 7, 20]
     # [18, 12, 10, 7, 22, 23, 20]
 
 
 
    # [18, 12, 10, 7, 22, 23, 20]
    # [18, 12, 10, 7, 20, 23, 22]
    position = left
    for index in range(left, right):
        if nums[index] < pivot:
            nums[index], nums[position] = nums[position], nums[index]
            position += 1 
 
    nums[right], nums[position] = nums[position], nums[right]
    return position
 
 
 
def findPivotAndSort(nums, left, right):
    if left >= right:
        return 
    pivotIndex = getPivotIndex(nums, left, right)
    findPivotAndSort(nums, left, pivotIndex - 1)
    findPivotAndSort(nums, pivotIndex + 1, right)
 
def performQuickSort(nums):
    n = len(nums)
    findPivotAndSort(nums, 0, n - 1)
 
 
 
 
nums = [8, 1, 7, 6, 5, 4, 3, 2, -1, -2, -3, -100, 100]
 
print("Before sorting:", nums)
performQuickSort(nums)
print("After sorting:", nums)
 
