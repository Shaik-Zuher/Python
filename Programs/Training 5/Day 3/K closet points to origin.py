#when ever heap is used to find k max or min remove elemnts when len(heap)>k
#so k largest or smallest can be pushed forwrd
#when k largest minheap and when k smallest maxheap
'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
'''
#checking distance from origin to points we want maxheap  so pushing then with minus so when poped max elemnets are removed(when negative become small)
####################whenever len(q)>k pop elements so big elements than k can be remove dto reduce time complexity
from heapq import heapify,heappush,heappop
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distance=[]
        heapify(distance)
        for i,j in points:
            dist=sqrt((-i)**2+(-j)**2)
            heappush(distance,[-dist,[i,j]])
            if len(distance)>k:
                heappop(distance)
        l=[]
        i=0
        while i<k:
            i+=1
            curr=heappop(distance)
            l.append(curr[1])
        return l
