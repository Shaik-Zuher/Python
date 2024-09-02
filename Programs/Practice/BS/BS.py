#Rotated bs 
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
"""
By using binary search we can even find pair of elements withs sum equal to target
ex: 1 2 3 4 target=3
    i     j   1+4=5>3 so we need to decrese big element(i.e)j
    i   j
    i j      match  else <target increase small element (i.e)i
This can be used for a lot of searchings
Can also be used for 3 sum where one loop wholey and j=i+1 and k is last element in array
Similarly for any sums(4 sum or 5 sum)
"""
