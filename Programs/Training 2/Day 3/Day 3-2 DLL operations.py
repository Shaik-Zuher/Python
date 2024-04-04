'''
#delete value in DLL
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=Node(10)
first=Node(20)
second=Node(30)
head.next=first
first.next=second
first.prev=head
second.prev=first
def display(head):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next
def delete(n,head):
    temp=head
    while temp!=None and temp.data!=n:
        temp1=temp
        temp=temp.next
    temp.next.prev=temp1
    temp1.next=temp.next
delete(20,head)
display(head)
print(second.prev.data)
'''
#delete values in DLL such that function has 3 arguments linked list ,no of positions to skip and no of nodees to delete
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=Node(10)
first=Node(20)
second=Node(30)
third=Node(40)
head.next=first
first.next=second
second.next=third
first.prev=head
second.prev=first
third.prev=second
def display(head):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next
def delete(head,skip,nod):
    temp=head
    c=0
    n=0
    while temp!=None and c<skip:
        temp1=temp
        temp=temp.next
        c+=1
    while temp!=None and n<nod:
        temp1.next=temp.next
        temp.next.prev=temp1
        n+=1
        temp=temp.next
delete(head,1,2)
display(head)
