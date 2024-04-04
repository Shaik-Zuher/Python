#BE CAREFULL IN ASSESSMENTS THEY SAY INPUT WILL BE GIVEN THROUGH CONSOLE BUT IF YOU USE USER INPUT IT GIVES ERROR
#THIER INPUT IS  22 33 44
#TO STORE THEM IN VARIUS VARIABLES
a,b,c=map(int,input.split(''))
#NOW 3 VALUES STORED IN A,B,C THE INT TELLS TO STORE VALUE AS INTEGER
######Note-Like js python has scopes
#varibles declared in function can'T be used outside
#If you wnat to use just use return(yawn) but make use to store return value oustide in new varibel to use it
#for exmaple def king():
#                 return hello
#hello=king()
#temp.next won't have of next node but address think carefully buddy temp.next.data has data
#try this
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(1)
first=Node(2)
second=Node(3)
third=Node(4)
head.next=first
first.next=second
second.next=third
print(first.next)
print(first.next.data)
#another thing
def iab(head):
    new=Node(1)
    new.next=head
    temp=head
    while temp.next!=head:
        temp=temp.next
    temp.next=new
    return new
#whenever you use head in LL make sure to return it at end(same head or update head)
#by the way head means just a first node whuch acts as pointer from where iteartion starts
