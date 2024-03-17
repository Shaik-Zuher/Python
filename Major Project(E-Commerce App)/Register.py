import csv
class Register:
    def reg(self):
        print("Welcome for Registration")
        self.username=input("Enter Name:")
        self.email=input("Enter Email:")
        self.phone=input("Enter Phone Number:")
        self.password=input("Enter password:")
        with open("details.csv","a",newline="") as file:
            a=csv.writer(file)
            a.writerow([self.username,self.email,self.phone,self.password])
register=Register()
class Login:
    def login(self):
        print("Welcome to Login")
        while(1):
            self.Name=input("Enter Username:")
            self.passed=input("Enter password:")
            with open("details.csv","r",newline="") as f:
                b=csv.DictReader(f)
                for col in b:
                    if col["Name"]==self.Name and col['Password']==self.passed:
                        print("Welcome",self.Name)
                        return True
                    elif col["Name"]==self.Name and col["Password"]!=self.passed:
                        print("Name exists but Invalid password")
                        print("Try Again")
                return False   
log=Login()