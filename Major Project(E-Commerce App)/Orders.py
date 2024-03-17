class Cart:
    def __init__(self):
        self.cart=0
        self.total=0
        self.items=[]
carty=Cart()
class Electronics:
    class Mobiles:
        def __init__(self):
            self.stock=300
            self.name="Mobile"
            self.bill=12000
            self.cart=0
        def display(self):
            print("Product Name:",self.name)
            print("Stock:",self.stock)
            print("Cost",self.bill)
            buy=input("Do You want to Place an Order?\n1.Yes\n2.No\n3.Add To Cart:\n")
            if (buy=="1" or buy=="Yes" or buy=="yes"):
                print("Your order has been placed")
                print("Your Bill:",self.bill)
                self.stock=self.stock-1
            elif(buy=="2" or buy=="No" or buy=="no"):
                print("Thanks for visiting")
            elif(buy=="3" or buy=="Add To Cart" or buy=="add to cart"):
                carty.cart=carty.cart+1
                carty.total=carty.total+self.bill
                carty.items.append(self.name)
            else:
                print("Invaid")
    class Watches(Mobiles):
        def __init__(self):
            self.stock=500
            self.name="Watches"
            self.bill=5000
    class Laptop(Mobiles):
         def __init__(self):
            self.stock=1000
            self.name="Laptops"
            self.bill=75000
class Groceries:
    class Vegetables:
        def __init__(self):
            self.stock=1000
            self.name="Vegetables"
            self.bill=150
        def display(self):
            print("Product Name:",self.name)
            print("Stock:",self.stock)
            buy=input("Do You want to Place an Order?\n1.Yes\n2.No\n3.Add To Cart:\n")
            if (buy=="Yes" or buy=="yes"):
                print("Your order has been placed")
                print("Your Bill:",self.bill)
                self.stock=self.stock-1
            elif(buy=="No" or buy=="no"):
                print("Thanks for visiting")
            elif(buy=="3" or buy=="Add To Cart" or buy=="add to cart"):
                carty.cart=carty.cart+1
                carty.total=carty.total+1
                carty.items.append(self.name)
            else:
                print("Invaid")
    class Fruits(Vegetables):
        def __init__(self):
            self.stock=500
            self.name="Fruits"
            self.bill=50
    class Oils(Vegetables):
         def __init__(self):
            self.stock=1000
            self.name="Oils"
            self.bill=750
class Textiles:
    class Men:
        def __init__(self):
            self.stock=300
            self.name="Mens Wear"
            self.bill=1200
        def display(self):
            print("Product Name:",self.name)
            print("Stock:",self.stock)
            buy=input("Do You want to Place an Order?\n1.Yes\n2.No\n3.Add To Cart:\n")
            if (buy=="Yes" or buy=="yes"):
                print("Your order has been placed")
                print("Your Bill:",self.bill)
                self.stock=self.stock-1
            elif(buy=="No" or buy=="no"):
                print("Thanks for visiting")
            elif(buy=="3" or buy=="Add To Cart" or buy=="add to cart"):
                carty.cart=carty.cart+1
                carty.total=carty.total+1
                carty.items.append(self.name)
            else:
                print("Invaid")
    class Women(Men):
        def __init__(self):
            self.stock=500
            self.name="Women wear"
            self.bill=5000
    class Kids(Men):
         def __init__(self):
            self.stock=1000
            self.name="Kids Wear"
            self.bill=2000
ele=Electronics()
mob=ele.Mobiles()
wat=ele.Watches()
lap=ele.Laptop()
gro=Groceries()
veg=gro.Vegetables()
fru=gro.Fruits()
oil=gro.Oils()
tex=Textiles()
m=tex.Men()
w=tex.Women()
k=tex.Kids()