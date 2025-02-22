#When ever we have something called as immediate next higher or next greatest we can definietly use mono stack or heap.

"""
2940. Find Building Where Alice and Bob Can Meet
You are given a 0-indexed array heights of positive integers, where heights[i] represents the height of the ith building.
If a person is in building i, they can move to any other building j if and only if i < j and heights[i] < heights[j].
You are also given another array queries where queries[i] = [ai, bi]. On the ith query, Alice is in building ai while Bob is in building bi.
Return an array ans where ans[i] is the index of the leftmost building where Alice and Bob can meet on the ith query. If Alice and Bob cannot move to a common building on query i, set ans[i] to -1.

Example 1:
Input: heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
Output: [2,5,-1,5,2]
Explanation: In the first query, Alice and Bob can move to building 2 since heights[0] < heights[2] and heights[1] < heights[2]. 
In the second query, Alice and Bob can move to building 5 since heights[0] < heights[5] and heights[3] < heights[5]. 
In the third query, Alice cannot meet Bob since Alice cannot move to any other building.
In the fourth query, Alice and Bob can move to building 5 since heights[3] < heights[5] and heights[4] < heights[5].
In the fifth query, Alice and Bob are already in the same building.  
For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.

Example 2:
Input: heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
Output: [7,6,-1,4,6]
Explanation: In the first query, Alice can directly move to Bob's building since heights[0] < heights[7].
In the second query, Alice and Bob can move to building 6 since heights[3] < heights[6] and heights[5] < heights[6].
In the third query, Alice cannot meet Bob since Bob cannot move to any other building.
In the fourth query, Alice and Bob can move to building 4 since heights[3] < heights[4] and heights[0] < heights[4].
In the fifth query, Alice can directly move to Bob's building since heights[1] < heights[6].
For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.

Constraints:
1 <= heights.length <= 5 * 104
1 <= heights[i] <= 109
1 <= queries.length <= 5 * 104
queries[i] = [ai, bi]
0 <= ai, bi <= heights.length - 1
"""
#Question says for query[i]=[alice,bob] index of them in heights we need to find largest buliding next where to f**k
#Undersatnd carfully you might think i<j then only move else -1###It actually confusing you might think i=ALICE j=BOB but no it says both can meet in necy tallest building
#Brute force is taking queries --find largest index in alice and bob and check largest bulding in(heights[alice],heights[bob]) and linear search after index to end to find largest break else -1
#example heights = [5,3,8,2,6,1,4,6] query=[0,3]
#                   i     j<-     -> check this side greater max(heights[alice],heights[bob])
#                            >5(bob height) It actually runnin O(n)/2-TLE
#############For that linear search we can use Segemnt Tree-WHiCH I havent learnt at this point(O(logn)/2)
#So about doing some revrse engineering as usual
#From heights i will check every value and ask for many queries this is answer
#Example 1 heights:[6,4,8,5,2,7] queries:[[0,1],[0,3],[2,4],[3,4],[2,2]]
#Index 0 height 6 how many queries is it anwser 0
#Index 1 height 4 how many queries=0
#Index 2 height 8 answer to 2 queries[[0,1][2,2]]
#index 3 height 5 no queires
#Index 4 No qereries
#Index 5 height 7 answer to 2 queries [[0,3],[3,4]]
"""
edge cases: if i==j alredy meet so answer j for query
           if i<j and heights[i]<heights[j] answer is j
                           No equal becuse if i,j have heights 1 we can have smething greater than on right
"""
#Coming back revrese engineering how to get answer i only want largest height 
#And will check if this maxheight is less than any height(traverse)
#########queries acn be check after max(i,j) right so until j(index during traverse) there is no answer at j we must add it-hashmap
##########suppose at j=2 there are bunch of queries (let max heights)[7,4,7] anc current(tervrse is 5) need to check if any smalls than 5 so we can use heap
from heapq import *
class Solution(object):
    def leftmostBuildingQueries(self, heights, queries):
        """
        :type heights: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans=[-1]*len(queries)#answer array
        mp={}
        #handing edge cases and hashmap
        for i in range(len(queries)):
            a,b=sorted(queries[i])#Basically if want largest index last
            if a==b:#equal case
                ans[i]=b 
            elif heights[a]<heights[b]:#height case
                ans[i]=b
            else:
                #add at which index(j) these queries must be checked
                if b in mp:
                    mp[b].append([max(heights[a],heights[b]),i])
                    #[max height,index(in answer)]
                else:
                    mp[b]=[[max(heights[a],heights[b]),i]]
        pq=[]
        print(mp)
        for i in range(len(heights)):
            #To how many queries current is answer
            while pq and pq[0][0]<heights[i]:
                #no equal becoz already handled in another loop
                a=heappop(pq)
                ans[a[1]]=i
            #adding query to heap
            #It is list so
            if i in mp:
                for j in mp[i]:
                    heappush(pq,j)
        return ans

#similar problem
"""
2454. Next Greater Element IV

You are given a 0-indexed array of non-negative integers nums. For each integer in nums, you must find its respective second greater integer.
The second greater integer of nums[i] is nums[j] such that:
j > i
nums[j] > nums[i]
There exists exactly one index k such that nums[k] > nums[i] and i < k < j.
If there is no such nums[j], the second greater integer is considered to be -1.
For example, in the array [1, 2, 4, 3], the second greater integer of 1 is 4, 2 is 3, and that of 3 and 4 is -1.
Return an integer array answer, where answer[i] is the second greater integer of nums[i].

Example 1:
Input: nums = [2,4,0,9,6]
Output: [9,6,6,-1,-1]
Explanation:
0th index: 4 is the first integer greater than 2, and 9 is the second integer greater than 2, to the right of 2.
1st index: 9 is the first, and 6 is the second integer greater than 4, to the right of 4.
2nd index: 9 is the first, and 6 is the second integer greater than 0, to the right of 0.
3rd index: There is no integer greater than 9 to its right, so the second greater integer is considered to be -1.
4th index: There is no integer greater than 6 to its right, so the second greater integer is considered to be -1.
Thus, we return [9,6,6,-1,-1].
Example 2:
Input: nums = [3,3]
Output: [-1,-1]
Explanation:
We return [-1,-1] since neither integer has any integer greater than it.
 
Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 109
"""
#You might wonder how to do this
#Think like this i want second greatest right 
#Find first greatest and at that place store the elements for which this element is greatest
# Second time we run another greatest(mono find) we can get second greatest
#same can be used for 3rd or 4th or so on...
# But don't use stacks at both iterations becmes mle instead use stack-first time  heap-second time so on.
"""
example:[2,4,0,9,6]
runing first general mono stack first greatest [4,9,9,-1,-1]
Right now i will store then in their first great position
[2,[2],0,[4,0],9,6] perform another mono stack but store the answer in original place by probabling use 2d list [ele,index]
#Actually no need to write whole array
take first store=[[],[],[],[],[]]
run reverse loop find first greater stack=[]
i=4 stack=[] stack updates fornext iteration
i=3 stack=[[6(ele),4(index)]] check if nums[i]>=stack[-1][0]:stack.pop so stack=[]
i=2 stack=[[9,3]] check condition still stack=[[9,3]] i.e that element is greatest so we have that elemnt index in that index(store) append current for which it is first greater
store=[[],[],[],[[0,2]],[]]
i=1 same as i=2 so store=[[],[],[],[[0,2][4,1]],[]]
i=0 stack=[[4,1][9,3]] so similar tore=[[],[[2,0]],[],[[0,2][4,1]],[]]

Second we can use another mono stack but when store[i] is not empty need to check if stack elemnt is greater and place it at that index
This gives mle so lets use heap--how
pq=[]
for i in range(len(nums)):
I will usually keep checking store[i] when there is present add all to pq(heap)
whenever i find larger element immdiate after that is second greatest
my main idea is:
I consider the elemnt doesnt exist until index of first greatest element at that point add.
"""
class Solution(object):
    def secondGreaterElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        store=[]
        for i in nums:
            store.append([])
        stack=[]
        #first greater check
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1][0]<=nums[i]:
                stack.pop()
            if stack:
                store[stack[-1][1]].append([nums[i],i])
                #store element at index of first greatest
            stack.append([nums[i],i])
        pq=[]
        ans=[-1]*len(nums)
        for i in range(len(nums)):
            while pq and pq[0][0]<nums[i]:#want greater so <
                ans[pq[0][1]]=nums[i]
                #store the elemnt at their respective indexes
                heappop(pq)
            #Add at that index until then no need
            if store[i]:
                for j in store[i]:
                    heappush(pq,j)
        return ans
#Same can be used for third greatest so on
"""
ele         2    4      9   9   6
first-great     [2,0]  [4,1]        first store
second-great           [2,0] [4,1]  another store
third-reat                  [2,0][4,1] we can keep going
"""
##########This will change
"""
pq=[]
newstore=[[] for _ in range(len(nums))]
for i in range(len(nums)):
    while pq and pq[0][0]<nums[i]:#want greater so <
        newstore[pq[0][1]].append(nums[i])
        ###################This is what might change 
        heappop(pq)
    #Add at that index until then no need
    if store[i]:
        for j in store[i]:
            heappush(pq,j)
return ans
"""
