#preorder Traversal
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(1)
child1=Node(2)
child2=Node(3)
root.left=child1
root.right=child2

def preorder(root):
    if root is None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)
preorder(root)'''
#postorder Traversal
'''
print("post order")
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(1)
child1=Node(2)
child2=Node(3)
root.left=child1
root.right=child2

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)
postorder(root)
'''
#Level order Traversal(BFS)(must use queue)--think what you want
#my first element is always root(front data) so add it to queue
#Repeat this until quque is empty:
#1.Collect front data in variable ############
#2.Print and remove it from queue
#3.Add left child and right child of front data if exists
from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(1)
child1=Node(2)
child2=Node(3)
child1l=Node(5)
child1r=Node(6)
root.left=child1
root.right=child2
child1.left=child1l
child1.right=child1r

def levelorder(root):
    dq=deque()
    dq.append(root)
    while len(dq)!=0:
        r=dq[0]#This is necessary to collect
        print(r.data)
        dq.popleft()
        if(r.left!=None):
            dq.append(r.left)
        if(r.right!=None):
            dq.append(r.right)
levelorder(root)
