"""
295. Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:
MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 
Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 
Constraints:
-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 
Follow up:
If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""
#brute force is add element every time sort after every time find median----Sort everytime so we can use heap
#But how to find median because it is not sorted array so we cant use index because in heap only 0 index has smallest
#Consider heap=[1,2,3,4] how to find median how about use 2 heaps  One heap has small part and one big part
#Step1: 2 heaps [1,2] [3,4] so i will big element from small heap and small from large heap
#So small heap=Max heap(ele are negative) big heap=Min heap
#Step2: In which element does heap go hmmmm  I will consider elements by default will so in max heap(small one)
#Elements are split properly  that means lengths must be equal
"""#Even case=[1] [2] odd case=[1,2] [3] so one heap can have equal or extra"""
#Dry run:
#add 1  maxheap=[-1] and minheap=[] one heap can have one elment so ok
'''case1'''
#add 2  maxheap=[-1,-2] and minheap=[] i dont want this so remove largest from max heap and add to min
#       maxheap=[-1] and minheap=[2]
'''case2'''
#add 3 maxheap=[-3,-1] and minheap=[2] check add element is greater or smaller than smallest one in minheap need to maintain order
#So i will pop and add to minheap maxheap=[-1] and minheap=[2,3]
#add 4 maxheap=[-4,-1] and minheap=[2,3]   ---> maxheap=[-1] and minheap=[2,3,4] here second length is greater so also check this case and add small one from second heap(large) into first heap(small)
##step 3 find median if lengths equal max(maxheap)+min(minheap)/2.0 and if odd then min from odd length heap
"""
Follow up: for 1,100 we can run brute force and store them in array of size 100 or hashmap and and find middle among counts pretty easy right
Another point:This won't work for large data sets(we need to use thread safe mechansim) or BST(segement Tree type)
"""
from heapq import *
class MedianFinder(object):

    def __init__(self):
        self.minheap=[]
        self.maxheap=[]

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        #Add cases
        #Default one
        heappush(self.maxheap,-num)
        if len(self.maxheap)>len(self.minheap)+1:#Uneven length Case 2
            heappush(self.minheap,-heappop(self.maxheap))
        #case 3 check if added is really small or large
        if self.maxheap and self.minheap:#necessary
            if -self.maxheap[0]>self.minheap[0]:
                heappush(self.minheap,-heappop(self.maxheap))
            if len(self.maxheap)+1<len(self.minheap):#Once again length check
                heappush(self.maxheap,-heappop(self.minheap))
        return
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minheap)==len(self.maxheap):
            return (self.minheap[0]+(-self.maxheap[0]))/2.0
        elif len(self.minheap)>len(self.maxheap):
            return self.minheap[0]
        else:
            return -self.maxheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
