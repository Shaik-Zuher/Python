#create class ticket which will be abstract class inside that create function book ticket which will be abstract method  and has nothing in it
#create class makemytrip which will use book ticket function from ticket class to take details such as name,phone,number,email_id,jouney date and dislays msg saying thank you for booking from make my trip
#create class IRCTC  which uses book ticket class and takes same details as make my trip but in the end it will give option to user to select whether it is 1 way or round trip if user option is round trip it again asks the user to enter return date as well and prints mesage thank you for choosing ircts else it prints msg thanks for choosing irctc
#create class indigo which takes all details as irctc and just asks which mode of transport you want to go with train,flight,bus and displays thanks for choosing indigo
#class becomes abstract when @abstract method i.e (from abc import ABC,abstractmethod ) used at top
from abc import ABC,abstractmethod
class Ticket(ABC):
    @abstractmethod
    def book_ticket(self):
        pass
class MakeMyTrip(Ticket):
    def book_ticket(self,name,p_no,eid,journey):
        print("Ticket for ",name,"booked successfully.Boarding on",journey)
        print("Thank You for booking from MakeMyTrip")
class IRCTC(Ticket):
    def book_ticket(self,name,p_no,eid,journey):
        end_date=input("Want you want 1.One way trip 2.Round trip")
        if(end_date=="1" or end_date=="One way trip"):
            print("Ticket for ",name,"booked successfully.Boarding on",journey)
            print("Thank You for booking from IRCTC")
        elif(end_date=="2" or end_date=="Round Trip"):
            end=input("Enter the return date:")
            print("Ticket for ",name,"booked successfully.Boarding on",journey,"Return date",end)
            print("Thank You for booking from IRCTC")
        else:
            print("Invalid")
class Indigo(Ticket):
    def book_ticket(self,name,p_no,eid,journey):
        choice=input("What you want 1.Flight 2.Train 3.Bus")
        if(choice=="1" or choice=="Flight"):
            end_date=input("Want you want 1.One way trip 2.Round trip")
            if(end_date=="1" or end_date=="One way trip"):
                print("Ticket for ",name,"booked successfully.Boarding on",journey)
                print("Thank You for booking from Indigo")
            else:
                end=input("Enter the return date:")
                print("Ticket for ",name,"booked successfully.Boarding on",journey,"Return date",end)
                print("Thank You for booking from Indigo")
        elif(choice=="2" or choice=="Train"):
            end_date=input("Want you want 1.One way trip 2.Round trip")
            if(end_date=="1" or end_date=="One way trip"):
                print("Ticket for ",name,"booked successfully.Boarding on",journey)
                print("Thank You for booking from Indigo")
            else:
                end=input("Enter the return date:")
                print("Ticket for ",name,"booked successfully.Boarding on",journey,"Return date",end)
                print("Thank You for booking from Indigo")
        elif(choice=="3" or choice=="Bus"):
            end_date=input("Want you want 1.One way trip 2.Round trip")
            if(end_date=="1" or end_date=="One way trip"):
                print("Ticket for ",name,"booked successfully.Boarding on",journey)
                print("Thank You for booking from Indigo")
            else:
                end=input("Enter the return date:")
                print("Ticket for ",name,"booked successfully.Boarding on",journey,"Return date",end)
                print("Thank You for booking from Indigo")
        else:
            print("Invalid")
inp=input("Enter want you want 1.Make My Trip 2.Irctc 3.Indigo:")
if(inp=="Make My Trip" or inp=="1"):
   obj=MakeMyTrip()
   obj.book_ticket(input("Enter name:"),input("Enter phone:"),input("Enter email:"),input("Enter journey date:"))
elif(inp=="Irctc"or inp=="2"):
    obj1=IRCTC()
    obj1.book_ticket(input("Enter name:"),input("Enter phone:"),input("Enter email:"),input("Enter journey date:"))
elif(inp=="Indigo"or inp=="3"):
    obj2=Indigo()
    obj2.book_ticket(input("Enter name:"),input("Enter phone:"),input("Enter email:"),input("Enter journey date:"))
else:
    print("invalid selection")
