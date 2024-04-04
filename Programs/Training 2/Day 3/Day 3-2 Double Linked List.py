#Create Double LInked List  with insertion and deletion operations
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
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
def iab(data,head):
    New=Node(data)
    New.next=head
    head.prev=New
    return New
def iae(data,head):
    New=Node(data)
    temp=head
    while temp.next!=None:
        temp=temp.next
    temp.next=New
    New.prev=temp
def dab(head):
    temp=head
    temp=temp.next
    return temp
def dae(head):
    temp=head
    while temp.next.next!=None:
        temp=temp.next
    temp.next=None
while(1):
    choice=int(input("1.Insertion At Begining\n2.Insert At Ending\n3.Delete at Begining\n4.delete at ending\n5.exit\nPerform Operation:"))
    
    if(choice==1):
        head=iab(1,head)
        display(head)
    if(choice==2):
        iae(40,head)
        display(head)
    if(choice==3):
        head=dab(head)
        display(head)
    if(choice==4):
        dae(head)
        display(head)
    if(choice==5):
        break
                 
        




