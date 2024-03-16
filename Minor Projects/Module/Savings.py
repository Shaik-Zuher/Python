class Bank:
    def __init__(self,savings):
        self.sv=savings
    def withdraw(self):
        print("Money in Bank:",self.sv)
cd=Bank("100000")

            
