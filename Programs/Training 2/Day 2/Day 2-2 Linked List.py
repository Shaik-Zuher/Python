#in Python there is no null instead we have None
#head pointing the first node
'''
#Create 4 nodes and link them and diplay the heads with loop inside function and parameter must be head
class Node:
    def __init__(self,data):
        self.data=data#has data
        self.next=None#has address
head=Node(23)
first=Node(70)
second=Node(50)
third=Node(100)
head.next=first
first.next=second
second.next=third
def display(head):
    temp=head#becuse head eill be changed
    while temp!=None:
        print(temp.data)
        temp=temp.next
display(head)
class Link:
    def __init__(self,data):
        self.d=data
        self.x=None
    def display(self,h):
        temp=h
        while temp!=None:
            print(temp.d)#best to write display function outside class can be pretty confusing
            temp=temp.x
head=Link(10)
sec=Link(20)
third=Link(30)
four=Link(40)
head.x=sec
sec.x=third
third.x=four
head.display(head)
'''
#insert at beginning

#Create a function tha has argument head and data which must be added at front of list
class Node:
    def __init__(self,data):
        self.data=data#has data
        self.next=None#has address
head=Node(20)
first=Node(23)
second=Node(70)
third=Node(50)
Four=Node(100)
head.next=first
first.next=second
second.next=third
third.next=Four
def display(head):
    temp=head#becuse head will be changed
    while temp!=None:
        print(temp.data)
        temp=temp.next
def Insert_At_beginning(data,head):
    New=Node(data)
    New.next=head
    head=New
    return head
head = Insert_At_beginning(10,head)#when value is returned the head must be updated sounds like crap
display(head)
'''
#Insert at ending
class Node:
    def __init__(self,data):
        self.data=data#has data
        self.next=None#has address
head=Node(20)
first=Node(23)
second=Node(70)
third=Node(50)
head.next=first
first.next=second
second.next=third

def display(head):
    temp=head#becuse head will be changed
    while temp!=None:
        print(temp.data,end=" ")
        temp=temp.next
def Insert_At_beginning(data,head):
    New=Node(data)
    New.next=head
    head=New
    print("New Node created")
    return head
def Insert_ate(data):
    New=Node(data)
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=New
head=Insert_At_beginning(10,head)
Insert_ate(100)
display(head)
'''
