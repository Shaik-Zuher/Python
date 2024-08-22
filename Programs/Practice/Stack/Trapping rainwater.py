"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


Example 1:
  3 |                            ___
    |                           |   |___
  2 |            ___            | 3    |    __
    |     ___   |   |__w_ w _w__|    2 |__w_| 2|__
  1 |    |   |w | 2     | w |           1       1 |
    |____|_1_|__|____1__|___|_____________________|
  0
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""
#find water quantuty we can say that water is only stored when there is previous great and next great
#Take 5 index(1) prev max=2 and next max=3 so water is stored quantity=min(prevmax,nxmax)-height[i]==>2-1=1 added to quantity
#so we need most greatest prev and nex 
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #prefix prev max
        #suffix next max
        def prefix():
            s=[0]
            for i in height:
                mx=max(s[-1],i)
                s.append(mx)
            return s
        def suffix():
            s=[0]
            for i in height[::-1]:
                mx=max(s[0],i)
                s.insert(0,mx)
            return s
        pre=prefix()
        suf=suffix()
        quantity=0
        for i in range(len(height)):
            if height[i]<pre[i] and height[i]<suf[i]:##used becouse if not used we can get -1 cases also
                quantity+=(min(pre[i],suf[i])-height[i])
        return quantity
#This uses O(2n) space not good so we can reduce it by using 2 pointers
"""
Approach: Take 2 pointers l(left pointer) and r(right pointer) pointing to 0th and (n-1)th index respectively. 
Take two variables leftMax and rightMax and initialize them to 0. 
If height[l] is less than or equal to height[r] then if leftMax is less than height[l] update leftMax to height[l] else add leftMax-height[l] to your final answer and move the l pointer to the right i.e l++. 
If height[r] is less than height[l], then now we are dealing with the right block. If height[r] is greater than rightMax, then update rightMax to height[r] else add rightMax-height[r] to the final answer. 
Now move r to the left. Repeat these steps till l and r crosses each other.

Intuition: We need a minimum of leftMax and rightMax.So if we take the case when height[l]<=height[r] we increase l++, so we can surely say that there is a block with a height more than height[l] to the right of l. And for the same reason when height[r]<=height[l] we can surely say that there is a block to the left of r which is at least of height[r]. So by traversing these cases and using two pointers approach the time complexity can be decreased without using extra space.
"""
# 0 1 0 2 1 0 1 3 2 1 2 1
# i                     j     -----leftmax,rightmax
#if i<=j
#   i                   j    left max for now is 0 
#     i                 j    left max for now is 1 as arr[i]>prevleftmax(0) before incrementing
#       i               j  now decremnt j
#       i             j      right max was initially 0 but now 1 as 1>prevrightmax(0)
height = [0,1,0,2,1,0,1,3,2,1,2,1]
n=len(height)
i=0
j=n-1
leftmax,rightmax=0,0
water=0
while i<=j:
    #pointers
    if height[i]<=height[j]:#checking less or greater
        if leftmax<=height[i]: #update left max
            leftmax=height[i]
        else:
            water+=leftmax-height[i] #adding quantity
        i+=1
    else:
        if rightmax<=height[j]:
            rightmax=height[j]
        else:
            water+=rightmax-height[j]
        j-=1
print(water)
