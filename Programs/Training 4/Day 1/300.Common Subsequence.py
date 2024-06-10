#Longest increasing subsequence length
#when length asked don't create any new strings or lists just use +1 for increasing lengths
nums=[10,9,2,5,3,7,101,18]
#need to track previuos and next elemnt
#if we want we can include or exclude so include-exclude mechansim
#       10 9 12 5 3 len=0
# p=-1  c     (initially)
#       p  c
def recurr(prev,nex):
    if prev==len(nums) or nex==len(nums):
        return 0
    include=0 #to prevtn block error
    if prev==-1 or nums[prev]<nums[nex]:
# 10 9 12 5 3 len=0
#  p    c     because of this function
#       p c   len=1
        include=1+recurr(nex,nex+1)
    exclude=recurr(prev,nex+1)
    return max(exclude,include)
#print(recurr(-1,0))
# index can range from 0 till n - 1 
# prevIndex can range from -1 till n - 1
n=len(nums)
cache = [[-1] * (n) for i in range(n + 1)]
#alwys take smaller one
 
def memoizationApproach(index, prevIndex):
    if index == n:
        return 0 
    elif cache[prevIndex + 1][index] != -1:
        return cache[prevIndex + 1][index]
 
    include = 0
    if prevIndex == -1 or nums[prevIndex] < nums[index]:
        include = 1 + memoizationApproach(index + 1, index) 
    exclude = memoizationApproach(index + 1, prevIndex)
    cache[prevIndex + 1][index] = max(include, exclude)
    return cache[prevIndex + 1][index]
 
def tabulationApproach():
    result = [1] * n 
    finalLis = 1
    for index in range(1, n): 
        for prevIndex in range(index):
            if nums[index] > nums[prevIndex]:
                result[index] = max(result[index], result[prevIndex] + 1)
        finalLis = max(finalLis, result[index])
    return finalLis
