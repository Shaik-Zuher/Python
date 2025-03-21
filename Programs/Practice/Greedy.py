#Greedy actually subtopic of dp and even sometimes heap.
#Greedy involves the point of becoming really greedy like man what does it even min.
#Greedy identified by optimal,maximum,minimum,smallest,largest.
#Like i always say minimum can be bs,heap,greedy,dp.

"""
Tip: When ever minimum is given in question first see if there is any monotoic nature(BS).
If no check greedy am i choose what is best while making decision--After that check heap(Because greedy comes with heap most time).
"""
#Dp min can be different as contraints will be always small around 200 like this seriously.
#Main point is in dp we break into sub problems and keep solving sub problems.
#While greedy is selecting optimally if we have something better then that is my answer I dont care about future.
#On other hand dp is even if i get answer i will leave it cause i know there can be something even better(Like rejecting deloite).
"""
Greedy Algorithms are approached to solve problems by making the current best choice at each stage with the hope of getting the best answer overall as well. At each step of the algorithm, we choose the best possible option available without considering the consequences of the choice in future steps.
####$$$  I feel sick!!!!!!!!!!!!!!!!!
"""
"""
Example for diff:
I have coins each coin can be infinite  and sum s my task is to get min coins equal to sum.
[4,1,2] and s=5  i need 2 coins(4+1).
[9,6,5,1] and s=10 i need 3 coins(9+9+1).
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
"""
678. Valid Parenthesis String

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
The following rules define a valid string:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true

Constraints:
1 <= s.length <= 100
s[i] is '(', ')' or '*'.
"""
#1)Using stack
#2)Lets try to be greedy
"""
You may think of appending (,* to stack and whenever ) appears stack.pop()
First prioritize ( cause * can be anything (or * or)
If no ( then pop *.
After all this is over you once again need to pop the ( and * stacks  as * can ) for ( stack elements
But make sure index of ( elements<index of *
if len(stack-[(])==0 true we dont care stack-[*] cause they can even be empty space
"""
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1=[]#for (
        s2=[]#for *
        for i in range(len(s)):
            if s[i]=="(":
                s1.append("(")
            elif s[i]=="*":
                s2.append("*")
            else:
                if not s1 and not s2:
                    return False
                if s1:
                    s1.pop()
                elif s2:
                    s2.pop()
        while s1 and s2 and s1[-1]<s2[-1]:
            s1.pop()
            s2.pop()
        return len(s1)==0
