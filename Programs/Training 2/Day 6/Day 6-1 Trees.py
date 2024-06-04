#tree is not linear ds
#height and depth both are same things but height is for whole tree but depth can be for node also
#depth of node= depth from root to particular node
#complete binary tree:conditions:1)All Nodes in level must be filled before going to next level(next level need not to be filled completely)
#                               2)nodes must be filled from left to right
#     1
#   /   \
#   3   2
# /  \
#4    5        #this is binary tree
#     1
#   /   \
#   3   2
# /  
#4            #this is binary tree
#     1
#   /   \
#   3   2
#   \
#    5        #this not is binary tree
#     1
#   /   
#   3   
# /  
#4           #this is not binary tree

#create a tree(same like linked list)

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
'''
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(1)
#insertion in bst
def insert(root,val):
    if root==None:#initially root is empty
        return Node(val)#created node
    if val<root.data:
        root.left=insert(root.left,val)#recursion to check on left
    elif val>root.data:
        root.right=insert(root.right,val)#recursion to check on right
    return root
insert(root,4)
#another way to insert
def insert(root,val):
    if root==None:#initially root is empty
       root=Node(val)#created node
    if val<root.data:
        root.left=insert(root.left,val)#recursion to check on left
    elif val>root.data:
        root.right=insert(root.rigth,val)#recursion to check on right
    return root
'''
'''
#not the best one
def display(root):
    temp=root
    while temp.left!=None:
        print(temp.left.data)
        print(temp.data)
        print(temp.right.data)
        temp=temp.left
display(root)
'''

#traversl  4 types
#Inorder : left,root,right
#preorder:root,left,right
#postorder:left,right,root
#levelorder:prints in order of level(left to right).First prints all nodes in levl0 then level1 so on...
#     1
#   /   \
#   3   2
# /  \
#4    5        #this is binary tree
#level order will be 1->3->2->4->5
#To check if given tree is bst we can recurssivey check evry node orrrrrrr we can check if inordeer traversal is in ascending order

#inorder Traversal
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

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)
inorder(root)
