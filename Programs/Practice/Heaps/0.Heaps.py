#Heaps can be many sometimes tree or queue.
#Heap is tree like structure in which root node is either most maximum or most mimimum.
#To help the coder it is made to look like priority queue(abstraction).
#heaps always need not to be numbers they can can be lists.
#[[0,"a"],[1,"b"],[2,"c"]] like this.
#[[0,2],[0,1]] when min heap smallest number at index 0 will be popped if tied then second element is checked.
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
