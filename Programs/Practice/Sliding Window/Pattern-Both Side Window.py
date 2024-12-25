#A pattern where we want something from both sides
"""
1423.Maximum Points You Can Obtain from Cards
There are several cards arranged in a row, and each card has an associated number of points.
The points are given in the integer array cardPoints.
In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Example 1:
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1.
However, choosing the rightmost card first will maximize your total score.
The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
"""
#How to do this...
#we can take k cards from both sides right lets take k cards from front first and keep on removing front card and adding back card
# 2    3  1 2 2 1 2 3  k=2   =>  2  3 1 2 2 1 2  3  => 2 3 1 2 2  1  2
# add add                       add             add             add add  keep tracking maxsum
def cards(cds,k):
    lsum=0
    msum=0
    #add all front
    for i in range(k):
        lsum+=cds[i]
    msum=lsum 
    i=len(cds)-1
    #remove one front add one back
    for j in range(k-1,-1,-1):
        lsum-=cds[j]
        lsum+=cds[i]
        msum=max(msum,lsum)
        i-=1
    return msum

"""
1658. Minimum Operations to Reduce X to Zero
You are given an integer array nums and an integer x.
In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x.
Note that this modifies the array for future operations.
Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
Example 1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:
Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zer
"""
#Here we try to do same card thing but wont work how abt doing some revrse engineering
#In arr we want min subarry where sum== from both sides right
#[1,1,4,2,3], x = 5
#we can either 1+1(front)+3(back)=5 or 2+3(back)=5 remaining sum is sum(arr)-x=6 so how about finding length of remaining array
#As we want min  subarry we will find max remaining subarray and return len(arr)-(maxlen remain array)
#This only works because no negatives or else it will become  dp
class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        s=sum(nums)-x
        i=j=0
        m=-1
        sm=0
        while j<len(nums):
            sm+=nums[j]
            while i<=j and sm>s:  ###Fu**ing annoying
                #we have test case like [1,1] and k=2 here s=0 so max remainig sum=0 and we can  sm>s(1>0 always true) to prevent it we must keep i<=j
                sm-=nums[i]
                i+=1
            if sm==s:
                m=max(m,j-i+1)
            j+=1
        if m==-1:
            return -1
        return len(nums)-m
