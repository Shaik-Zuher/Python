class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
def push(head,data):
    new=Node(data)
    if head==None:
        head=new
        return head 
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=new
    return head 
def pop(head):
    if head==None:
        return -1
    temp=head
    if not head.next:
        head=None
        return head
    while temp.next.next!=None:
        temp=temp.next
    temp.next=None
    return head 
def display(head):
    temp=head
    while temp:
        print(temp.data,end=",")
        temp=temp.next
    return None
head=push(head,20)
head=push(head,30)
display(head)
head=pop(head)
display(head)
