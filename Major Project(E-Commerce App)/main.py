#E-commerce App like Amazon
'''
#Features 
1.Login system
2.Cart System
'''
from Register import *
from Products import *
from Orders import *
while(1):
    visit=input("Is this your first visit Yes/No:")
    if visit=="Yes" or visit=="yes":
        register.reg()
        if log.login():
            shopping()
            exit=input("Do you want to Exit app(Yes/No):")
            if(exit=="Yes" or exit=="yes"):
                break
            elif(exit=="No" or exit=="no"):
                pass
            else:
                print("Invalid")
        else:
            print("No such user Exists Register For Account.")
            register.reg()
    elif visit=="No" or visit=="no":
        if(log.login()):
            shopping()
            exit=input("Do you want to Exit app(Yes/No):")
            if(exit=="Yes" or exit=="yes"):
                break
            elif(exit=="No" or exit=="no"):
                pass
            else:
                print("Invalid")
        else:
            print("No such user Exists Register For Account.")
            register.reg()
    else:
         print("Enter properly.")
