#Heaps can be many sometimes tree or queue
#Heap is tree like structure in which root node is either most maximum or most mimimum
#To help the coder it is made to look like priority queue(abstraction)
#heaps always need not to be numbers they can can be lists
#[[0,"a"],[1,"b"],[2,"c"]] like this
#[[0,2],[0,1]] when min heap smallest number at index 0 will be popped if tied then second element is checked
#########Heap is not sorted at all
"""
Identification:
Min or max element,K
It requires sorting
#There is confusion with binary search(same minumum type problems)
#Both can be used Time of bs is nlogn(if sort needed) and Time of heap is nlogk
######Most important-Whenever we constantly need to sort array after inserting or deleting element and get some largest or smallest elements
      then this heap can be used becoz heap is always sorted even if you insert a new element or delete element

Patterns:
1)Top k pattern like find k max etc..
2)Merge problem 
3)Two heap problems
4)Minimum problem(BS and greedy)also    
"""
#smallest means max heap,largest means min heap
####We have top k freqent elements top=biggest=largest(We can use min heap)
"""
1)Min max element k
2)priority/event based problems
3)median
4)merging arrays(better than sort when sizes of array not equal)
"""
##ex: we want 3rd min element brute force is sort arr and find the 3rd index
#Plan comes we need only 3 elements why sort whole array waste of time and space so we use heap which will have constant size 3
#Find small - use max heap, Find big - use min heap
#Heaps have most odd behaviour sometimes it feels like when you heapify arr is sorted and sometimes not
"""
Lets say for example you are said to find max elemnt in heap after adding every elemnt
for example i am given sorted array=[1,2,3] max=m=3 now
after heapify and adding 4 now max must be 4 how to check
You can check if max(m,array[-1]) #cause in heap will be sorted you might think like that but wrong actullay it contains most rcently inserted elemnt 
but next time when popped it return min and then set itself in order
###3So m=max(m,arr[-1]) is right but m=arr[-1] wrong
Small tip:::::::::
Now you are doing first add you already know your max till now
Now adding you are adding only one element so why cant you do m=max(m,4(the elemnt you are adding)) instead of arr[-1]
Its more better right
Cause you only add one elemnt you already know max check if that is small or big
If you add 2 you max is 4
m=max(4,2(ele adding))--No change use it
"""
#Deletion in heap
"""
Use remove like array and then heapify(fix structure)
Time-O(n)+O(k) usually big complexity 
Instead there is method called lazy removal
i.e heap=[3,4,5]
if i want to remove 5 I will store it in hashmap mp={5:1}
I consider that element is removed already(assumption)
I casully perform ops
heap=[4,5] #heappop
heap=[4,8,5] #heappush(8)
heap=[5,8] #heappop()
Now when heappop i will check if heap[0] in lazy and then remove it my decrement count in map
##So i will remove the elements when that element is blocking my passage in heap
#hashmap used instead of set is becuse of dups i may wnat to remove 2 5s do mp{5:2} right when count==0 we must remove from map
"""
"""
Find Kth smallest elemnet in array
arr=[23,4,5,1,60,22] k=2
"""
#Pattern Top K pattern
from heapq import heapify,heappop,heappush
def ksmall(arr,k):
    ans=[]
    heapify(ans)
    for i in arr:
        #python doesnt have max heap so store elements as neg so when we pop we get smallest neg=biggest pos
        heappush(ans,-i)
        if len(ans)>k:
            heappop(ans)
    return heappop(ans)*-1

#We have problem called as skyline problem can be solved by both heap,line sweep need to get intution
"""
218. The Skyline Problem

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.
The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:
lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.
The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.
Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

Example 1:                     need to return outlines of buildings
15|    |11|
  |    |11|
  |    |1|33333|
10|   |00000|33|     |4444|
  |   |00000|33|     |4444|
  |   |00000|33|     |444|555555|  
5 |   |00000|33|     |444|555555|
  |   |00000|33|     |444|555555|
0 |   |00000|33|     |444|555555|
   _________________________________
   0     5    10    15    20     25 
15|    x  |
  |    |  |                           return x marks
  |    | |X    |
10|   X     |  |     X    |
  |   |     |  |     |    |
  |   |     |  |     |   |X     |  
5 |   |     |  |     |   |      |
  |   |     |  |     |   |      |
0 |   |     |  X     |   |      |
   _________________________________
   0     5    10    15    20     25 
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
Example 2:
Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]
 
Constraints:
1 <= buildings.length <= 104
0 <= lefti < righti <= 231 - 1
1 <= heighti <= 231 - 1
buildings is sorted by lefti in non-decreasing order.
"""
#brutely observe how we can solve this  
#answer contains x-axis(point) and height--so i need this
#Intitution is use max heap and keep track of height whenver height changes then that is one of answer
#Now how to check heights i mean at point it is added and another point removed so track it
#we can run loop from 0 to max(end buliding  point)-Might be TLE haven't tried
###another point i only need to check building start and end indices right so about sorted(set(start,end of all builidng))
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        sp={}#start points
        ep={}#end points
        ans=[]
        pq=[]
        points=set()
        for i in buildings:
            if i[0] not in sp:
                sp[i[0]]=[i[2]]
            else:
                sp[i[0]].append(i[2])
            if i[1] not in ep:
                ep[i[1]]=[i[2]]
            else:
                ep[i[1]].append(i[2])
            points.add(i[1])
            points.add(i[0])
        points=list(points)
        points.sort()
        lazy={}#lazy removal
        heappush(pq,0)#just for checking last point in answer
        #There are 3 cases 1)if start point 
        #                  2)if end point
        #                  3)If both start and end then priority is end first
        for i in points:
            if i in sp and i in ep:#case3
                while -pq[0] in lazy:
                    lazy[-pq[0]]-=1
                    if lazy[-pq[0]]==0:
                        del lazy[-pq[0]]
                    heappop(pq)
                for j in ep[i]:
                    if j in lazy:
                        lazy[j]+=1
                    else:
                        lazy[j]=1
                a=pq[0]
                while -pq[0] in lazy:
                    lazy[-pq[0]]-=1
                    if lazy[-pq[0]]==0:
                        del lazy[-pq[0]]
                    heappop(pq)
                for j in sp[i]:
                    heappush(pq,-j)
                if(a!=pq[0]):#check when removal also
                    ans.append([i,-pq[0]])
                
            elif i in sp:#case1
                a=pq[0]
                for j in sp[i]:
                     heappush(pq,-j)
                if(a!=pq[0]):
                    ans.append([i,-pq[0]])
            else:#case 2
                while -pq[0] in lazy:
                    lazy[-pq[0]]-=1
                    if lazy[-pq[0]]==0:
                        del lazy[-pq[0]]
                    heappop(pq)
                for j in ep[i]:
                    if j in lazy:
                        lazy[j]+=1
                    else:
                        lazy[j]=1
                a=-pq[0]
                while -pq[0] in lazy:
                    lazy[-pq[0]]-=1
                    if lazy[-pq[0]]==0:
                        del lazy[-pq[0]]
                    heappop(pq)
                if(a!=-pq[0]):#check when removal also
                    ans.append([i,-pq[0]])
        return ans
