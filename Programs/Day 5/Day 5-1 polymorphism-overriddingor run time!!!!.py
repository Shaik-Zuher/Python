#method-overridding possible in python
#this is run time polymorphism happens durring runtime
class Father:
    def bike(self):
        print("Splendor")
    def laptop(self):
        print("Laptop is 500GB")
class Son(Father):
    def laptop(self):
        print("Laptop is 1TB")
obj=Son()
obj.bike()
obj.laptop()
#contents of overridding functions can be accessd by super()
#contnts of overriding constructor can be accessed by super().__init__(self)
