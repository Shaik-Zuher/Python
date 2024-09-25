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
#for example     1 2 30 25
#take 2            it is min of 3 windows[2],[2,30],[2,30,25](i.e len of array)
#                  0 on right(as 1 is min)(i.e -1) we would get [2] but it is duplicate to prevent this we keep>= see in code
#nse=[[2,1(index)],[30,2],[-1,4],[-1,4]]
#pse=[[-1,-1],[1,0],[2,1],[2,1]]
#to get number of windows for 25  (4(nsei)-1(psei))=3 but we want is 2 as psei is min index we need to add 1 to it to prevent index errors as indexing starting from 0 to fixe this pse[i]+1(this is also becuase of so called >= symbol)
#[0,0,0,0]ans becuse we have 4 lengths windows
#number of windows of elements [4,3,1,2]
#we think idea that our value is for which window size our ele is max for example if 2 then element(i.e max for window size 2)that means its alraedy max for window size1
#we can get values 4 to prevnt (it index-1)
#ans [0,0,0,1] first iteration(i.e elmet 1 of[1,2,30,25],windows[1,1,2,2])
#ans [0,0,2,1] second iteration 
#ans[30,0,2,1]
#ans[30,25,2,1]
####This is answer
######We have situations like we have place elemnt at index but there is alredy index in place for example 25,2 both have window 2 .2 alreedy placed at index1 now 25 must also be placed at 1 here 25>2 so change it 
#some times we have [70,0,0,2] like this the 0 tells that for all those windows the window with value(is ans)
##so revrse check and max(ans[i],ans[i+1])--every element
#ans will be [70,2,2,2]
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
        while len(stack)!=1 and stack[-1][0]>=arr[i]:#####################here >=
            stack.pop()
        pse.append(stack[-1])   
        stack.append([arr[i],i])
    ans=[0]*n
    for i in range(n):
        #placeing at index
        #how to figure this you just try to do differnt caluculations like *,+,/ and find how can you get answers
        index=(nse[i][1]-(pse[i][1]+1))
        #check alredy presnt element greater or what
        if ans[index-1]<arr[i]:
            ans[index-1]=arr[i]
    #replacing zeroes
    for i in range(n-2,-1,-1):
        ans[i]=max(ans[i],ans[i+1])
    return ans
print(maxOfMin(arr,N))
