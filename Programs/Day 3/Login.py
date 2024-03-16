#Login creditianls
'''
def login():
    username=str(input("Enter username:"))
    password=str(input("Enter password:"))
    while username!=password:
        print("try again")
        username=str(input("Enter username:"))
        password=str(input("Enter password:"))
    if(username==password):
        print("Welcome")
    
login()
'''
def login():
    while 1:
        username=str(input("Enter username:"))
        password=str(input("Enter password:"))
        if(username==password):
            print("Welcome")
            break
        else:
            print("try again")
    
login()
