#A=11->22->33
#B=12->21->34
#Crete LL with sorted above
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
A=Node(11)
A1=Node(22)
A2=Node(33)
B=Node(12)
B1=Node(21)
B2=Node(34)
A.next=A1
A1.next=A2
B.next=B1
B1.next=B2
def merge(A,B):
    Dummy=Node(-1)
    current=Dummy
    while A!=None and B!=None:
        if A.data<=B.data:
            current.next=A.data
            A=A.next
        else:
            current.next=B.data
            B=B.next
        current=current.next
    if(A!=None):
        current.next=A
    if(B!=None):
        current.next=B
    return Dummy.next
def display(head):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next
merge(A,B)
display()
