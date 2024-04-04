#insertion,deletion in Circular Linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
first=Node(20)
second=Node(30)
third=Node(40)
head.next=first
first.next=second
second.next=third
third.next=head
def display(head):
    temp=head
    while temp.next!=head:
        print(temp.data)
        temp=temp.next
    print(temp.data)
def iab(head):
    new=Node(1)
    new.next=head
    temp=head
    while temp.next!=head:
        temp=temp.next
    temp.next=new
    return new
def iae(head):
    new=Node(50)
    temp=head
    while temp.next!=head:
        temp=temp.next
    temp.next=new
    new.next=head
    return head
def delete(head,n):
    print("After deletion")
    temp=head
    if(n!=1):
        c=1
        while temp.next!=head and c<n:
            c+=1
            temp1=temp
            temp=temp.next
        temp1.next=temp.next
    if(n==1):
        temp1=head
        while temp1.next!=head:
            temp1=temp1.next
        temp1.next=temp.next
        return temp.next
        
head=iab(head)
print("Insertion At beginning")
display(head)
head=iae(head)
print("insertion at Ending")
display(head)
head=delete(head,1)
display(head)

