"""1004. Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""
#Like general instead of 1s let count zeroes
##brute force
def binary(arr,k):
    #genertaing all sub arrays
    mlen=0
    for i in range(len(arr)):
        zeroes=0
        for j in range(i,len(arr)):
            #count zeroes
            if arr[j]==0:
                zeroes+=1
            if zeroes<=k:
                mlen=max(mlen,j-i+1)
            if zeroes>k:
                break
#better
def binary(arr,k):
    mlen,i,j,zeroes=0,0,0,0
    while j<len(arr):
        if arr[j]==0:
            zeroes+=1
        while zeroes>k:
            if arr[i]==0:
                zeroes-=1
            i+=1
        if zeroes<=k:
            mlen=max(mlen,j-i+1)
        j+=1
#best
def binary(arr,k):
    mlen,i,j,zeroes=0,0,0,0
    while j<len(arr):
        if arr[j]==0:
            zeroes+=1
        if zeroes>k:  #just change if
            if arr[i]==0:
                zeroes-=1
            i+=1
        if zeroes<=k:
            mlen=max(mlen,j-i+1)
        j+=1
