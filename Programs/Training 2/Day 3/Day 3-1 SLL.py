#reverse linked list
#dont try to use lists for sll
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
second=Node(20)
third=Node(30)
four=Node(40)
head.next=second
second.next=third
third.next=four
def reverse(head):
    prev=None
    current=head
    while current!=None:
        x=current.next
        current.next=prev
        prev=current
        current=x
    return prev
def display(head):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next
head=reverse(head)
display(head)
'''
#reverse particular portion in linked list
#Example : 1 2 3 4 5 6 (reverse by 3) 3 2 1 6 5 4
'''
lets say    1     2     3     4     5     6
           head
    prev   curr   next
ant to reverse 3  3 elemnets
3    2     1     4   5    6
          head
   prev    curr   nxt
   so head.next=recursion
if there are no elements for example you have only 10 20 30 and reverse 3 elements
30 20 10
    p  c x
       h
if x=null we must stop so check it
         
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
sec=Node(20)
third=Node(30)
four=Node(40)
head.next=sec
sec.next=third
third.next=four
def display(head):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next
def partrev(n,head):
    count=0
    previous=None
    current=head
    while current!=None and count<n:
        x=current.next
        current.next=previous
        previous=current
        current=x
        count+=1
    if(x!=None):
        head.next=partrev(n,x)
    return previous
head=partrev(2,head)
display(head)
    
