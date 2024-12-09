####Queue is used in circular,simulations,dfs,sliding window
#pop(0) has more complexity so use popleft instead.
#insert takes more time complexity so try to use append/assignment
#Identification when we have loop i,j and j in dependent on i(range from i to n like this) we can use stacks
#Sliding window lenght is taken as j-i+1 and stacks j-(i+1) in stacks we want exclusive we want to find length between i and unlike sliding window where we want both i,j

#Motonic stack is tack where elements are ascending or descending order
#Next greater,Next smaller,prev greater etc 
#####We have 3 types of next element tracker
"""1.First next larger element"""
stack=[12,44,1,7,3,9]
#if no ele either 0 or -1
#ans=[44,-1,7,9,9,-1]
s=[-1]#default array as it always starts with -1
ans=[0]*len(stack)
for i in range(len(stack)-1,-1,-1):
    while s[-1]!=-1 and stack[i]>=s[-1]:###this is main logic our stack always has greater eles when current ele is greater elements in stack removed until -1
        s.pop()
    ans[i]=s[-1]
    s.append(stack[i])
print(ans)
###One of variation said that the array is cyclic then just append stack to same stack and follow same technique
"""2.Immediate next greater element"""
stack=[12,44,1,7,3,9]
#if no ele either 0 or -1
#ans=[44,-1,7,-1,9,-1]
s=[-1]#default array as it always starts with -1
ans=[0]*len(stack)
for i in range(len(stack)-1,-1,-1):
    while s[-1]!=-1 and stack[i]>=s[-1]:###this is main logic our stack always has greater eles when current ele is greater elements in stack removed until -1
        s=[-1]##allremoved because immediate checked
    ans[i]=s[-1]
    s.append(stack[i])
print(ans)
"""3.Most graetest element"""
stack=[12,44,1,7,3,9]
#ans=[44,9,9,9,9,0]
##for these types generally use prefix max or suffix max
ans=[0]
for i in range(len(stack)-1,-1):
    mx=max(ans[0],stack[i])
    ans.insert(0,mx)
print(ans)
#####This used in traping rain water and rectangle
##################sum of subarry min or sum of subarray max like this reqires stack(nge,pge,pse,nse)
#Here we check contribution how many times used stack stores indices and eles
#not t be confused with binary search becuase these are contagious
"""
907. Sum of Subarray Minimums
Given an array of integers arr,find the sum of min(b),where b ranges over every (contiguous) subarray of arr.
Since the answer may be large, return the answer modulo 109 + 7.
Example 1:
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:
Input: arr = [11,81,94,43,3]
Output: 444
"""
#track the contributions
#                               3 1 2 4
#contributions of 3             1[3]
#                               0[1,3]adding next elements no matter what you do you have only 1 contribution
#contribution of 1                1[1] on right side
#                                 1[1,2]
#                                 1[1,2,4]
#                 on leftside[3,1]1
#                          [3,1,2]1
#                        [3,1,2,4]1  we have 6 contributions
#contribution of 2                   1[2]    on right side
#                                    1[2,4]
#                    on leftside     none(-1)
#contributin of 4                      1[4] right side
#                    on leftside     none(-1)
######Here main logic is that a ele is considered is min until it encounter another min so we can check next small and prev small
# indices                       0 1 2 3
# let that ele 2                3 1 2 4
#next smaller                       none(len(arr) becuse we cant keep -1 it means its the smallest)
#prev smaller                       1(index=1)
#                        cal= next index-curr index * curr index-previndex
#                        cal*arr[i]
####################This is most important point got it
class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mod=10**9+7
        def nse():
            s=[]
            stack=[[-1,len(arr)]]
            for i in range(len(arr)-1,-1,-1):
                while len(stack)!=1 and stack[-1][0]>arr[i]:
                    stack.pop()
                s.insert(0,stack[-1])
                stack.append([arr[i],i])
            return s

        def pse():
            s=[]
            stack=[[-1,-1]]
            for i in range(len(arr)):
                while len(stack)!=1 and stack[-1][0]>=arr[i]:####here = uaed to avoid edgecase [1,1]
                    stack.pop()
                s.append(stack[-1])
                stack.append([arr[i],i])
            return s
        ns=nse()
        ps=pse()
        #print(ns)
        #print(ps)
        s=0
        for i in range(len(arr)):
            m=(ns[i][1]-i)*(i-ps[i][1])
            s+=(m*arr[i])%mod
        return s%mod
#there is variation called minsubarray ranges tehn we need to find min(pse,pge) and max(nge,pge) and max-min
            
