#linked list and hashmap are related
"""In test cases they will say head is given but check if head is None this is mistake you do most of time"""
#one powerful algo is hare tortosie mechanism
#1 2 3 4 5 we have this find middle.
#turtle moves 1 poinet and hare moves 2 points
# 1 2 3 4 5
# t
# h
#1 2 3 4 5
#  t h
#1 2 3 4 5
#    t   h --done so hare.next!=Null
#even case
# 1 2 3 4 5 6
# t
# h
#1 2 3 4 5 6
#  t h
#1 2 3 4 5 6
#    t   h
#1 2 3 4 5 6
#      t      h --done so hare.next!=Null will gives error so take hare!=Null also
# so while hare and hare.next:
###############################
#This can be used for lot of things like finding loops inlinked lists
#1 2 3(3 once again connected to 1)
#t
#h
#  t
#h
#    t(met)
#    h
#when started both are same if they both are same somewher in point then there is loop we can use hashmap here
"""Can also be used t find length of loop once both meet keep one pointer in same place iterate another poinetr
with 1 step and count the nxt time they meet the count is given"""#while hare==turtle but before this make sure hare=hare.next so it acn enter loop
"""Can also be used to find starting point in loop
when both meet make turtle =head and incerment both with 1 the nxxt time they meet that is start
take examples and visuize in mind"""

"""
138. Copy List with Random Pointer
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
Return the head of the copied linked list.
The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
"""
#this can be solved using hashmap
#for every node create new node and map it ti original node
#next time traverse original head and connect next and random to new node created and mapped
#consider as map:
#
#  original node2:new node2
#  original node:new node    mapping
#####Or we can create new node and place them in middle of nodes
#we create new node and place them between original nodes
#next time we connect the random pointers
#next we connect their original nexts

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        temp=head
        #creating new nodes between original nodes
        #7[null]->6[1]->8[0]  randoms[]
        while temp:
            new=Node(temp.val)
            nx=temp.next
            temp.next=new
            temp=temp.next
            temp.next=nx
            temp=temp.next
        temp=head
        nx=temp.next
        #7[null]->7(c)[]->6[1]->6(c)[]->8[0]->8(c)[]    new nodes placed
        #first we store random poinetrs in varable valled rd but random points to original nodes but new nodes are next so temp.random.next
        #it can also be null so we place it in if-else loop
        #next we connect the random pointers
        #
        while temp:
            if temp.random:
                rd=temp.random.next
            else:
                rd=None
            #7[null]->7(c)[]->6[1]->6(c)[]->8[0]->8(c)[] rd=null
            #7[null]->7(c)[null]->6[1]->6(c)[]->8[0]->8(c)[]
            #7[null]->7(c)[null]->6[1]->6(c)[]->8[0]->8(c)[] rd=1
            #7[null]->7(c)[null]->6[1]->6(c)[1]->8[0]->8(c)[]
            temp.next.random=rd#for movings
            temp=temp.next.next
        temp=head
        x=nx
        #next we set the next pointers
        #removing links
        while temp.next and x.next:
            hnx=temp.next.next
            nnx=x.next.next
            temp.next=hnx
            x.next=nnx
            temp=temp.next
            x=x.next
        temp.next=None
        return nx
""""""
#ll can aso be used to find duplicate numbers
#if linear time not asked then hp can be used so we use ll instead
#think of numbers of nodes as number repeated there is loop for sure
#Let us deal our list as linked list, where i is connected with nums[i].
"""indices are connected to elements
Consider example 6, 2, 4, 1, 3, 2, 5, 2. Then we have the following singly-linked list:
0 -> 6 -> 5 -> 2 -> 4 -> 3 -> 1 -> 2 -> ...
We start with index 0, look what is inside? it is number 6, so we look at index number 6, what is inside? Number 5 and so on. Look at the image below for better understanding.
So the goal is to find loop in this linkes list. Why there will be always loop? Because nums[1] = nums[5] in our case, and similarly there will be always duplicate, and it is given that it is only one.
"""


"""Y shaped linked list find intersction point of 2 LL
1)BruteForce
2)hashmap/set--store one LL in hp/set  -O(m+n) space-o(m)  --Wont be liked want O(1) space
3)2 pointers alternate interchange(only once)
Take 2 pointers and traverse both LL simultaneously and when temp1 is null chsnge temp1 to head2 vice versa until interection found
Be carefull works only if there is confirm intersection otherwise TLE
4)when intersection may not be there use difference count find len of both diff=large-small 
start trvaerse from large point(index) in l(one) and then run parallel(l2)--boom works
"""
class Solution:
    def intersectPoint(self, head1, head2):
        t1=head1
        t2=head2
        while t1!=t2:
            if t1:
                t1=t1.next
            else:
                t1=head2
            if t2:
                t2=t2.next
            else:
                t2=head1
        return t1
