#rotated bs.
#[7,8,9,1,2,3,4,5,6]
#ie rotated at point to use bs on this 
#first lets check sorted part and check in that
#If left part is sorted check if target preesnt in left half or present in right half
#mid=(s+e)//2
#how to check which part sorted nums[start]<nums[mid] so left sorted basically ypu can say that(seriously)
#now how to check if present in sorted part nums[s]<target<nums[mid] so yes then e=mid-1 else s=mid+1
###effective if elements unique
#Lets say there are dups
#[2,8,9,1,2,3,4,5,2]
#l                r
#here nums[left]=nums[mid]=nums[right]
#so then why dont you just change pointers
#[2,8,9,1,2,3,4,5,2]
#   l           r
##################################################
#IN type of max min problems 
#always return low but not condition becoz low cntains(min) value but not condition 
#In find min type problems there might be confusion whether bs/heap/greedy bs-sorted heap-priority greedy-decisions. You can use anything
"""
Generally, we identify that binary search is applicable with 3 conditions :


Constraint of n <= 10 ^ 5
Question asks to find the minimum of maximums , maximum of minimums or some minimum/ maximum / at least
Montonic nature of the problem
"""
"""
conditions for bs:
1)searching
2)median without sorting
3)missing
4)min max elements
5)min elemrnts
6)peak
7)min max dist between gas stations---different casse based on decimal numbers
"""
"""
In question like make array of elements equal minimum moves we can use bs
in this we use  (lets say cost is outer func to caaculate cost)
s<=e:
left=cost(mid)
right=cost(mid+1)
if left<right: ############
e=mid-1
#########THIS is used in min cost operations type questions
"""
#Find duplicate element sorted
arr=[2,2,3,4,4]
"""
use normal bs check if mid!=mid-1 and mid!=mid+1 return mid
now our left/right elimination depends on mid position
example [1,1,2,2] observe pattern every first(duplicate) is in even position and every second(duplicate) in odd posititon
[1,1,2,3,3,4,4] mid=3(odd index),arr[mid]=3 so arr[mid-1] must also be 3 if not non_duplicate is on left else on right
[1,1,2,3,3,4,4,5,5] mid=4(even index),arr[mid]=3 so arr[mid+1] must also be 3 if not then non_duplicate is on left else on right
"""
arr=[1,2,2,3,3,4,4]
def duplicate(arr):
    if len(arr)==1:
        return arr[0]
    elif arr[0]!=arr[1]:
        return arr[0]
    elif arr[-2]!=arr[-1]:
        return arr[-1]
    s=0
    e=len(arr)-1
    while s<=e:
        mid=s+(e-s)//2
        if arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]:
            return arr[mid]
        elif mid%2==0:
            if arr[mid]==arr[mid+1]:
                s=mid+1
            else:
                e=mid-1
        else:
            if arr[mid]==arr[mid-1]:
                s=mid+1
            else:
                e=mid-1
    return -1

