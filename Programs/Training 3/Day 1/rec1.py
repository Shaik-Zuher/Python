#create list  and find sum,min,max
l=[15,10,-5,81]
#Using for or while loop
"""
sum=0
for i in l:
    sum+=i
print(sum)
min,max=99,0
for i in l:
    if i<min:
        min=i
print(min)
for i in l:
    if i>max:
        max=i
print(max)
"""
#Using recursion
""" Sum"""
#parent to child -parent just changing something but not taking anything from child as result  but dp is reverse
#      (index,array,sum)
def so(i,n,sum):
    if i==len(n):
        print(sum)
        return
    sum+=n[i]
    so(i+1,n,sum)
so(0,l,0)
#passing data from child function to parent function(dp)
def sum2(index,n,nums):
    if index==n:
        return 0
    nextElementSum=sum2(index+1,n,nums) #This is dp #child functions data
    return nextElementSum+nums[index]    #passed to parent functin
print(sum2(0,len(l),l))

"""Max"""
def max1(index,maxi,l):
    if index>=len(l):
        print("Max p to c:",maxi)
        return
    if maxi<l[index]:
         maxi=l[index]
    max1(index+1,maxi,l)
max1(0,0,l)
#####Practice#####
def max2(index,l):
    if index==len(l)-1:
        return l[index]
    child_give_data=max2(index+1,l)
    if child_give_data<l[index]:
        return l[index]
    return child_give_data
print("Max using dp",max2(0,l))
"""Min"""
def min(index,mini,l):
    if index>=len(l):
        print("Min p to c:",mini)
        return
    if mini>l[index]:
         mini=l[index]
    min(index+1,mini,l)
min(0,99,l)
