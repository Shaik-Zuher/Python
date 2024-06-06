#Tree construction
#            5
#           / \
#          3   7                            #1 newnodes are kept being added in same level it is not going to below this is biggest mistake
#         / \  / \
#        1   2 6  8
class Node():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class construct():
    def AddNode(self,root,data):
        #creating nodes
        newNode=Node(data)
        #Check if root is null then val will be new root
        if root==None:
            return newNode#as root
        else:
            if data<root.val:
                '''
                root.left=newNode #this is mitske we do most of time #######1
                '''
                #check if root.left empty then add else recurse and move buddy
                if root.left==None:
                    root.left=newNode
                else:
                    self.AddNode(root.left,data)
            else:
                 #check if root.right empty then add else recurse and move buddy
                if root.right==None:
                    root.right=newNode
                else:
                    self.AddNode(root.right,data)
            return root
            
nodes=[16,9,28,4,10,93,8,15]
tree=construct()
root=None#orginally none right
for i in nodes:
    root=tree.AddNode(root,i)
print(root.left)

class Bst():
    def levelorder(self,root,tree):#write while loop instead of recursion
        if not root:
            return
        queue=[root]
        while len(queue)!=0:
            element=queue.pop(0)
            tree.append(element.val)
            if element.left:
                queue.append(element.left)
            if element.right:
                queue.append(element.right)
binary=Bst()
res=[]
binary.levelorder(root,res)
print(res)
