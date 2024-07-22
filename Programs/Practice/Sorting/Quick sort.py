#Quick sort is done using pivot
#pivot can be any ele first/mid/last/random
#The mechanism is we take pivot and place it at correct position where it is sorted
#[4,6,1,2,5] ill say first ele is pivot     i want it to be like  1,2,4,5,6
# 0 1 2 3 4
#pivot=arr[low] so i  want to place it at pos 2
#take one pointer at front i and one from last j
#everytime check arr[i]>pivot because pivot will obviously change so i want small elements to be on left of pivot
# and larger ones on right so when ever i found larger elment i will swap it with small ele from backisde 
#so from backside check arr[i]<pivot swap them 
#after pivot comes in correct position split the arry like merge sort and perform on individul array with new pivots
"""dry run
pivot=arr[low]=4   4 6 1 2 5
              (low)i       j(high)
check  until arr[i]>pivot 
4 6 1 2 5
  i     j    yes now check until if arr[j]<pivot
4 6 1 2 5
  i   j    swap them 
4 2 1 6 5  continue prcess 4 6 1 2 5   4 6 1 2 5   4 6 1 2 5
  i   j                        i  j          j         j i
                                             i
stop once crossed now swap j and low 1 6 4 2 5 pivot is in correct position
return j the crrect position of pivot
"""
#now split [1,6]   and [2,5]   new pivots arr[low]=1 and 6 respectively
#partition(low,pivot-1)
#########partition(pivot+1,high) pivot alraedy placed so dont include
def qs(low,high,nums):#pointer gievn as parametrs to prevnt slicing
    if low<high: #dont want the crossed ones  and dont want to split len 1 arrays
        pivot_Index=partition(low,high,nums)
        qs(low,pivot_Index-1,nums)#left split
        qs(pivot_Index+1,high,nums)
    return nums
def partition(low,high,nums):
    pivot=nums[low]
    i=low
    j=high
    while i<j:#crossing thing
        while nums[i]<=pivot and i<high:#prevtn index out of range
            i+=1
        while nums[j]>=pivot and j>=low+1:##be carefull with 0 and lows #####################
            #######low+1 used becuse first element is pivot so to prevent that
            j-=1
        if i<j:#at last case i>j to prevtn swap there
            nums[i],nums[j]=nums[j],nums[i]
    #last pivot switch
    nums[low],nums[j]=nums[j],nums[low]
    return j #pivot position
nums=[3,2,4,5,5]
nums=qs(0,len(nums)-1,nums)
print(nums)