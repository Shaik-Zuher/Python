"""
def performBubbleSort(nums, n):
    if n == 1:
        return 
 
    # last index is (n - 1)
    for index in range(n - 1):
        if nums[index] > nums[index + 1]:
            nums[index], nums[index + 1] = nums[index + 1], nums[index]
 
    performBubbleSort(nums, n - 1)    
 
 
def performSelectionSort(nums, n):
    if n == 1:
        return 
 
    # fix (n-1)th index 
    maxEleIndex = n - 1 
    for index in range(n - 1):
        if nums[index] > nums[maxEleIndex]:
            maxEleIndex = index 
 
    if maxEleIndex != n - 1:
        nums[maxEleIndex], nums[n - 1] = nums[n - 1], nums[maxEleIndex]
 
    performSelectionSort(nums, n - 1)
 
 
 
def performInsertionSort(nums, n):
    if n == 1:
        return 
 
 
    performInsertionSort(nums, n - 1)
    # nums = [1, 3, 4, 5, 6, 7, 8, 2]
    # nums = [1, 3, 3, 4, 5, 6, 7, 8]
    currValue = nums[n - 1]   
    prevIndex = n - 2
    while prevIndex >= 0:
        if nums[prevIndex] > currValue:
            nums[prevIndex + 1] = nums[prevIndex]
        else:
            break 
        prevIndex -= 1 
    nums[prevIndex + 1] = currValue
 
 
def performCountingSort(nums, n):
    pass
 
nums = [8, 1, 7, 6, 5, 4, 3, 2]
 
print("Before sorting:", nums)
performInsertionSort(nums, len(nums))
print("After sorting:", nums)
"""
nums=[8,1,7,3,0]
def bubble(nums,n):
    if n==1:
        return
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            nums[i],nums[i+1]=nums[i+1],nums[i]
    bubble(nums,n-1)
#bubble(nums,len(nums))
#we can take either temp min number  and compare with everything or take tempmax
def selection(nums,n):
    if n==0:
        return
    maxele=n-1
    for i in range(n-1):
        if nums[maxele]<nums[i]:
            maxele=i
    if maxele!=n-1:
        nums[maxele],nums[n-1]=nums[n-1],nums[maxele]
    selection(nums,n-1)
selection(nums,len(nums))
print(nums)

