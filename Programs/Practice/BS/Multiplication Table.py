"""
Kth Smallest Number in Multiplication Table
Given three integers M, N and K. Consider a grid of M * N, where mat[i][j] = i * j (1 based index).
The task is to return the Kth smallest element in the M * N multiplication table.
Example 1:
Input:
M = 3, N = 3
K = 5
Output: 3
Explanation: 
   1  2  3
1  1  2  3 
2  2  4  6
3  3  6  9
1 2 2 3 3 4 6 6 9
The 5th smallest element is 3. 

Example 2:
Input:
M = 2, N = 3
K = 6
Output: 6 
"""
#Similar to find median in 2D array
#We nee to find number of smaller elements
class Multiply():
    def matrix(m,n,k):
        def enough(l):
            c=0
            for i in range(1,m+1):
                #For number of elements if we generate tables TLE
                #usually every row is in form i,2*i,3*i...n*i
                #Consider last element is smallest n*i==l so n=l//i
                #if first row 5//1=5 but our first row doesnt have 5 so min(n(col),l//i)
                #for second 5//2=2(2,4 only less than 5) so normally added
                c+=min(n,l//i)
            return c
        s=1
        e=m*n#possible mac
        while s<=e:
            mid=s+(e-s)//2
            if enough(mid)<k:
            #number of elemnts less than mid <=k(smallest we need)
                s=mid+1
            else:
                e=mid-1
        return s
