"""
Given k sorted arrays arranged in the form of a matrix of size k * k. The task is to merge them into one sorted array. Return the merged sorted array ( as a pointer to the merged sorted arrays in cpp, as an ArrayList in java, and list in python).
Examples :
Input: k = 3, arr[][] = {{1,2,3},{4,5,6},{7,8,9}}
Output: 1 2 3 4 5 6 7 8 9
Explanation: Above test case has 3 sorted arrays of size 3, 3, 3 arr[][] = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]. The merged list will be [1, 2, 3, 4, 5, 6, 7, 8, 9].
"""
######Similarly we have merge linked lists--merge is used there
#merging all lists
#There a lot of ways 
#basic-concate all lists into one list and sort(O(NlogN))
#Some what better is merge sort(O(NlogN))---good all lists are same size
#Another heaps+(somewhat graph dfs)(O(NlogK))--good if lists are different sizes
"""
#We can use brute force merge sort
#Run a loop on arr and a=arr[1],b=arr[2] merge and store them in arr[1] again a=arr[1],b=arr[3]
#But still it might be around O(n^2)
"""
#Pattern 2:Merge
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
#its not neccesary to solev this using heaps but there are many problems on this same concept heap+bfs(type)
        ans=[]
        heapify(ans)#generally  heap
        #brute force takes somewhat aroun O(N^2)-I hate it instead of it lets use one loop ans store only small in every list
        for i in range(K):#K is len of arr
            heappush(ans,[arr[i][0],i,0])#its already sorted
            #            min ele,index in array,subindex in inner array----This is acting like dfs
        #heap=[[1,1,0],[4,2,0],[7,3,0]]
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
    """
    Here i have problem i usually use dfs type list but i also think popped one also needs to be stored in new heap
    but no need the popped can be in answer list
    """
    #variation of pattern get top 10 small elements in list of sorted elements
    #Above one was sort so all need to checked
    #But here only 10 need to be checked remaining go to hell
    def check(mat,k):
        pq=[]
        res=[]
        for i in range(len(mat)):
            heappush(pq,[mat[i][0],i,0])
            # element,row index,col index
        while len(res)<k and pq:####################This is main logic
        ##We dont need to check every element becuse rows are already sorted so we dont need to take heap and
        ##store pops in it with while len>k the popped can be added to result because it will be answer
            a=heappop(pq)
            res.append(a[0])
            a[2]+=1
            if a[2]<len(mat[0]):
                heappush(pq,[mat[a[1]][a[2]],a[1],a[2]])
        return res
    mat=[[1,2,3],[3,4,5]]
    k=4

################################Another important similar pattern--find pair numbers with min sum
"""
373. Find K Pairs with Smallest Sums

You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
 
Constraints:
1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in non-decreasing order.
1 <= k <= 104
k <= nums1.length * nums2.length
"""
#k pairs in question tells heap must be used.
#a=[1,7,11] b=[2,4,6] smallest sum will be first in both arrays 1+2=3
#Insert into heap pq=[[7(sum),0(index),0(index)]]
#In above merge problems we take small from pq and increment that particular popped so one removed and one added
#Here one removed two will be added
# a=[1,7,11]   a=[1,7,11]
#      |          |
# b=[2,4,6]    b=[2,4,6]first value is 1+2 next one will be next will be either (7(index1)+2(index0)) or(1(index0),4(index1)) this is pattern
#    |              |
# so intial pq=[[7,0,0]] then next pq=[[5,0,1],[8,1,0]] first array index+1 and second arr index+1
"""One problem is duplicates"""
#Let go in order of inserting pq=[[3,0,0]]=>[[5,0,1][8,1,0]]=>[[8,1,0][13,0,2],[11,1,1]]=>[[13,0,2]   [11,1,1][11,1,1]    ,[13,2,0]]
''''''#                                                                                    see we actually got duplicates
#To prevent this duplicates use set when adding element to pq to check if index already checked
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        pq=[]
        ans=[]
        heappush(pq,[nums1[0]+nums2[0],0,0]) #intial add
        while len(ans)<k and pq:#Don't forget what i thought you
            a=heappop(pq)
            ans.append((nums1[a[1]],nums2[a[2]]))
            #Don't add index before if condition
            if a[1]+1<len(nums1):
                #a[1]+=1     bad move because if you add now other index add(if condition) will be effected
                new=a[1]+1
                heappush(pq,[nums1[new]+nums2[a[2]],new,a[2]])
            if a[2]+1<len(nums2):
                new=a[2]+1
                heappush(pq,[nums1[a[1]]+nums2[new],a[1],new])
        return ans
#Similar one is sum of max combinations 
