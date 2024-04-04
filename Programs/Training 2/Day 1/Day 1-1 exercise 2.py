#without sorting find peak element binary search  
array=[1,3,6,7,9,5,2]
s=0
e=len(array)-1
k=0
mid=s+(e-s)//2
while s<=e:
    if (array[mid]>array[mid-1] and array[mid]>array[mid+1]):
        k=mid
        break
    elif (array[mid]<array[mid-1]):
        e=mid
    elif (array[mid]<array[mid+1]):
        s=mid
    mid=s+(e-s)//2
print("position of peak element is",k)
print("Peak Element is",array[mid])
