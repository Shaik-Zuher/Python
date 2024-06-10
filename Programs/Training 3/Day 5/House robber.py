'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
'''
"""
case1:rob
nums[i]+recusrion(skipping next one)(n+2)
case2:skip
0+recuersion of next one(n+1)
"""
###Recursion
nums = [2,7,9,3,1]
n=len(nums)
def rob(i,n,nums):
    if i>=n:
        return 0 ###max is returned
    case1=nums[i]+rob(i+2,n,nums)
    case2=rob(i+1,n,nums)
    return max(case1,case2)
print("recursion:",rob(0,n,nums))
####memoization
####min cost step
cache=[-1]*(n+1)
def robb(index,n,nums):
    if index>=n:
        return 0
    case1=nums[index]+rob(index+2,n,nums)
    case2=rob(index+1,n,nums)
    cache[index]=max(case1,case2)
    return cache[index]
print("meno",robb(0,n,nums))
def table(n):
    dp=[-1]*(n+2)
    dp[n-1]=0
    for i in range(n-1,-1,-1):
        case1=nums[i]+cache[i+2]
        case2=cache[i+1]
        cache[i]=max(case1,case2)
    return cache[0]
print(table(n))