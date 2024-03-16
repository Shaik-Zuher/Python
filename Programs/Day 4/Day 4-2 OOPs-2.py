#car showroom  detailed price and milage displayed
#in car showroom there are three car companies toyota,mahendra and mercedies
#take input from user for car company name and in input message give user three options 3 companies this user input company name goes as input\argument to model name function,which welcomes user accordingly to company name.ask user to enter specific model name for that company
#second function whose name is variant.According to the car company name and car model the user should to ask to enter the variant he would like to choose from petrol,diesel
#lastfunction hopefuly display according to car company car model name and car vraiant first its ex-showroom price,onroad price should be displayed,calculated as ex-showroom price+CGST+SGST+insurance.
#SGST,CGST and insurance all 3 have common value  throughout the car showroom(percentage)
class Car:
    def __init__(self):
        self.SGST=50
        self.CGST=20
        self.insurance=10
    def BX(self,variant):
        if(variant=="1" or variant=="Petrol"):
            bx1=300000
            print("Car Company Toyota")
            print("Car Model BX")
            print("Car Variant Petrol")
            print("Ex-showroom Price",bx1)
            print("On-road Price",(bx1+((self.CGST/100)*bx1)+(self.SGST/100)*bx1+(self.insurance/100)*bx1))
        elif(variant=="2" or variant=="Diesel"):
            bx2=300000
            print("Car Company Toyota")
            print("Car Model BX")
            print("Car Variant Diesel")
            print("Ex-showroom Price",bx2)
            print("On-road Price",(bx2+((self.CGST/100)*bx2)+(self.SGST/100)*bx2+(self.insurance/100)*bx2))
        else:
            print("Invalid")
    def CX(self,variant):
        if(variant=="1" or variant=="Petrol"):
            cx1=350000
            print("Car Company Toyota")
            print("Car Model CX")
            print("Car Variant Petrol")
            print("Ex-showroom Price",cx1)
            print("On-road Price",(cx1+((self.CGST/100)*cx1)+(self.SGST/100)*cx1+(self.insurance/100)*cx1))
        elif(variant=="2" or variant=="Diesel"):
            cx2=355000
            print("Car Company Toyota")
            print("Car Model CX")
            print("Car Variant Diesel")
            print("Ex-showroom Price",cx2)
            print("On-road Price",(cx2+((self.CGST/100)*cx2)+(self.SGST/100)*cx2+(self.insurance/100)*cx2))
        else:
            print("Invalid")      
    def FZ(self,variant):
        if(variant=="1" or variant=="Petrol"):
            fz1=400000
            print("Car Company Toyota")
            print("Car Model FZ")
            print("Car Variant Petrol")
            print("Ex-showroom Price",fz1)
            print("On-road Price",(fz1+((self.CGST/100)*fz1)+(self.SGST/100)*fz1+(self.insurance/100)*fz1))
        elif(variant=="2" or variant=="Diesel"):
            fz2=350000
            print("Car Company Toyota")
            print("Car Model CX")
            print("Car Variant Diesel")
            print("Ex-showroom Price",fz2)
            print("On-road Price",(fz2+((self.CGST/100)*fz2)+(self.SGST/100)*fz2+(self.insurance/100)*fz2))
        else:
            print("Invalid")
    def Tar(self,variant):
        if(variant=="1" or variant=="Petrol"):
             t1=300000
             print("Car Company Mahindra")
             print("Car Model Tar")
             print("Car Variant Petrol")
             print("Ex-showroom Price",t1)
             print("On-road Price",(t1+((self.CGST/100)*t1)+(self.SGST/100)*t1+(self.insurance/100)*t1))
        elif(variant=="2" or variant=="Diesel"):
             t2=300000
             print("Car Company Mahindra")
             print("Car Model Tar")
             print("Car Variant Diesel")
             print("Ex-showroom Price",t2)
             print("On-road Price",(t2+((self.CGST/100)*t2)+(self.SGST/100)*t2+(self.insurance/100)*t2))
        else:
             print("Invalid")
    def Jar(self,variant):
        if(variant=="1" or variant=="Petrol"):
             j1=350000
             print("Car Company Mahindra")
             print("Car Model Jar")
             print("Car Variant Petrol")
             print("Ex-showroom Price",j1)
             print("On-road Price",(j1+((self.CGST/100)*j1)+(self.SGST/100)*j1+(self.insurance/100)*j1))
        elif(variant=="2" or variant=="Diesel"):
             j2=355000
             print("Car Company Mahindra")
             print("Car Model Jar")
             print("Car Variant Diesel")
             print("Ex-showroom Price",j2)
             print("On-road Price",(j2+((self.CGST/100)*j2)+(self.SGST/100)*j2+(self.insurance/100)*j2))
        else:
             print("Invalid")
    def Kia(self,variant):
        if(variant=="1" or variant=="Petrol"):
             k1=400000
             print("Car Company Mahindra")
             print("Car Model Kia")
             print("Car Variant Petrol")
             print("Ex-showroom Price",k1)
             print("On-road Price",(k1+((self.CGST/100)*k1)+(self.SGST/100)*k1+(self.insurance/100)*k1))
        elif(variant=="2" or variant=="Diesel"):
             k2=350000
             print("Car Company Mahindra")
             print("Car Model Kia")
             print("Car Variant Diesel")
             print("Ex-showroom Price",k2)
             print("On-road Price",(k2+((self.CGST/100)*k2)+(self.SGST/100)*k2+(self.insurance/100)*k2))
        else:
             print("Invalid")
    def Gis(self,variant):
        if(variant=="1" or variant=="Petrol"):
            g1=1000000
            print("Car Company Mercedes")
            print("Car Model Gis")
            print("Car Variant Petrol")
            print("Ex-showroom Price",g1)
            print("On-road Price",(g1+((self.CGST/100)*g1)+(self.SGST/100)*g1+(self.insurance/100)*g1))
        elif(variant=="2" or variant=="Diesel"):
            g2=1100000
            print("Car Company Mercedes")
            print("Car Model Gis")
            print("Car Variant Diesel")
            print("Ex-showroom Price",g2)
            print("On-road Price",(g2+((self.CGST/100)*g2)+(self.SGST/100)*g2+(self.insurance/100)*g2))
        else:
            print("Invalid")
    def EQS(self,variant):
        if(variant=="1" or variant=="Petrol"):
            eqs1=1500000
            print("Car Company Mercedes")
            print("Car Model EQS")
            print("Car Variant Petrol")
            print("Ex-showroom Price",eqs1)
            print("On-road Price",((eqs1+((self.CGST/100)*eqs1)+(self.SGST/100)*eqs1+(self.insurance/100)*eqs1)))
        elif(variant=="2" or variant=="Diesel"):
            eqs2=1300000
            print("Car Company Mercedes")
            print("Car Model EQS")
            print("Car Variant Diesel")
            print("Ex-showroom Price",eqs2)
            print("On-road Price",(eqs2+((self.CGST/100)*eqs2)+(self.SGST/100)*eqs2+(self.insurance/100)*eqs2))
        else:
            print("Invalid")
    
while(1):
    Choice=input("Enter the car you want: 1.Toyota 2.Mahendra 3.Mercedes:")
    user=Car()
    if Choice=="1" or Choice=="Toyota":
        print("Welcome to Toyota Family")
        while(1):
            family=input("Enter the car you want: 1.BX 2.CX 3.FZ:")
            if(family=="1" or family=="BX"):
                user.BX(input("Enter the Varient 1.Petrol 2.Diesel:"))
                break
            elif(family=="2" or family=="CX"):
                user.CX(input("Enter the Varient 1.Petrol 2.Diesel:"))
                break
            elif(family=="3" or family=="FZ"):
                user.CZ(input("Enter the Varient 1.Petrol 2.Diesel:"))
                break
            else:
                print("invalid")
        break
    elif Choice=="2" or Choice=="Mahendra":
        print("Welcome to Mahendra Family")
        while(1):
            family=(input("Enter the car you want: 1.Tar 2.Jar 3.Kia:"))
            if(family=="1" or family=="Tar"):
                user.Tar(input("Enter the Varient 1.Petrol 2.Diesel:"))
                break
            elif(family=="2" or family=="Jar"):
                user.Jar(input("Enter the Varient 1.Petrol 2.Diesel:"))
                break
            elif(family=="3" or family=="Kia"):
                user.Kia(input("Enter the Varient 1.Petrol 2.Diesel:"))
                break
            else:
                print("invalid")
        break
    elif Choice=="3" or Choice=="Mercedes":
        print("Welcome to Mercedes Family")
        while(1):
            family=(input("Enter the car you want: 1.Gis 2.EQS:"))
            if(family=="1" or family=="Gis"):
                user.Gis((input("Enter the Varient 1.Petrol 2.Diesel:")))
                break
            elif(family=="2" or family=="EQS"):
                user.EQS((input("Enter the Varient 1.Petrol 2.Diesel:")))
                break
            else:
                print("invalid")
        break
    else:
        print("Enter proper value")
