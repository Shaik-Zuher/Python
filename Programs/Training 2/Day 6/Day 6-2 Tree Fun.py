#tree is called a slef balanced height or a balanced tree if the absolute difference between the left and heght sholud be less than 1 or else it is called an self balanced or balanced trees then it is called AVL tree
#check if tree is avl or not
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(10)
r=Node(20)
l=Node(30)
rr=Node(40)
rl=Node(50)
root.left=l
root.right=r
r.left=rl
r.right=rr

def height(root):
    if(root==None):
        return 0
    lheight=height(root.left)
    rheight=height(root.right)
    if lheight>rheight:#we can also write rheight<lheight #when recursed for first time o is returned next time else block id recurrsed  
        return 1+lheight
    else:
        return 1+rheight
def balance(root):
    if(root==None):
        return 0
    balance(root.left)
    balance(root.right )
    lheight=height(root.left)
    rheight=height(root.right)
    if abs(lheight-rheight)<=1:
        return "AVL"
    else:
        return "Not AVL"
            
print(balance(root))
'''
#check the least common ancestor(common parent) for given nodes
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(50)
def insert(root,data):
    if root==None:
        root=Node(data)
    if(data<root.data):
        root.left=insert(root.left,data)
    if(data>root.data):
        root.right=insert(root.right,data)
    return root
insert(root,30)
insert(root,80)
insert(root,20)
insert(root,40)
insert(root,70)
insert(root,90)
insert(root,10)
insert(root,25)
insert(root,60)
insert(root,85)
def ancestor(root,m,n):
    if root==None:
        return
    if m<root.data and n<root.data:
        ancestor(root.left,m,n)
    if m>root.data and n>root.data:
        ancestor(root.right,m,n)
    else:
        return root.data
print(ancestor(root,10,25))
#find lowest common ancestor  not in bst but in bt
