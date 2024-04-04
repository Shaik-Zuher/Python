#complexities
# lets say ekemnet to find is in first position then number of iterations would be 1 so O(1)-best case
#lets say element to find is in last position the numbers of iterations would be n so O(n)-worst case
'''
list=[0,12,13,14,15,16]
k=int(input("Enter a number:"))
for i in range(0,len(list)):
    if(list[i]==k):
        print("Element found at",i)
        break
'''
list=[0,12,13,14]
k=int(input("Enter the number:"))
i=0
for j in range(0,len(list)):
    if(list[j]==k):
        i=j
        break
if(i!=0):
    print("Element found at",i)
else:
    print("Element Not Found")

