#polymorphism- 1 object diferrent forms
#+ opeartor used for addition and conactination so it is called overloading
#!!!!!!!!!!!!!!!!!!!!!1Python does'nt support function,comstructor overloading ony erator overloadng possible
class Arithematic:
    def Add(self,a):#forgotten
        print(a)
    def Add(self,a,b):#forgotten
        print(a+b)
    def Add(self,a,b,c):#recent created functin is considered
        print(a+b+c)
obj=Arithematic()
# obj.Add(1) #shows error missing one missing position
#obj.Add(1,2)#shows error missing two missing position
obj.Add(1,2,3)
#This overloading--complie time polymorphism because it happens during compile time
