#first we need to import library heapq
#python has inbuilt minheap function but no max heap
from heapq import heapify,heappush,heappop
#this is min heap
'''
heap=[19,10,1]
heapify(heap)
print(heap)
#inserting
heappush(heap,7)
heappush(heap,-121)
print(heap)
while heap:
    ele=heappop(heap)
    #min elemnts poped first 
    print(ele)
'''
maxheap=[]
heapify(maxheap)
l=[12,1,18,5]
for i in l:
    heappush(maxheap,-i)
print(maxheap)
#we are changing numbers in negative so when poped smallest elemnt is popeed but originally it is max heheheheh so we can again multiply it with minus to get back our positive value
while maxheap:
    ele=-heappop(maxheap)
    print(ele)
