#May sound like sliding window but no I'm a stack
#mmmmmmm   sounds like shit ya but this is bullshit stack becouse of so called min max of every window size and funnily every window size==subaray
#Yes you got it right it like find sum of mins of subarrays 
"""
Maximum of minimum for every window size

Given an integer array. The task is to find the maximum of the minimum of every window size in the array.
Note: Window size varies from 1 to the size of the Array.

Example 1:

Input:
N = 7
arr[] = {10,20,30,50,10,70,30}
Output: 70 30 20 10 10 10 10 
Explanation: 
1.First element in output
indicates maximum of minimums of all
windows of size 1.
2.Minimums of windows of size 1 are {10},
 {20}, {30}, {50},{10}, {70} and {30}. 
 Maximum of these minimums is 70. 
3. Second element in output indicates
maximum of minimums of all windows of
size 2. 
4. Minimums of windows of size 2
are {10}, {20}, {30}, {10}, {10}, and
{30}.
5. Maximum of these minimums is 30 
Third element in output indicates
maximum of minimums of all windows of
size 3. 
6. Minimums of windows of size 3
are {10}, {20}, {10}, {10} and {10}.
7.Maximum of these minimums is 20. 
Similarly other elements of output are
computed.

Example 2:
Input:
N = 3
arr[] = {10,20,30}
Output: 30 20 10
Explanation: First element in output
indicates maximum of minimums of all
windows of size 1.Minimums of windows
of size 1 are {10} , {20} , {30}.
Maximum of these minimums are 30 and
similarly other outputs can be computed
"""
N = 7
arr= [10,20,30,50,10,70,30]
#this idea involves same method as contribution but unlike that here not added
#we want to find min so lets find for how many windows(subarry) the element is minimum
#remember when  we dont find the elemnets just write outside indexes
#class Solution():
def maxOfMin(arr,n):
    nse=[0]*n
    stack=[[-1,n]]
    for i in range(n-1,-1,-1):
        while len(stack)!=1 and stack[-1][0]>arr[i]:
            stack.pop()
        nse[i]=stack[-1]
        stack.append([arr[i],i])
    pse=[]
    stack=[[-1,-1]]
    for i in range(n):
        while len(stack)!=1 and stack[-1][0]>=arr[i]:
            stack.pop()
        pse.append(stack[-1])   
        stack.append([arr[i],i])
    ans=[0]*n
    for i in range(n):
        index=(nse[i][1]-(pse[i][1]+1))
        if ans[index-1]<arr[i]:
            ans[index-1]=arr[i]
    for i in range(n-2,-1,-1):
        ans[i]=max(ans[i],ans[i+1])
    return ans
print(maxOfMin(arr,N))
