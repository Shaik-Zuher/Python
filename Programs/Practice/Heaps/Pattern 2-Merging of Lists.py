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
'''getting somw what hard'''
"""
1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows

You are given an m x n matrix mat that has its rows sorted in non-decreasing order and an integer k.
You are allowed to choose exactly one element from each row to form an array.
Return the kth smallest array sum among all possible arrays.

Example 1:
Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 7
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.
Example 2:
Input: mat = [[1,3,11],[2,4,6]], k = 9
Output: 17
Example 3:
Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
Output: 9
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.  
 
Constraints:
m == mat.length
n == mat.length[i]
1 <= m, n <= 40
1 <= mat[i][j] <= 5000
1 <= k <= min(200, nm)
mat[i] is a non-decreasing array.
"""
#If said get kth smallest we can either use binary search or heap(merge pattern)
#This is min sum thing in matrix
#I will use min sum of 2 arrays as sub problem
#We have 0 1 2 rows i will use that problem on 0 1 and store in 1 and then use it on 1 2 and store 2 return mat[-1].pop()(last row)
class Solution(object):
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        def merger(a,b):
            ans=[]
            pq=[]
            heappush(pq,[a[0]+b[0],0,0])
            s=set()
            while len(ans)<k and pq: #len(ans)<k but not len(a) or len(mat[0]) becuse we can even have k=10 but n=3 thats why
                p=heappop(pq)
                ans.append(p[0])
                if p[1]+1<len(a):
                    new=p[1]+1
                    if (new,p[2]) not in s:
                        heappush(pq,[a[new]+b[p[2]],new,p[2]])
                        s.add((new,p[2]))
                if p[2]+1<len(b):
                    new=p[2]+1
                    if (p[1],new) not in s:
                        heappush(pq,[a[p[1]]+b[new],p[1],new])
                        s.add((p[1],new))
            return ans
        temp=mat[:]
        for i in range(1,len(mat)):
            temp[i]=merger(temp[i-1],temp[i])
        return temp[-1].pop()

#This is hard problem
"""
2386. Find the K-Sum of an Array

You are given an integer array nums and a positive integer k. You can choose any subsequence of the array and sum all of its elements together.
We define the K-Sum of the array as the kth largest subsequence sum that can be obtained (not necessarily distinct).
Return the K-Sum of the array.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
Note that the empty subsequence is considered to have a sum of 0.

Example 1:
Input: nums = [2,4,-2], k = 5
Output: 2
Explanation: All the possible subsequence sums that we can obtain are the following sorted in decreasing order:
- 6, 4, 4, 2, 2, 0, 0, -2.
The 5-Sum of the array is 2.
Example 2:

Input: nums = [1,-2,3,4,-10,12], k = 16
Output: 10
Explanation: The 16-Sum of the array is 10

n == nums.length
1 <= n <= 105
-109 <= nums[i] <= 109
1 <= k <= min(2000, 2n)
"""
#You might not get pattern but k sum means we have to use merge one but how we need to fix array to use merge one
#Lets be greedy max possible sum is sum of all elelments but array has neg so sum of all positives
#Next what might be next max i.e max-small(array) as array has neg make whole array absolute 
#Cause i am gonna use maxheap=[-(sums-array[0])] even if the positive is added the elemnt is maxheap will end being postive due to larger and eventually removed
######Subsequence means 2 cases 1)remove current elemnet(exclude) 2)include this and exclude next one(include)
#######case 1: sum-array[i]   case2:sum+array[i]-array[i-1]
from heapq import *
class Solution(object):
    def kSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s=0
        for i in range(len(nums)):
            if nums[i]>0:
                s+=nums[i]
            nums[i]=abs(nums[i])
        nums.sort()
        pq=[]
        heappush(pq,[-(s-nums[0]),0])
        ans=[s]#current sum is biggest possible
        while len(ans)<k:
            a=heappop(pq)
            ans.append(-a[0])
            a[1]+=1
            if a[1]<len(nums):
                heappush(pq,[-(-a[0]-nums[a[1]]),a[1]])
                heappush(pq,[-(-a[0]+(nums[a[1]-1])-nums[a[1]]),a[1]])
        return ans[-1]
