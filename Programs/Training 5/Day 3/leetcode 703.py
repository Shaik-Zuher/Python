'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
 

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
'''
#when inserting elemnt if heap length<k pop smallest elemnt so that k largest elemnt is moved to top
#[2,4,5,8]-----[4,5,8] k=3
#insert 3 ---[3,4,5,8] ---[4,5,8] so heap[0] is our kth largest
class KthLargest(object):
 
    def __init__(self, k, nums):
        self.minHeap = []
        self.k = k
        heapify(self.minHeap)
 
        for ele in nums:
            heappush(self.minHeap, ele)
            if len(self.minHeap) > k:
                heappop(self.minHeap)
 
    def add(self, val):
        heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]
