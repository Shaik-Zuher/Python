#Take a inout number generate that number of unique binary strings using recursion
n=int(input("Enter:"))
def binay(size,result,n):#1
    if size==n:#2
        print(result)#3
        return#4
    binay(size+1,result+'1',n)#5
    binay(size+1,result+'0',n)#6
binay(0,'',n)
    
#recursive stack
"""
lets say n=2
    (1,2,3,4)X,[5]r,6--b(2,"11",2)--stopped and printed
    (1,2,3,4)X,[5]r,6--b(1,"1",2)
    (1,2,3,4)X,[5]r,6--b(0,"",2)
#dry run
in first iteration-res="1"
in seond it-res

"""
"""output screen
"""


#2yYrb7yn
