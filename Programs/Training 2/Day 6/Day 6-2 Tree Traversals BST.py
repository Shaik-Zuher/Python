#################Trees and recursion are related###########################
#Get preorder traversal of tree
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(50)
def insert(root,data):
    if root==None:
        root=Node(data)
    if data<root.data:
        root.left=insert(root.left,data)
    if data>root.data:
        root.right=insert(root.right,data)
    return root
insert(root,5)
insert(root,10)
insert(root,55)
insert(root,60)
def preorder(root):
    if root==None:
        return   #important
    print(root.data)
    preorder(root.left)
    preorder(root.right)
preorder(root)
'''
#Get inorder Traversal of tree
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(50)
def insert(root,data):
    if root==None:
        root=Node(data)
    if data<root.data:
        root.left=insert(root.left,data)
    if data>root.data:
        root.right=insert(root.right,data)
    return root
insert(root,5)
insert(root,10)
insert(root,55)
insert(root,60)
def preorder(root):
    if root==None:
        return   #important
    preorder(root.left)
    print(root.data)
    preorder(root.right)
preorder(root)
'''
#get post order Traversal
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(50)
def insert(root,data):
    if root==None:
        root=Node(data)
    if data<root.data:
        root.left=insert(root.left,data)
    if data>root.data:
        root.right=insert(root.right,data)
    return root
insert(root,5)
insert(root,10)
insert(root,55)
insert(root,60)
def postorder(root):
    if root==None:
        return   #important
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")
postorder(root)
'''
#get levelorder Traversal
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(50)
def insert(root,data):
    if root==None:
        root=Node(data)
    if data<root.data:
        root.left=insert(root.left,data)
    if data>root.data:
        root.right=insert(root.right,data)
    return root
insert(root,5)
insert(root,10)
insert(root,55)
insert(root,60)
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
