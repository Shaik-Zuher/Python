class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
def push(head):
    def iate(head,data):
        new=Node(data)
        head.next=new
        return head
    
        
    
