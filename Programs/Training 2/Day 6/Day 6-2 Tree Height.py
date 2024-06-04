#heught not edges but nodes counted
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
def height(root):
    if root==None:#if tree empty
        return 0
    lheight=height(root.left)#check left height
    rheight=height(root.right)#check righht height
    if lheight>rheight:
        return 1+lheight
    else:
        return 1+rheight
print(height(root))
