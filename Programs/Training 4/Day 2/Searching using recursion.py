#linear search
l=[1,2,3,4,5]
res="Not Found"
'''
def recur(key,i,n,res):
    if i==n:
        return 
    if key==l[i]:
        res=i
        return res
    recur(key,i+1,n,res)
    #won't work because recursion value is not stored like seriously
    #its more like dp instead of recursion
    return res
print(recur(4,0,len(l),res))
def work(key,i,n,res):
    if i==n:
        return 
    if key==l[i]:
        return i
    res=work(key,i+1,n,res)
    return res
print(work(4,0,len(l),res))
'''
#binary search
start=0
end=len(l)
mid=start+((end-start)//2)
def bin(key,s,mid,e):
    #where is mid being updated
    if e<=s:
        return
    if key<l[mid]:
        e=mid-1
        return e
    if key>l[mid]:
        s=mid+1
        return s
    if key==l[mid]:
        return mid
    res=bin(key,s,mid,e)
    return res
print(bin(1,start,mid,end))
def bin1(key,s,e):
    #return is powerful need tobe carefull
    if e<=s:
        return
    mid=s+((e-s)//2)
    if key<l[mid]:
        e=mid-1
    if key>l[mid]:
        s=mid+1
    if key==l[mid]:
        return mid
    res=bin1(key,s,e)
    return res
print(bin1(1,start,end))
    
