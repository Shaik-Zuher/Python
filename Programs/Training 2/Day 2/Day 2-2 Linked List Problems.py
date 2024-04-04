#count elemnets in linked list and mid value
#temp.next won't have of next node but address think carefully buddy temp.next.data has data
'''
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
    array=[]
    temp=head#becuse head will be changed
    while temp!=None:
        array.append(temp.data)
        temp=temp.next
    print("elements=",array)
    mid=len(array)//2
    print("Middle Element",array[mid])
    print("Count is ",len(array))
display(head)
'''
#deletion in linked list using function
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(1)
first=Node(2)
second=Node(3)
third=Node(4)
head.next=first
first.next=second
second.next=third
def display(head):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next
def delete(n,head):
    temp=head
    while temp.data!=n:
        temp=temp.next
    temp1=head
    while temp1.data<=n:
        temp1=temp1.next
        print(temp1.next)
    temp.next=temp1.next
l=int(input("Enter a Number:"))
delete(l,head)
display(head)
'''
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(1)
first=Node(2)
second=Node(3)
third=Node(4)
head.next=first
first.next=second
second.next=third
def delete(n,head):
    temp=head
    while temp.next!=None:
        if temp.next.data==n:
            temp.next=temp.next.next
            return temp.next
        temp=temp.next
def display(head):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next            
delete(int(input("Enter a Number:")),head)
display(head)
'''
#deletion of middle node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(1)
first=Node(2)
second=Node(3)
third=Node(4)
four=Node(5)
#five=Node(6)
head.next=first
first.next=second
second.next=third
third.next=four
#four.next=five
def display(head):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next
def deletem(head):
    temp=head
    count=0
    while temp!=None:
        count+=1
        temp=temp.next
    c=count//2
    print(c)
    c1=1
    temp1=head
    while temp1!=None:
        c1+=1
        if c1==c:
            temp1.next=temp1.next.next
        temp1=temp1.next
deletem(head)
display(head)
