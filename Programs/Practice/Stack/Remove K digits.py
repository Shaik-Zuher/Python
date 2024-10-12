"""
402. Remove K Digits
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""
#main point is we need to remove numbers in front to make number small 
#so stack and traverse and append
#when ever stack[-1]>i remove and decrment k
#edgecases
#1)sometimes k wholelly will not be decremented again write it
#2)empty stack case return 0
#3)we can even have leading 0 like "0010" so str(int(number))---works
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack=[]
        for i in num:
            while k!=0 and stack and stack[-1]>i:
                stack.pop()
                k-=1
            stack.append(i)
        while k!=0:
            stack.pop()
            k-=1
        if not stack:
            return "0"
        res="".join(stack)
        return str(int(res))
