"""
2940. Find Building Where Alice and Bob Can Meet.
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
