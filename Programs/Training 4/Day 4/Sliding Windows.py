def findAllIndices(nums, k, target):
    n = len(nums)
    currTotal = sum(nums[:k])
    result = []
    if currTotal == target:
        result.append(0)
 
    left, right = 0, k 
    while right < n:
        currTotal -= nums[left]
        currTotal += nums[right]
        if currTotal == target:
            result.append(left + 1)
        left += 1 
        right += 1 
    return result
 
nums = [10, 2, 3, 43, 2, 10, 35, 3]
k = 3 
target = 48
result = findAllIndices(nums, k, target)
print(result)
##[10, 2, 3, 43, 2, 10, 35, 3]
#first take the k sized elements i.e [10,2]
#if sum of first==target then add fisrt elemnt index to result array
#next loop from k and lets take pointer i=0
#sum=sum-nums[i]  10,2=sum(12) in this nums[0] removed 12-10=2
#sum=sum+nums[k]   2+3=5 this will be repated whenever sum meets our required index added
#####Maximum sliding window
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        result = []
        store = []
        
        #[300, 20, 80, 90, 150]
        # k = 4
        # [0, 1, 2, ]
        #####use python visuliazer
        for i in range(k):
            # step-2 (eliminate all smaller elements indices)
            while store and nums[store[-1]] <= nums[i]:
                store.pop()
    
            # step-3 (insert current index)
            store.append(i)
        
        result.append(nums[store[0]])
        
        
        left, right = 0, k
        while right < n:
            # step-1 (eliminate unwanted indices)
            if store and store[0] == left:
                store.pop(0)

            # step-2 (eliminate all smaller elements indices)
            while store and nums[store[-1]] <= nums[right]:
                store.pop()

            # step-3 (insert current index)
            store.append(right)
            result.append(nums[store[0]])
            left += 1 
            right += 1 
            
        return result


