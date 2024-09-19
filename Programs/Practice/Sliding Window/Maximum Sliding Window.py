"""
Given an array arr[] of size N and an integer K. Find the maximum for each and every contiguous subarray of size K.
Example 1:
Input:
N = 9, K = 3
arr[] = 1 2 3 1 4 5 2 3 6
Output: 
3 3 4 5 5 5 6 
"""
##This is just like monotic stack(stock span problem)
#Our idea is we store a element whenver we get max elemnt we remove elemnents less than it from arr becoz we want only max element we don't need small ones so lets remove it
#store=[] i=j=0
#store=[1] arr[j]=0(window is 1)
#store=[2] i=0 arr[j]=1(window 1 2) we removed one because 2>1 why i need small one I need bigs 
#store=[3] i=0 arr[j]=2(window 1 2 3) we removed 2 
#store[3,1] i=0 j=3 arr[j]=1(window 2 3 1) it is not greater so for now it wont be max but can be in future so store it and j==k store first element from store which wil definitely be max
#store=[3,4] i=1(window increased) j=4 and arr[j]=4(window 3 1 4) but we need to check if store[0] is out of our window and max of current window still 3
#store=[3,5] i=2(window increased) j=5 and arr[j]=5(window is 1 4 5) but we need to check if store[0] is out of our window and max of current window still 3
#here 3 out of window so remove it this is how we take these elemnts
###How to check if out of bounds is if arr[i]=store[0] then remove store[0]
### We can either store their indexes and check if i>store[0](this has indexes)
class Solution:
    #Function to find maximum of each subarray of size k.
    #elemnt store
    def max_of_subarrays(self,arr,n,k):
        i=j=0
        ans=[]
        store=[]
        while j<n:
            while store and store[-1]<=arr[j]:
                store.pop()#remove smalls
            store.append(arr[j])#store the current ele
            if i>0 and arr[i-1]==store[0]:#checking out of bounds
                store.pop(0)
            if(j-i+1)>=k:
                ans.append(store[0])
                i+=1
            j+=1
from collections import deque
#We can even use queue
class Solution:
    #Function to find maximum of each subarray of size k.
    #Index stores
    def max_of_subarrays(self,arr,n,k):
        i=j=0
        ans=[]
        store=deque([])
        while j<n:
            while store and arr[store[-1]]<=arr[j]:
                store.pop()#remove smalls
            store.append(j)#store the current ele index
            if store and i>store[0]:#checking out of bounds
                store.popleft
            if(j-i+1)>=k:
                ans.append(arr[store[0]])
                i+=1
            j+=1
        return ans
    
