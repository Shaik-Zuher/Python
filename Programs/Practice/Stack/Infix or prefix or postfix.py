"""
Infix to Postfix
Given an infix expression in the form of string str. Convert this infix expression to postfix expression.
Infix expression: The expression of the form a op b. When an operator is in-between every pair of operands.
Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
Note: The order of precedence is: ^ greater than * equals to / greater than + equals to -. Ignore the right associativity of ^.
Example 1:
Input: str = "a+b*(c^d-e)^(f+g*h)-i"
Output: abcd^e-fgh*+^*+i-
Explanation:
After converting the infix expression 
into postfix expression, the resultant 
expression will be abcd^e-fgh*+^*+i-
"""
#We want ans=""
#traverse string when alpanum add i to res and maintain stack of ops
#a+b*(c^d-e)^(f+g*h)-i
#  i      stack      res
#  a                  a
#  +       +          a
#  b       +          ab
#  *      +,*         ab
#  (      +,*,(       ab
#  c      +,*,(       abc   ####everytime opeartors added check priority of top when top priority is more it must be added to res
#  ^      +,*,(,^     abc   #### when we have ) we must add every op until top is (
#  d      +,*,(,^     abcd
#  -      +,*,(,^     abcd

class Solution:
    
    #priority.
    def priority(self,e):
        if e=="(":
            return -1
        if e=="^":
            return 2
        if e=="*" or e=="/":
            return 1
        else:
            return 0
    def InfixtoPostfix(self, exp):
        #code here
        operators=[]
        res=""
        for i in range(len(exp)):
            if exp[i].isalnum():
                res+=exp[i]
            elif exp[i]=="(":
                operators.append(exp[i])
            elif exp[i]==")":
                while operators[-1]!="(":
                    a=operators.pop()
                    res+=a
                operators.pop()
                #opeartor in stack should never be greater
            elif operators and self.priority(exp[i])<=self.priority(operators[-1]):
                while operators and self.priority(exp[i])<=self.priority(operators[-1]):
                    a=operators.pop()
                    res+=a
                operators.append(exp[i])
            else:
                operators.append(exp[i])
        while operators:
            if operators[-1]=="(":
                operators.pop()
            else:
                res+=operators.pop()
        return res
#prefix to infix
#-ab
#take stack and push letters when ever u come across symbol pop last 2 ele and add symbol and puh back in stcak
#from reverse
def infix(n):
            stack=[]
            res=""
            for i in range(len(n)-1,-1,-1):
                if n[i].isalnum():
                    stack.append(n[i])
                else:
                    f=stack.pop()
                    s=stack.pop()
                    m="("+f+n[i]+s+")"
                    stack.append(m)
            return stack[-1]
#this both mechansim can be used for anything.....
