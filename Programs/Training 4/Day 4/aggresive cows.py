'''
You are given an array consisting of n integers which denote the position of a stall. You are also given an integer k which denotes the number of aggressive cows. You are given the task of assigning stalls to k cows such that the minimum distance between any two of them is the maximum possible.
The first line of input contains two space-separated integers n and k.
The second line contains n space-separated integers denoting the position of the stalls.

Example 1:

Input:
n=5 
k=3
stalls = [1 2 4 8 9]
Output:
3
Explanation:
The first cow can be placed at stalls[0], 
the second cow can be placed at stalls[2] and 
the third cow can be placed at stalls[3]. 
The minimum distance between cows, in this case, is 3, 
which also is the largest among all possible ways.
'''
#Lets start thinking about cases
# _  _  _  _  _
#| min|
#|     max     |
#but there can be chances that in between the cows ther might be min distance(index1....n-1)
#So we need to check the distances

class Solution:
    def solve(self,n,k,stalls):
        #this checks distances
        stalls.sort()
        maxPossible = stalls[n - 1] - stalls[0]
        minPossible = stalls[1] - stalls[0]
        for index in range(2, n):
            minPossible = min(minPossible, stalls[index] - stalls[index - 1])
#upto here
#We need to check if cows can be placed with the  current min distance
#[1 2 4 8 9]
#lets say there are there are  3 cows with min distance 3
# 1st(index0)  2nd(index 2(dist=2-1<3)so that cant be placed  2nd(index3(true)) 3rd(index4) all placed successfully
#s for min=3 we have true
#if min=6
# 1st(index0)  2nd(index 2(dist=2-1<6)so that cant be placed  2nd(index4(true)) 3rdcant be placed 
# for min=6 we have false
#fro all mins  0  1  2  3  4  5  6
#              T  T  T  T  F  F  F
#we need to minimum cost with max so we use mid(binary serach)and check if true occurances at left or right and go to lst occurance
        def isPossible(val):
            cowsToBePlaced = k - 1
            #placed at index 0
            previousCow = 0 
 
            for index in range(1, n):
                diff = stalls[index] - stalls[previousCow] 
                if diff >= val:
                    previousCow = index
                    cowsToBePlaced -= 1
                    if cowsToBePlaced == 0:
                        return True 
            return False
 
        result = -1 
        left, right = minPossible, maxPossible 
        while left <= right:
            mid = (left + right) // 2 
            if isPossible(mid):
                result = mid 
                left = mid + 1 
            else:
                right = mid - 1
        return result
