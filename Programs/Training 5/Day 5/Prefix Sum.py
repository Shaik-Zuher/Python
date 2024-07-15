l=[10,8,12,5,25,11]
res=0
prefix=[]
for i in l:
    res+=i
    prefix.append(res)
print(prefix)
#prefix sum is sum of all elemnets in array upto that index
#you can also do this as sum[i]=n[i]+sum[i-1] which pretty much wraps it up in O(1) space complexity
#ranges find prefix sum between particular indices i.e between index 2 and index 6 we can find as think about removing all before elemnts
# i.e prefix[6]-prefix[1](we want from index 2 so remove everything upto before)
"""
nums = [10, 2, 32, 15, 21, 5, -2]
n = len(nums)
prefix = [0] * n 
for index in range(n):
    prefix[index] = nums[index]
    if index > 0:
        prefix[index] += prefix[index - 1]
 
queries = [[0, 6], [1, 6], [4, 5], [2, 6]]
for query in queries:
    left, right = query[0], query[1]
    result = prefix[right]
    if left > 0:
        result -= prefix[left - 1]
    print(result)
"""
queries = [[0, 5], [1, 5], [3, 4], [2, 5]]
   #        indices
for j in queries:
    last=j[1]
    first=j[0]
    if first== 0:# index out of bounds becomes -1
        print(prefix[last])
    else:  
        print(prefix[last]-prefix[first-1])
