#Sliding window lenght is taken as j-i+1 and stacks j-(i+1) in stacks we want exclusive we want to find length between i and unlike sliding window where we want both i,j
#Sliding window affected by negative numbers crap!!!!
#String takes more time than list/array
#sliding always need not to have some array called as window.It can also be achived with pointers(i.e type of 2 pointers)
################sliding window anf hashmap are freqently used but when ever hp[i]==0 make sure delete it  and last longst length condition must always have <= because we need longest someytimes it might be even small
################!!!!!!!!! Dont forget ----when hp and cnt used make sure thatcnt is increase hp[s[r]]>-1##########
#window can be fixed size or any size.This is just a mechanism of shrink and extend
#need to find shrink expand condition
########Important: Sliding window questions will always some condition or 2 inputs.Otherwise it wont be sliding window(rare cases)
######## It will have size of window ,some condition,subarray,substring,subsequence
"""
patterns
1)fixed window size
2)longest common substring with condition
3)no of subarrays with condition
4)minimum subarray with condition
"""
#pattern 4 is not the same as min max sliding window(this is stack)
"""
Identify:
1)some fixed size
2)Contagious 
3)subarray,subsequence
4)consecutive
5)Contains window in question
Note:You will be always given 2 inputs then only sliding window
###Remember window min max of stack problem.If no 2 inputs.Max it wont be sliding window except rare cases
"""
######################Queue
######Implementation of sliding window requires queue
#pop(0) takes more complexity than popleft() so try to avoid it
"""
fixed window size example
1)find subarray of length k which has sum equal to some number
"""
from collections import deque
sum=3
k=3
arr=[1,4,2,2,-1,1]
s=0
window=deque([])
for i in range(k):
    window.append(arr[i])
    s+=arr[i] 
if s==sum:
    print(window)
for i in range(k,len(arr)):
    a=window.popleft()
    window.append(arr[i])
    s-=a
    s+=arr[i]
    if s==sum:
        print(window)
"""
2)contingous,continous,subarray,subsequenec with some condition
This requires 2 points where 1 will act as start of window and other as end of window
Here we won't have fixed window size
EXAMPLE
1)find max length of subarray which has sum less than or equal to some value
  a)Brute force---generating all subarrays
  b)better      -----if give subarray asked
  c)best------only useful for ones where something like max/min length is asked not usefull for give the subarray
"""
###########Most of time it needs hashmap but when ever hp[i]==0 make sure delete it  and last longst length condition must always have <= because we need longest someytimes it might be even small
ss=4
#better
#take 2 pointers l,r 
# r        end of window(incrementing)     it involves two things expand,shrink
# l        start of window                                         r      l
# 1 4 2 2 -1 1
l,r=0,0
length=0
s=0
while r<len(arr):
    s+=arr[r]
    while l<=r and s>ss:
        #l<=r not necessary but can be used for safety
        s-=arr[l]
        l+=1
    length=max(length,(r-l+1))#dont forget array is 0 based
    r+=1
print(length)
#You might think it is o(n^2) but l doesn,t run for whole length right so it is o(n)+o(n)
"""
best approach
"""
####We got extra n becuse of while loop 
#we can observe we want only max so when i want largest why I need to shrink my window somethimg less why don't I remove while
#lets say i have  1 2 3 1 4 1and sum=6
#                 i   j
#                 i     j     sum>6  my max length is 4 so i will only remove first element becuse why i want to chcek something with length small
#                   i     j     still >6 so one removed mut my max window length is maintained....
l,r=0,0
length=0
s=0
while r<len(arr):
    s+=arr[r]
    if s>ss:    # this is only change
        s-=arr[l]
        l+=1
    if s<=ss: #if condition this must be present for foresight protection of cases
#############Another point------whenever there is while inside while main condition if not needed at all
        length=max(length,(r-l+1))#dont forget array is 0 based
    r+=1
print(length)
"""template
while r<len(arr):
    s+=arr[r]
    if s>ss:    # condition   this is what changes depending on requirement
        s-=arr[l]
        l+=1    #shrink
    if s<=ss: #if condition this must be present for foresight protection of cases
        length=max(length,(r-l+1))#dont forget array is 0 based
    r+=1        #expand
"""
#This better approch must be used when subarray is asked to be printed
"""
3)count of subarrays with condition
ex:count the number of subarrays with sum=0
"""
####Logic here
#count(condtion)=count(<=condition)-count(<=condition-1)
#arr=[1,0,0,1] find number of subarrays where sum=0
arr=[1,0,0,1]
goal=0
def count(arr,goal):
    i=0
    j=0
    c=0
    s=0
    while j<len(arr):
        s+=arr[j]
        while i<=j and s>goal: #if must not be used
            #i<=j no need necesarrily but can be used for safety so whenever testcases fail try this
            s-=arr[i]
            i+=1
        if arr[j]<=goal:######When while there please never use if Process when while there first try 1)If passes good 2) Else remove if
            c+=(j-i+1)  #like this becuse [1] 1 elemnt added  [1,2] has [1][2][1,2] alredy [1] is added we need to [2][2,3]==length.....
        j+=1
    return c 
#############Another point------whenever there is while inside while main condition if not needed at all
print(count(arr,goal)-count(arr,goal-1))
"""
4.Minmum window problems
same as 2nd pattern but somewhat different
"""
#In some problems you are asked to return substing of another string in other fashion whne we have use of 2 hps 
#and chceking condition like mp==hp instead of mainatining 2 maps decrement the values in single map
#Example: hp={a:1 b:2} and s[j]=b then make hp[s[j]]-=1 and cnt+=1 which is lot better becuause otherwise need to check lot of edge cases
#example t="ABC" and s="CCAB" and tell use return substring t in s if we check 2 maps and hp==mp
#mp={A:1,B:1,C:1} and s={C:2,B:1,A:1} we wont get answer because we can have exact or more occurances of elemnts in t
#we need to increment cnt based on hp[s[i]]<=mp[s[i]] otherwise it will be disaster
