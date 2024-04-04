'''Bubble Sort-swap the largest element to last
Syntax
i->0 to n:
   j->0 to n-i-1:
   if(a[j]>a[j+1]):
      swap
'''
#best case O(n)
#worst case O(n^2)
'''
l=[23,45,1,8,4,3]
temp=0
for i in range(0,len(l)):
    for j in range(0,len(l)-i-1):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print(l)
'''
'''Selection sort-swap the smallest element by travelling whole list found index of min list and swapped with first one'''
l=[23,45,1,8,4,3]
temp=0
min=0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[min]>l[j]:
            min=j
            temp=l[i]
            l[i]=l[min]
            l[min]=temp
        min=i
print(l)
