#Book Allocation
#aggressive Cows
######################################################Book allocation#########################################
'''
Book has M pages in array for example say [10,20,30,40] and N number of students.Pages are allocated such that:-
1)Every Student has atleast one book
2)Every book must be allocated in consecutive order
Find maximum pages alloacted whic are minimum
##Note--When ever we have something like Maximum and minimum binary search is used
__Usecase:
case1:s1 has 10 and s2 has 20,30,40(sum=90)
case2:s1 has 10,20(sum=30) and s2 has 30,40(sum=70)
case3:s1 has 10,20,30(sum=60)and s2 has 40
maximum pages allocated are 90,70,60 the minimum is 60
'''
def Ispossible(s,page,mid):
    sum=0
    ns=1
    for i in range(0,len(page)):
        if(sum+page[i]<=mid):
            sum+=page[i]
        else:
            ns+=1
            if(ns>s or page[i]>mid):
                return False
            sum=page[i]
    return True
def bin(s,page):
    ps=0
    for i in page:
        ps+=i
    start=0
    end=ps
    mid=start+(end-start)//2
    while start<=end:
        if Ispossible(s,page,mid):
            ans=mid
            end=mid-1
        else:
            start=mid+1
        mid=start+(end-start)//2
    return ans
print(bin(2,[10,20,30,40]))
