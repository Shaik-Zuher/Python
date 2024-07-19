"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
"""
"""
1  4  7  11  15
2  5  8  12  19
3  6  9  16  22
10 13 14 17  24
18 21 23 26  30
"""
"""
We can enhance this method by adjusting how we move through the matrix. Let's take a look at the four corners: (0, 0), (0, m-1), (n-1, 0), and (n-1, m-1).
Observations:
Cell (0, 0): Assume we are starting traversal from (0, 0) and we are searching for 14.
Now, this row and column are both sorted in increasing order. So, we cannot determine, how to move i.e. row-wise or column-wise.
That is why, we cannot start traversal from (0, 0).

Cell (0, m-1): Assume we are starting traversal from (0, m-1) and we are searching for 14.
Now, in this case, the row is in decreasing order and the column is in increasing order.
Therefore, if we start traversal from (0, m-1), in the following way, we can easily determine how we should move.
If matrix[0][m-1] > target: We should move row-wise.
If matrix[0][m-1] < target: We need bigger elements and so we should move column-wise.

Cell (n-1, m-1): Assume we are starting traversal from (n-1, m-1) and we are searching for 14.
Now, this row and column are both sorted in decreasing order. So, we cannot determine, how to move i.e. row-wise or column-wise.
That is why, we cannot start traversal from (n-1, m-1).

Cell (n-1, 0): Assume we are starting traversal from (n-1, 0) and we are searching for 14.
Now, in this case, the row is in increasing order and the column is in decreasing order.
Therefore, if we start traversal from (n-1, 0), in the following way,  we can easily determine how we should move.
If matrix[n-1][0] < target: We should move row-wise.
If matrix[n-1][0] > target: We need smaller elements and so we should move column-wise.

From the above observations, it is quite clear that we should start the matrix traversal from either the cell (0, m-1) or (n-1, 0).

Note: Here in this approach, we have chosen the cell (0, m-1) to start with. You can choose otherwise.

Using the above observations, we will start traversal from the cell (0, m-1) and every time we will compare the target with the element at the current cell.
After comparing we will either eliminate the row or the column accordingly like the following:
If current element > target: We need the smaller elements to reach the target. But the column is in increasing order and so it contains only greater elements. So, we will eliminate the column by decreasing the current column value by 1(i.e. col--) and thus we will move row-wise.
If current element < target: In this case, We need the bigger elements to reach the target. But the row is in decreasing order and so it contains only smaller elements. So, we will eliminate the row by increasing the current row value by 1(i.e. row++) and thus we will move column-wise.
"""
#we can either start from 0,m-1 check row and col depending on conditions and decrement respective row or col literally brain moment
# a b c
# d e f     we can either start from c or g lets take c if target <c that means elemnt presnt in row.So decrement row.When row decremented its row and col checked.
# g h i
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
def array(matrix,target):
    m=len(matrix)
    n=len(matrix[0])
    # i will take case of m-1,0 bottom left
    row=m-1
    col=0
    while row>-1 and col<n:
        if matrix[row][col]==target:
            return True
        elif target<matrix[row][col]:
            row-=1
        else:
            col+=1
    return False
print(array(matrix,target))
