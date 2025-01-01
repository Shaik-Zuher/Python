"""
Given k sorted arrays arranged in the form of a matrix of size k * k. The task is to merge them into one sorted array. Return the merged sorted array ( as a pointer to the merged sorted arrays in cpp, as an ArrayList in java, and list in python).
Examples :
Input: k = 3, arr[][] = {{1,2,3},{4,5,6},{7,8,9}}.
Output: 1 2 3 4 5 6 7 8 9.
Explanation: Above test case has 3 sorted arrays of size 3, 3, 3 arr[][] = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]. The merged list will be [1, 2, 3, 4, 5, 6, 7, 8, 9].
"""
######Similarly we have merge linked lists--Merge is used there.
#Merging all lists.
#There a lot of ways.
#Basic-concate all lists into one list and sort(O(NlogN))
#Some what better is merge sort(O(NlogN))---good all lists are same size
#Another heaps+(somewhat graph dfs)(O(NlogK))--good if lists are different sizes
"""
#We can use brute force merge sort.
#Run a loop on arr and a=arr[1],b=arr[2] merge and store them in arr[1] again a=arr[1],b=arr[3]
#But still it might be around O(n^2)
"""
class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        # code here
        # return merged list
#Tip of mergesort: use only one merge like general merge sort [1,2,3] use it on [[1],[2],[3]] the lists to be treated as single element
        if len(arr)>1:
            mid=len(arr)//2
            left=arr[:mid]
            right=arr[mid:]
            self.mergeKArrays(left)
            self.mergeKArrays(right)
            return self.merge(left,right)
    def merge(self,l,r):
        temp=[]
        i,j=0,0
        while i<len(l) and j<len(r):
            if l[i]<=l[r]:
                temp.append(l[i])
                i+=1
            else:
                temp.append(r[j])
                j+=1
        while i<len(l):
            temp.append(l[i])
            i+=1
        while j<len(r):
            temp.append(r[j])
            j+=1
        return temp
#Heap version
from heapq import heapify,heappop,heappush
class Solution:
    #Function to merge k sorted arrays.
    #Example:{{1,2,3},{4,5,6},{7,8,9}}
    def mergeKArrays(self, arr, K):
#Its not neccesary to solev this using heaps but there are many problems on this same concept heap+bfs(type)
        ans=[]
        heapify(ans)#generally  heap
        #brute force takes somewhat aroun O(N^2)-I hate it instead of it lets use one loop ans store only small in every list
        for i in range(K):#K is len of arr
            heappush(ans,[arr[i][0],i,0])#its already sorted
            #            min ele,index in array,subindex in inner array----This is acting like dfs
        #Heap=[[1,1,0],[4,2,0],[7,3,0]]
        res=[]
        while ans:
            ele,index,subindex=heappop(ans)
            res.append(ele)
            #ele,index,subindex=1,1,0
            #increase subindex +1 and add next element is heap
            if(subindex+1)<len(ele[index]): #Check if next element exists
                heappush(ans,[arr[index][subindex],index,subindex])
            #heap now [[2,1,1],[4,2,0],[7,3,0]]
            #         in 1st index it is element at index 1
        return res
