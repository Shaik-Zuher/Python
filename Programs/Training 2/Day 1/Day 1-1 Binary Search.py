#Here mid=start+end//2 not recmended lets say if end number is 2^32(integer range)
#so mid will be more than range to solve this proble use (s+((e-s)//2))
#(s+((e-s)//2))=(2s+(e-s))//2
'''list=[12,13,14,15]
t=int(input("Enter The Number:"))
start=0
end=len(list)-1#if not length will be given
mid=(start+end)//2
while start<=end:
    if list[mid]==t:
        print(mid)
        break
    elif t<list[mid]:
        end=mid-1
    elif t>list[mid]:
        start=mid+1
    mid=(start+end)//2   
'''
#time complexity list=n/2 -iteration 1
#list=(n/2)/2=n/2^2 -iteration 2
#list=(n/2^2)/2=n/2^3 -iteration 3
#list=n/2^k -iteration k
#n/2^k=1
#n=2^k
#log n=K log2
#k=log n
list=[12,13,14,15]
t=int(input("Enter The Number:"))
start=0
end=len(list)-1#if not length will be given
mid=(start+((end-start)//2))
while start<=end:
    if list[mid]==t:
        print(mid)
        break
    elif t<list[mid]:
        end=mid-1
    elif t>list[mid]:
        start=mid+1
    mid=(start+((end-start)//2))
