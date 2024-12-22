"""
Given an array and sum k find longest subarray having sum equal to k.
"""
#On first thought seems easy but nooooooo.
#If it has only positives then we can use normal sliding window
#If has negatives use hashmap(it is somewhat like 2 sum leetcode problem)
arr=[-1,1,-1,1,1,1,1]
k=3
def sub(arr,k):
    hp={}#hashmap
    s=0#prefix sum
    ml=0
    for r in range(len(arr)):
        s+=arr[r]
        if s==k:
            ml=r+1
        if s-k in hp:
            ml=max(ml,r-hp[s-k])
        if s-k not in hp:
            hp[s-k]=r 
    return ml 
#In hashamp we store prefix sums as our req sum is k we do some revrse maths saying s-k if it is present we take index and distance betwwen index and r is maxlen
#Basically prefix=[i,j,k]   sum of subarray=[j,k] is sum=prefix[k]-prefix[j-1](prefix[j]+prefix[k] So len is from j not j-1)
#prefix[k] in prefix track and prefix[j] is past one so saved in hashmap so prefix[j]=prefix[k]-sum so prefix[j] to find in hashmap
"""
r=0 and arr[r]=-1 s=-1   s-k=-1-3=-4 not there
hp{ 
-1:0(index)  s=-1 r=0
0: 1         s=0 r=1
            s=-1 when r=2 already there so skip as well as s-k still not there
            s=0 when r=3 already there so skip as well as s-k still not there
1:4    s=1 r=4
2:5   but s-k=2-3=-1 presnt so if check from index 0 to 4 -1+1-1+1+1+1=3(0 must be excluded becoz at zero sum is -1 we want to remove that much)  ml=(r-0)=5
                        so unlike j-i+1 we do only j-1######imporatnt
3:6   ml=7(sum==3)
} like this
"""
