 #Insertion sort
''' lets say  a=12 11 13 5 6
                 0  1  2 3 4
insertion always checks in reverse so j will  be one less than i
when i=0 j=-1 --not good as array first index is 0
Iteration 1     This is where loop starts
              a=12 11 13 5 6
                 0  1  2 3 4
                 j  i
So initially i=1 
store value in i as a[i]=key
j=i-1=1-1=0
value a[j]=12
''
while j>=0 and a[j]>key :#j cant be less than 0(array first)
     a[j+1]=a[j] this is assigning not swapping  a=12 12 13 5 6
     j-=1 #decrement
a[j+1]=key #insertion step as 11 was removed from list so insert(name laugh) it in its position  now a= 11 12 13 5 6
we must check everthing so while placed in for loop i->1 to length
insertion must be outside while becuase  we must insert even if while condition not satisfied
Iteartion 2
So  i=1
              a=11 12 13 5 6
                 0  1  2 3 4
                 j  i 
store value in i as a[i]=key=12
j=i-1=1-1=0
value a[j]=11
while j>=0 and a[j]>key :#j cant be less than 0(array first) 11 not greater than 12 so loop not eneterd
a[j+1]=key #insertion step  a= 11 12 13 5 6
Iteartion 3
So  i=2 
              a=11 12 13 5 6
                 0  1  2 3 4
                 j     i
store value in i as a[i]=key=12
j=i-1=1-1=0
value a[j]=11
while j>=0 and a[j]>key :#j cant be less than 0(array first) 11 not greater than 12 so loop not eneterd
a[j+1]=key #insertion step  a= 11 12 13 5 6
So on Iterations
we must check everthing so while placed in for loop i->1 to length
insertion must be outside while becuase  we must insert even if while condition not satisfied
''
'''
def Insertion(list):
    for i in range(1,len(list)):
        insert=list[i]
        j=i-1
        while j>=0 and list[j]>insert:
            list[j+1]=list[j]
            j-=1
        list[j+1]=insert
    return list
print(Insertion([4,16,2,1]))
        
