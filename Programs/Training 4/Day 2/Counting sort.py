
def performCountingSort(nums):
    n = len(nums)
    temp = [-1] * n
    # step-1: finding max 
    mx = max(nums)
 
    # step-2: creating (max + 1) length list with zeroes 
    store = [0] * (mx + 1)
 
    # step-3: finding each element frequency 
    for ele in nums:
        store[ele] += 1 
    print(store)
 
    # step-4: calculating prefix sum 
    for index in range(1, mx + 1):
        store[index] += store[index - 1]
    print(store)
 
 
    # step-5: traverse from right to left and place the element at appropriate index 
    for index in range(n - 1, -1, -1):
        ele = nums[index]
        store[ele] -= 1 
        temp[store[ele]] = ele
        print(temp)
 
 
    # step-6: (optional) copy the temp output list to main list
    for index in range(n):
        nums[index] = temp[index]
 
 
 
 
 
 
nums = [8, 1, 7, 6, 5, 4, 3, 2, 1, 1, 2, 2, 4, 4, 4, 4, 6]
 
print("Before sorting:", nums)
performCountingSort(nums)
print("After sorting:", nums)
 
