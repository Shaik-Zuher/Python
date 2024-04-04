#Merge Sort
'''
after merging take for example  2arrays left,right
left=47 56    right =1 4
      i              j
compare i and j
smaller is added to array :1 and then inedx incremented
left=47 56    right=  4
      i               j
continues untill all added to array
'''
arr=[56,47,29,1,4,32]
'''
def  divide(a):
    print("dividing")
    if len(a)>1:
        mid=len(a)//2
        left=a[:mid]
        right=a[mid:]
        print(left,right)
        divide(left)
        divide(right)
        print("merging")
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                a[k]=left[i]
                i+=1
            else:
                a[k]=right[j]
                j+=1
            k+=1
            #if elemnts left in left right
        while i<len(left):
            a[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            a[k]=right[j]
            j+=1
            k+=1
    return a
print(divide(arr))
'''
#Quick Sort
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range (low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quick(arr,low,high):
    if low<high:
        pvot=part(arr,low,high)
        quick(arr,low,pivot-1)
        quick(arr,pivot+1,high)
    
        
