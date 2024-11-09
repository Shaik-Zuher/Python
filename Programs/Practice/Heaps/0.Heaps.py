#Heaps can be many sometimes tree or queue


#Heap is tree like structure in which root node is either most maximum or most mimimum
#To help the coder it is made to look like priority queue(abstraction)
#Heaps always need not to be numbers they can can be lists
#[[0,"a"],[1,"b"],[2,"c"]] like this ...
#[[0,2],[0,1]] when min heap smallest number at index 0 will be popped if tied then second element is checked
"""
Identification:
Min or max element,K
It requires sorting
#There is confusion with binary search(same minumum type problems)
#Both can be used Time of bs is nlogn(if sort needed) and Time of heap is nlogk
######Most important-Whenever we constantly need to sort array after inserting or deleting element and get some largest or smallest elements
      then this heap can be used becoz heap is always sorted even if you insert a new element or delete element
"""
#Smallest means max heap,largest means min heap
####We have top k freqent elements top=biggest=largest(We can use min heap)
"""
1)Min max element k
2)priority/event based problems
3)median
4)merging arrays(better than sort when sizes of array not equal)
"""
##Ex: we want 3rd min element brute force is sort arr and find the 3rd index
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
