#Heaps can be many sometimes tree or queue
#Heap is tree like structure in which root node is either most maximum or most mimimum
#To help the coder it is made to look like priority queue(abstraction)
"""
Identification:
Min or max element,K
It requires sorting
#There is confusion with binary search(same minumum type problems)
#Both can be used Time of bs is nlogn(if sort needed) and Time of heap is nlogk
"""
##ex: we want 3rd min element brute force is sort arr and find the 3rd index
#Plan comes we need only 3 elements why sort whole array waste of time and space so we use heap which will have constant size 3
#Find small - use max heap, Find big - use min heap
"""
Find Kth smallest elemnet in array
arr=[23,4,5,1,60,22] k=2
"""
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
