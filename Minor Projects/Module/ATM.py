#Create an ATM system
#displaying remianing amount to withdraw in ATM
#3 types of login 1,rupay 2.visa 3.mastercard
#Authentication of user when user is authenticated then give his following options to choose
#1.check balance--
#2.Cash Withdrawal
#during rupay can withdraw only 2000,for visa withdraw 5000 for mastercard 8500 else show trasaction limit exceeded--after withdrawal show balance
#3.Cash Deposit--total amount
#mini statement of last 3 transactions
from Login import log
from Savings import cd
'''log.login()'''
class ATM:
    def __init__(self):
        self.ubal=10000
    def ulbal(self):
        print("Current Savings:",self.ubal)
    def rw(self):
        wi=int(input("Enter amount to withdraw:"))
        if(wi<=2000 and wi<self.ubal):
            print("Amount Withdrawn:",wi)
            self.ubal=self.ubal-wi
        elif(wi>2000 and wi<=self.ubal):
            print("Transaction Limit exceeded")
        else:
            print("Savings Insufficient")
    def vw(self):
        wi=int(input("Enter amount to withdraw:"))
        if(wi<=5000 and wi<self.ubal):
            print("Amount Withdrawn:",wi)
            self.ubal=self.ubal-wi
        elif(wi>5000 and wi<=self.ubal):
            print("Transaction Limit exceeded")
        else:
            print("Savings Insufficient")
    def mcw(self):
        wi=int(input("Enter amount to withdraw:"))
        if(wi<=8500 and wi<self.ubal):
            print("Amount Withdrawn:",wi)
            self.ubal=self.ubal-wi
        elif(wi>8500 and wi<=self.ubal):
            print("Transaction Limit exceeded")
        else:
            print("Savings Insufficient")
    def bald(self):
        deposit=int(input("Enter amount to deposit:"))
        self.ubal=self.ubal+deposit
        print("Deposited:",deposit)
        print("Total savings:",self.ubal)
        
    
ATM=ATM()        
cd.withdraw()
while(1):
    card=input("1.Rupay\n2.Visa\n3.MasterCard\n4.Exit\nEnter Type of card:")
    if(card=="1" or card=="Rupay"):
       log.login()
       op=input("1.Check Balance\n2.Cash Withdrawal\n3.Cash deposit\nEnter Option:")
       match(op):
           case "1":
               ATM.ulbal()
           case "2":
                ATM.rw()
           case "3":
                ATM.bald()
           case _:
                print("Invalid")
    elif(card=="2" or card=="Visa"):
       log.login()
       op=input("1.Check Balance\n2.Cash Withdrawal\n3.Cash deposit\nEnter Option:")
       match(op):
           case "1":
               ATM.ulbal()
           case "2":
                ATM.vw()
           case "3":
                ATM.bald()
           case _:
                print("Invalid")
    elif(card=="3" or card=="MasterCard"):
       log.login()
       op=input("1.Check Balance\n2.Cash Withdrawal\n3.Cash deposit\nEnter Option:")
       match(op):
           case "1":
               ATM.ulbal()
           case "2":
                ATM.mcw()
           case "3":
                ATM.bald()
           case _:
                print("Invalid")
    elif(card=="4" or card=="Exit"):
        print("We look Forward To your Next visit")
        break
    else:
        print("Invalid")
