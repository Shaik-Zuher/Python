'''
class Faculty:
    def __init__(self,f_name,department,f_id):
        self.f_name=f_name
        self.department=department
        self.f_id=f_id
    def print_info(self):
        print("faculty information=",self.f_name,self.department,self.f_id)
obj=Faculty("Ashish","computer_science",1001)
obj.print_info()
#-----------------------------------------------------------------------
####when pass used then program executes even if class doesn't have an statements
class Cse(Faculty):
    pass
obj=Cse("JyotiMam","Computer_science",1002)
obj.print_info()
'''
#Create a class of name placements which has function info which displays "number of placements".
#create another class named department with function display which will display the names of departments present in college.
#create class pragati which function welcome which displays mesaage "welcome to pec we are glad to have you on board" this class sholud also display the details about departments and placements
'''#Mutiple inheritence approach
class Placements:
    def info(self):
        print("Number of placements are 1209 and still counting....")
class Department:
    def display(self):
        print("Departments:")
        print("Computer Science and Engineering")
        print("Information Technology")
        print("Mechanical Engineering")
        print("Electrical and Communications Engineering:")
        print("Electrical and Electronics Engineering")
        print("Civil Engineering")

class Pragati(Placements,Department):
    def welcome(self):
        print("Welcome To Pragati Engineering College.We are glad to have you on Board")
obj=Pragati()
obj.welcome()
obj.info()
obj.display()
'''
'''
#Mutli level inheritence approach
class Placements:
    def info(self):
        print("Number of placements are 1209 and still counting....")
class Department(Placements):
    def display(self):
        print("Departments:")
        print("Computer Science and Engineering")
        print("Information Technology")
        print("Mechanical Engineering")
        print("Electrical and Communications Engineering:")
        print("Electrical and Electronics Engineering")
        print("Civil Engineering")

class Pragati(Department):
    def welcome(self):
        print("Welcome To Pragati Engineering College.We are glad to have you on Board")
obj=Pragati()
obj.welcome()
obj.info()
obj.display()
'''
'''
#Hierchrcial
#Lets say bardock has 2 children goku,radditz but radditz,goku inherted properties of bardock but goku amd radditz have no realtion
class Placements:
    def info(self):
        print("Number of placements are 1209 and still counting....")
class Department(Placements):
    def display(self):
        print("Departments:")
        print("Computer Science and Engineering")
        print("Information Technology")
        print("Mechanical Engineering")
        print("Electrical and Communications Engineering:")
        print("Electrical and Electronics Engineering")
        print("Civil Engineering")

class Pragati(Placements):
    def welcome(self):
        print("Welcome To Pragati Engineering College.We are glad to have you on Board")
obj=Pragati()
obj.welcome()
obj.info()
obj2=Department()
obj2.display()
'''
#Hybrid
#combination of 2 0r more inheritence
class Placements:
    def info(self):
        print("Number of placements are 1209 and still counting....")
class Department(Placements):
    def display(self):
        print("Departments:")
        print("Computer Science and Engineering")
        print("Information Technology")
        print("Mechanical Engineering")
        print("Electrical and Communications Engineering:")
        print("Electrical and Electronics Engineering")
        print("Civil Engineering")
class Pragati(Department,Placements): ####here be crefull classes must be passed in order of functions called.
    def welcome(self):
        print("Welcome To Pragati Engineering College.We are glad to have you on Board")
obj=Pragati()
obj.welcome()
obj.info()
obj.display()
