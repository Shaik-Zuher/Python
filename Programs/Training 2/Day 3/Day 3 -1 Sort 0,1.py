#2->1->0->2->1->0
#otput must be 0->0->1->1->2->2
#Dont use sorting or extra spaces
#usng variables doenst occupy that much space
N=int(input("Enter Number of Nodes to Create:"))
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(2)
def display(head):
    temp=head
    while temp!=None:
        print(temp.data,end=" ")
        temp=temp.next
def insertate(n,head):
    NewNode=Node(n)
    temp=head
    while temp.next!=None:
        temp=temp.next
    temp.next=NewNode
def ort(head):
    temp=head
    c0=0
    c1=0
    c2=0
    while temp!=None:
        if(temp.data==0):
            c0+=1
        if(temp.data==1):
            c1+=1
        if(temp.data==2):
            c2+=1
        temp=temp.next
    temp1=head
    #reassigning
    while temp1!=None:
        while c0>0:
            temp1.data=0
            temp1=temp1.next
            c0-=1
        while c1>0:
            temp1.data=1
            temp1=temp1.next
            c1-=1
        while c2>0:
            temp1.data=2
            temp1=temp1.next
            c2-=1
while(N>0):
    insertate(int(input("Enter data:")),head)
    N-=1
display(head)
print()
ort(head)
display(head)
