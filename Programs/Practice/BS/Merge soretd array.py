"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
 

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
#one of naive is merging using merge sort and find mid but time complexity is alot
#without mergings lets think about imaginary array(merged)
#1,3                           mid
#2,4,5,6         Imaginary 1,2,3|4,5,6 this is what be get when merged
#                  In left part one ele is from list1 and one ele in from list2 this is what we need to take as mid(no of elements taken)
#I need 3 elemnts in left side and 3 elements in right side
############This half is taken as n1+n2/2 words good for even  4+4/2=4   so now for odd 4+5/2=4(but mid must be 5) so add 1 for evn case evn if you add 1 4+4+1/2=4
#For example let say i will take zero elements form one elements from small array and all from second
#       |1,3      how to check lets think last elemnt in array1 before mid as l1  and after mid as r1
#2,4,5  |6                                            inarray2  before mid as l2  and after mid as r2 
#2,4,5|1,3,6 no not sorted         l1<r2  and l2<r1  then you can say yeah it is sorted   ------------just cross check thats all
####now take 1 elemnt from first arry
#    1 | 3
# 2,4  | 5,6   now l1 not greter than r2 so skip
####now take 2 elemnt from first array
#   1,3| 
#    2 | 4,5,6  this is true yup
#####Now lets take this point from arr1 if 2 elemnts taken then ((n1+n2)/2)-mid which is 1 elemnt taken from arr2 this can be called as mid2
#mid1 is first array       mid2 is second arry
#to reduce time complxity  take first mid as small array always
############now median calculated can we say max(l1,l2)+min(r1,r2)/2 yeah thats good
nums1=[1,3]
nums2=[2]
def merger(a,b):
    n1=len(a)
    n2=len(b)
    if n1>n2:
       a,b=b[:],a[:]
       n1=len(a)
       n2=len(b)
    half=(n1+n2+1)//2
    s=0
    e=n1
    while s<=e:
        mid1=s+(e-s)//2
        mid2=half-mid1
        l1,l2,r1,r2=float("-inf"),float("-inf"),float("inf"),float("inf")
        if mid1<n1:####TO prevent out of bounds errors
            r1=a[mid1]
        if mid2<n2:
            r2=b[mid2]
        if mid1-1>=0:
            l1=a[mid1-1]
        if mid2-1>=0:
            l2=b[mid2-1]
        if l1<=r2 and l2<=r1:
            if (n1+n2)%2==1:#even length case
                return max(l1,l2)
            else:
                return (max(l1,l2)+min(r1,r2))/2.0
        else:
            if l1>r2:
                e=mid1-1
            else:
                s=mid1+1
    return 0
print(merger(nums1,nums2))
