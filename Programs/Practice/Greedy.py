#Greedy actually subtopic of dp and even sometimes heap.
#Greedy involves the point of becoming really greedy like man what does it even min
#Greedy identified by optimal,maximum,minimum,smallest.largest
#Like i always say minimum can be bs,heap,greedy,dp.
"""
Tip: When ever minimum is given in question first see if there is any monotoic nature
If no check greddy am i choose what is best while making decision--After that check heap(Because greedy comes with heap most time)
"""
#Dp min can be different as contraints will be always small around 200 like this seriously
#Main point is in dp we break into sub problems and keep solving sub problems
#While greedy is selecting optimally if we have something better then that is my answer I dont care about future
#On other hand dp is even if i get answer i will leave it cause i know there can be something even better(Like rejecting deloite)
"""
Greedy Algorithms are approached to solve problems by making the current best choice at each stage with the hope of getting the best answer overall as well. At each step of the algorithm, we choose the best possible option available without considering the consequences of the choice in future steps.
####$$$  I feel sick!!!!!!!!!!!!!!!!!
"""
"""
Example for diff:
I have coins each coin can be infinite  and sum s my task is to get min coins equal to sum
[4,1,2] and s=6  i need 2 coins(4+1)
[9,6,5,1] and s=10 i need 3 coins(9+9+1)
Here greedy fails
No this cannot be solved using Greedy apprach. (e.g., coins = {9, 6, 1} and sum = 11).
The greedy choice would pick {9,1,1} (3 coins), but the optimal solution is {6, 6} (2 coins).
"""
#Classic Fractional Knapsnack
"""
Problem Statement: The weight of N items and their corresponding values are given. We have to put these items in a knapsack of weight W such that the total value obtained is maximized.
Note: We can either take the item as a whole or break it into smaller units.
Example:
Input: N = 3, W = 50, values[] = {100,60,120}, weight[] = {20,10,30}.
Output: 240.00
Explanation: The first and second items  are taken as a whole  while only 20 units of the third item is taken. Total value = 100 + 60 + 80 = 240.00
"""
#I will think from small weight and keep on movie but i am gonna br greedy and want more val
#What will capacity think man
#Instead of having everything we can have fraction part right so for each index check which has more val for 1 unit weight
#sort these val(per unit) in descending order
#[weight for 1 unit,val,weight]=>[[5,100,20],[6,60,10],[4,120,30]]
#sort in desc and keep taking whenever we get more break-done and dusted
class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, val, wt, capacity):
        store=[]
        for i in range(len(val)):
            store.append([val[i]/wt[i],val[i],wt[i]])
        store.sort(reverse=True)
        total=0
        mval=0
        for i in store:
            if total+i[2]<=capacity:
                total+=i[2]
                mval+=i[1]
            else:
                diff=capacity-total
                mval+=(i[0]*diff)
                break
        return mval
