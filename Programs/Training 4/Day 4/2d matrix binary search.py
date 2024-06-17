matrix =[[10, 20, 30, 40], 
            [50, 60, 70, 80], 
            [90, 100, 110, 120]]
 
target=100
#dont use 2 for loops
#My own approach
def search(matrix,target):
    for i in range(len(matrix)):
        start=0
        end=len(matrix[i])-1
        while start<=end:
            mid=start+(end-start)//2
            if matrix[i][mid]==target:
                return True
            elif matrix[i][mid]>target:
                end=mid-1
            else:
                start=mid+1
    return False
print(search(matrix,target))
#But this is O(n^2) approach
#lets try this in O(log(n+m))
#lets imaginary think there is only single list not matrix =[10,20,30,40,50,60,70,80,90,100,110,120]
#start is 0 and end is a[11] where length is 12 which can be obtained by rwo*col=3*4=12
#or mid will be 0+11/2=5 i.e a[5]=60 in matrix it is a[1][1] lets see how we can obtain them using n and m and mid
#if mid//n=5//4=1###################################
#lly mid%n=5%4=1################################
#so these can be row and col just figure out which is which
def sera(matrix,target):
    m=len(matrix)
    n=len(matrix[0])
    start=0
    end=(n*m)-1
    while start<=end:
        mid=start+(end-start)//2
        row=mid//n####
        col=mid%n#####
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]<target:
            start=mid+1
        else:
            end=mid-1
    return  False
print(sera(matrix,target))
