#create class f15 with functions lights,fan,ac,display
#light-prints color of light which is taken as parameter to function
#fan-displays regulator speed in which is taken as parameter to function
#AC-displays current room temperature and outside temperature which are taken aa parameters
#display-prints difference in outside temp and room temp from ac and also diplays fan speed
'''
class f15:
    def light(self,colour):
        print(colour,"is color of light")
    def fan(self,speed):
        self.speed=speed
    def AC(self,rt,ot):
        self.rt=rt
        self.ot=ot
        print("room temperature is:",rt)
        print("outside temperature is:",ot)
    def display(self):
        temp=self.ot-self.rt
        print("Differnce is",temp)
        print("Regulator speed is:",self.speed)
person=f15()
person.light("red")
person.fan(4)
person.AC(16,32)
person.display()
'''
#self keyword is like this(js,java)
#self need not be denoted with self it can be another word like M
class f15:
    def __init__(M,cst,cnt):
        M.cst=cst
        M.cnt=cnt
        print("Constructor is function called automatically when object is created as well as allocates memory allocation to variable")
    def light(M,colour):
        print(colour,"is color of light")
    def fan(M,speed):
        M.speed=speed
    def AC(M,rt,ot):
        M.rt=rt
        M.ot=ot
        print("room temperature is:",rt)
        print("outside temperature is:",ot)
    def display(M):
        temp=M.ot-M.rt
        print("Differnce is",temp)
        print("Regulator speed is:",M.speed)
        print("Class start time:",M.cst)
        print("Class end time:",M.cnt)
person=f15("9.00AM","3.55PM")
person.light("red")
person.fan(4)
person.AC(16,32)
person.display()
# constructor syntax id def __init__(self):---double underscore are used.
