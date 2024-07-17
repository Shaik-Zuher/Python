"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Return the kth positive integer that is missing from this array.

 
Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
"""
arr = [1,2,3,4]
#originally array must have been [1,2,3,4,5]
#now lets say [5,6,7,8] which k=4 element is 4 obvisouly because before 5 we have 4 missing elements
# 1 2 3 4  5 indexs bcoz numbers startfrom 1
#[2,3,4,7,11]  for 2 we have 1 missing elemnt for 3 we have missing elemnt.....for 7 we have 3 missing (trick:7(ele)-4(original ele(index+1)))
# 1 1 1 4 6  missings
k = 6
#brute force
def fn(arr, k):
    cnt=k
    for i in range(len(arr)):
         if(k>(arr[i]-(i+1))):
            cnt+=1
         else:
             break
    return cnt
print(fn(arr,k))
##Using BS
#################keep track of misssing numbers
# 1 2 3 4  5 indexs bcoz numbers startfrom 1
#[2,3,4,7,11]  for 2 we have 1 missing elemnt for 3 we have missing elemnt.....for 7 we have 3 missing (trick:7(ele)-4(original ele(index+1)))
# 1 1 1 4 6  missings
#       ^ ^
#       | | must be present here
def findKthPositive(arr, k):
    
    if(k<arr[0]):
            return k
    s=0
    e=len(arr)-1
    while(s<=e):
        mid=s+(e-s)//2
        if k>arr[mid]-(mid+1):
            s=mid+1
        else:
            e=mid-1
    return k+s####s contains missing elemnets
